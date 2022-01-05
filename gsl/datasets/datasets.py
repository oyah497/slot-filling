from torch.utils.data import Dataset
from .templates import QueryTemplate, ResponseTemplate


class SLDataset(Dataset):
    """
    Slot filling dataset.
    Args:
        text_sl_data_list: [(sentence, entity list, slot), ...]
        query_schema:
        response_schema:
    """

    def __init__(self,
                 text_sl_data_list,
                 query_schema='description',
                 response_schema='plain'):
        super(SLDataset, self).__init__()
        self.text_sl_data_list = text_sl_data_list
        self.query_generator = QueryTemplate(query_schema)
        self.response_generator = ResponseTemplate(response_schema)
        self.x_text = []
        self.y_text = []
        self.generate_xy_text()

    def generate_xy_text(self):
        for sentence, entity, slot in self.text_sl_data_list:
            self.x_text.append(self.query_generator(sentence, slot))
            self.y_text.append(self.response_generator(entity))

    def __len__(self):
        return len(self.text_sl_data_list)

    def __getitem__(self, item):
        query = self.x_text[item]
        response = self.y_text[item]
        return query, response
