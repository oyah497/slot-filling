from gsl.data import generate_text_data
from gsl.data import SLDataset
from transformers import T5ForConditionalGeneration, T5Tokenizer
from torch.utils.data import DataLoader
from gsl.agents import Trainer

if __name__ == '__main__':
    train_data, valid_data, test_data = generate_text_data('./data', 'atis', shot_num=0)
    # print(train_data)
    # print(valid_data)
    # print(test_data)
    # train_dataset = SLDataset(train_data, 'a')
    # print(len(train_dataset))
    # for record in train_dataset:
    #     if ',' in record[1]:
    #         print(record)

    # model = T5ForConditionalGeneration.from_pretrained('t5-small')
    # print(model)
    # tokenizer = T5Tokenizer.from_pretrained('t5-small')
    # print(tokenizer)
    train_dataset = SLDataset(train_data)
    data_loader = DataLoader(train_dataset, batch_size=4, shuffle=False)
    mask = [0, 2]
    for query, response in data_loader:
        print(query)
        print(response)
        print(response[mask])
        break
    # train_dataloader = DataLoader(train_dataset, batch_size=5)
    # for batch in train_dataloader:
    #     print(batch)
    #     break
