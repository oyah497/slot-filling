from .utils import slot2description, slot2example


class QueryTemplate:
    def __init__(self, schema):
        if schema == 'description':
            self.template = 'sentence: %s. requirement: find the %s in the above sentence.'
        elif schema == 'example':
            self.template = 'sentence: %s. requirement: find entities like %s in the above sentence.'
        elif schema == 'mix':
            self.template = 'sentence: %s. requirement: find the %s, like %s, in the above sentence.'
        else:
            raise ValueError('Unsupported schema: %s.' % schema)
        self.schema = schema

    def __call__(self, sentence, slot):
        if self.schema == 'description':
            return self.template % (sentence, slot2description[slot])
        elif self.schema == 'example':
            return self.template % (sentence, ' and '.join(slot2example[slot]))
        elif self.schema == 'mix':
            return self.template % (sentence, slot2description[slot], ' and '.join(slot2example[slot]))
        else:
            return ValueError('Unknown Error!')


class ResponseTemplate:
    def __init__(self, schema):
        if schema == 'plain':
            self.template = '%s.'
        else:
            raise ValueError('Unsupported schema: %s.' % schema)
        self.schema = schema

    def __call__(self, entity):
        if self.schema == 'plain':
            return self.template % (', '.join(entity))
        else:
            raise ValueError('Unknown Error!')
