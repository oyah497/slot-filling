import argparse
import setting
from gsl.datasets import generate_text_data, SLDataset
from gsl import Trainer, seed_everything

parser = argparse.ArgumentParser(description='Set experiment args.')
parser.add_argument('tgt_domain', help='Target domain.', type=str,
                    choices=['AddToPlaylist',
                             'BookRestaurant',
                             'GetWeather',
                             'PlayMusic',
                             'RateBook',
                             'SearchCreativeWork',
                             'SearchScreeningEvent',
                             'atis'])
parser.add_argument('--seed', help='Global seed.', type=int, default=1129)
parser.add_argument('--model-name', help='Model name.', type=str, default='t5-small')
parser.add_argument('--batch-size', help='Batch size.', type=int, default=16)
parser.add_argument('--num-epochs', help='Train epochs.', type=int, default=100)
parser.add_argument('--lr', help='Learning rate of train step.', type=float, default=2e-5)
parser.add_argument('--query-max-seq-length', help='Max sequence length for query.', type=int, default=128)
parser.add_argument('--response-max-seq-length', help='Max sequence length for response.', type=int, default=64)
parser.add_argument('--num-beams', help='T5 generation beam number.', type=int, default=2)
parser.add_argument('--query-schema', help='Schema for query generation', type=str,
                    choices=['description',
                             'example',
                             'mix'], default='description')
parser.add_argument('--response-schema', help='Schema for response generation', type=str,
                    choices=['plain'], default='plain')
parser.add_argument('--shot-num', help='Shot number.', type=int, default=0)
parser.add_argument('--patience', help='Patience epoch for early stop.', type=int, default=5)

args = parser.parse_args()


def process_args():
    args.summary_dir = setting.SUMMARY_DIR
    args.dump_dir = setting.DUMP_DIR
    args.data_dir = setting.DATA_DIR
    args.exp_name = '%s-%s-%s' % (args.model_name, args.tgt_domain, args.shot_num)


process_args()
seed_everything(args.seed)


def train():
    train_data, valid_data, test_data = generate_text_data(args.data_dir,
                                                           args.tgt_domain,
                                                           shot_num=args.shot_num)
    train_dataset = SLDataset(train_data, query_schema=args.query_schema, response_schema=args.response_schema)
    valid_dataset = SLDataset(valid_data, query_schema=args.query_schema, response_schema=args.response_schema)
    test_dataset = SLDataset(test_data, query_schema=args.query_schema, response_schema=args.response_schema)

    trainer = Trainer(args.model_name, args)
    trainer.fit(train_dataset, valid_dataset, test_dataset,
                batch_size=args.batch_size, lr=args.lr, epochs=args.num_epochs, patience=args.patience,
                query_max_seq_length=args.query_max_seq_length, response_max_seq_length=args.response_max_seq_length,
                num_beams=args.num_beams)


if __name__ == '__main__':
    train()
