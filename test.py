from gsl.datasets import generate_text_data
from gsl.datasets import SLDataset
from transformers import T5ForConditionalGeneration, T5Tokenizer
from torch.utils.data import DataLoader
from gsl.agents import Trainer
import torch

if __name__ == '__main__':
    # train_data, valid_data, test_data = generate_text_data('./data', 'atis', shot_num=0)
    # print(train_data)
    # print(valid_data)
    # print(test_data)
    # train_dataset = SLDataset(train_data, 'a')
    # print(len(train_dataset))
    # for record in train_dataset:
    #     if ',' in record[1]:
    #         print(record)

    model = T5ForConditionalGeneration.from_pretrained('t5-base')
    model.eval()
    # print(model)
    tokenizer = T5Tokenizer.from_pretrained('t5-base')
    # print(tokenizer)
    query = ['sentence: what is the nearest movie house with window connection playing at lunch. requirement: find the movie name, like on the beat and for lovers only, in the above sentence.']
    query_token = tokenizer(query, padding=True,
                            truncation=True, max_length=128,
                            return_tensors="pt")
    query_ids, query_mask = query_token.input_ids, query_token.attention_mask
    with torch.no_grad():
        pred_ids = model.generate(
            input_ids=query_ids,
            attention_mask=query_mask,
            max_length=64,
            num_beams=2,
            repetition_penalty=2.5,
            length_penalty=1.0,
            early_stopping=True)
    pred_response = tokenizer.batch_decode(pred_ids, skip_special_tokens=True,
                                           clean_up_tokenization_spaces=True)
    print(pred_response)
    # train_dataset = SLDataset(train_data)
    # data_loader = DataLoader(train_dataset, batch_size=4, shuffle=False)
    # mask = [0, 2]
    # for query, response in data_loader:
    #     print(query)
    #     print(response)
    #     print(response[mask])
    #     break
    # train_dataloader = DataLoader(train_dataset, batch_size=5)
    # for batch in train_dataloader:
    #     print(batch)
    #     break
