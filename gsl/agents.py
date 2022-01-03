import os
import tqdm
import torch
import datetime
import numpy as np

from .metrics import tp_count
from collections.abc import Sequence
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader
from transformers import T5ForConditionalGeneration, T5Tokenizer


class EarlyStopping:
    """Early stops the training if validation loss doesn't improve after a given patience."""

    def __init__(self, patience=7, verbose=False, delta=0, mode='min', path='checkpoint.pt', trace_func=print):
        """
        Args:
            patience (int): How long to wait after last time validation loss improved.
                            Default: 7
            verbose (bool): If True, prints a message for each validation loss improvement.
                            Default: False
            delta (float): Minimum change in the monitored quantity to qualify as an improvement.
                            Default: 0
            path (str): Path for the checkpoint to be saved to.
                            Default: 'checkpoint.pt'
            trace_func (function): trace print function.
                            Default: print
            mode (str): The more min or the max, the better.
        """
        self.patience = patience
        self.verbose = verbose
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.val_loss_min = np.Inf
        self.delta = delta
        self.path = path
        self.trace_func = trace_func
        self.mode = mode

    def __call__(self, value, model):
        if self.mode == 'min':
            score = -value
        else:
            score = value

        if self.best_score is None:
            self.best_score = score
            self.save_checkpoint(value, model)
        elif score < self.best_score + self.delta:
            self.counter += 1
            self.trace_func(f'EarlyStopping counter: {self.counter} out of {self.patience}')
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_score = score
            self.save_checkpoint(value, model)
            self.counter = 0

    def save_checkpoint(self, val_loss, model):
        """Saves model when validation loss decrease."""
        if self.verbose:
            if self.mode == 'min':
                info = f'Validation metric decreased ({self.val_loss_min:.6f} --> {val_loss:.6f}).  Saving model ...'
            else:
                info = f'Validation metric increased ({self.val_loss_min:.6f} --> {val_loss:.6f}).  Saving model ...'
            self.trace_func(info)
        torch.save(model.state_dict(), self.path)
        self.val_loss_min = val_loss


class Trainer:
    def __init__(self, model_name_or_path, args):
        self.model = T5ForConditionalGeneration.from_pretrained(model_name_or_path)
        self.tokenizer = T5Tokenizer.from_pretrained(model_name_or_path)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = self.model.to(self.device)

        timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d-%H%M%S')
        if hasattr(args, 'exp_name') and args.exp_name is not None:
            self.exp_name = f'{args.exp_name}-{timestamp}'
        else:
            self.exp_name = timestamp

        log_dir = os.path.join(args.summary_dir, self.exp_name)

        self.args = args
        self.writer = SummaryWriter(log_dir=log_dir)
        self.writer.add_text('args', str(self.args), global_step=0)

    def __del__(self):
        self.writer.flush()
        self.writer.close()

    def to_device(self, data):
        if isinstance(data, torch.Tensor):
            return data.to(self.device)
        elif isinstance(data, Sequence):
            return [self.to_device(item) for item in data]
        else:
            raise ValueError('Unsupported data type: %s.' % data.__class__.__name__)

    def fit(self,
            train_sl_dataset,
            valid_sl_dataset,
            test_sl_dataset,
            batch_size=16,
            lr=2e-5,
            epochs=100,
            patience=5,
            query_max_seq_length=128,
            response_max_seq_length=64,
            num_beams=2):
        train_dataloader = DataLoader(train_sl_dataset, batch_size=batch_size, shuffle=True)
        optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        save_model_path = os.path.join(self.args.dump_dir, 'ckpt.pt')
        test_mistake_record_path = os.path.join(self.args.dump_dir, '%s.record' % self.exp_name)
        early_stopping = EarlyStopping(patience=patience, verbose=True, mode='max', path=save_model_path)

        for epoch in range(epochs):
            self.model.train()
            train_epoch_loss = []
            train_bar = tqdm.tqdm(train_dataloader)
            for query, response in train_bar:
                query_token = self.tokenizer(query, padding=True,
                                             truncation=True, max_length=query_max_seq_length,
                                             return_tensors="pt")
                response_token = self.tokenizer(response, padding=True,
                                                truncation=True, max_length=response_max_seq_length,
                                                return_tensors='pt')
                query_ids, query_mask = query_token.input_ids, query_token.attention_mask
                response_ids, response_mask = response_token.input_ids, response_token.attention_mask

                query_ids, query_mask, response_ids, response_mask = self.to_device(
                    [query_ids, query_mask, response_ids, response_mask]
                )
                outputs = self.model(
                    input_ids=query_ids,
                    attention_mask=query_mask,
                    labels=response_ids,
                )
                loss = outputs.loss

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                train_epoch_loss.append(loss.item())
                train_bar.set_description(f'Epoch: [{epoch + 1}/{epochs}], loss: {loss.item():.6f}')

            train_loss = sum(train_epoch_loss) / len(train_epoch_loss)

            valid_f1, valid_precision, valid_recall, valid_loss = self.evaluate(
                valid_sl_dataset, batch_size, query_max_seq_length, response_max_seq_length, num_beams, with_loss=True
            )

            self.writer.add_scalars('loss', {'train': train_loss,
                                             'valid': valid_loss}, epoch)
            self.writer.add_scalars('f1', {'valid': valid_f1}, epoch)
            self.writer.add_scalars('precision', {'valid': valid_precision}, epoch)
            self.writer.add_scalars('recall', {'valid': valid_recall}, epoch)
            self.writer.flush()

            early_stopping(valid_f1, self.model)

            if early_stopping.early_stop:
                print('Early Stop!')
                break

        print("Evaluation on test dataset...")
        self.model.load_state_dict(torch.load(save_model_path))
        self.model = self.model.to(self.device)
        test_f1, test_precision, test_recall, test_loss = self.evaluate(
            test_sl_dataset, batch_size, query_max_seq_length, response_max_seq_length, num_beams, with_loss=True,
            mistake_record_path=test_mistake_record_path
        )
        test_result = f'F1: {test_f1:.6f}, precision: {test_precision:.6f}, ' \
                      f'recall: {test_recall:.6f}, loss: {test_loss:.6f}'
        self.writer.add_text('Test result', test_result, global_step=0)

    def evaluate(self,
                 dataset,
                 batch_size=16,
                 query_max_seq_length=128,
                 response_max_seq_length=64,
                 num_beams=2,
                 with_loss=False,
                 mistake_record_path=None):
        self.model.eval()
        data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=False)
        valid_bar = tqdm.tqdm(data_loader)
        loss_values = []
        tp = num_true = num_pred = 0
        mistake_records = []
        for query, response in valid_bar:
            query_token = self.tokenizer(query, padding=True,
                                         truncation=True, max_length=query_max_seq_length,
                                         return_tensors="pt")
            response_token = self.tokenizer(response, padding=True,
                                            truncation=True, max_length=response_max_seq_length,
                                            return_tensors='pt')
            query_ids, query_mask = query_token.input_ids, query_token.attention_mask
            response_ids, response_mask = response_token.input_ids, response_token.attention_mask

            query_ids, query_mask, response_ids, response_mask = self.to_device(
                [query_ids, query_mask, response_ids, response_mask]
            )
            if with_loss:
                with torch.no_grad():
                    outputs = self.model(
                        input_ids=query_ids,
                        attention_mask=query_mask,
                        labels=response_ids,
                    )
                loss = outputs.loss
                loss_values.append(loss.item())

            pred_ids = self.model.generate(
                input_ids=query_ids,
                attention_mask=query_mask,
                max_length=response_max_seq_length,
                num_beams=num_beams,
                repetition_penalty=2.5,
                length_penalty=1.0,
                early_stopping=True)
            pred_response = self.tokenizer.batch_decode(pred_ids, skip_special_tokens=True,
                                                        clean_up_tokenization_spaces=True)
            _tp, _num_true, _num_pred, _mistake_records = tp_count(query, response, pred_response)
            tp += _tp
            num_true += _num_true
            num_pred += _num_pred

            if mistake_record_path is not None:
                mistake_records.extend(_mistake_records)

        if mistake_record_path is not None:
            with open(mistake_record_path, 'w') as f:
                for sample in mistake_records:
                    q, tr, pr = sample
                    record = '<query> %s\n' % q
                    record += '<true response> %s\n' % tr
                    record += '<pred response> %s\n' % pr
                    record += '\n'
                    f.write(record)

        epsilon = 1e-10
        precision = tp / (num_pred + epsilon)
        recall = tp / (num_true + epsilon)
        f1 = 2 * precision * recall / (precision + recall + epsilon)
        if len(loss_values) > 0:
            loss = sum(loss_values) / len(loss_values)
            return f1, precision, recall, loss
        return f1, precision, recall

    def predict(self,
                dataset,
                batch_size=16,
                query_max_seq_length=128,
                response_max_seq_length=64,
                num_beams=2):
        pass


class Predictor:
    pass
