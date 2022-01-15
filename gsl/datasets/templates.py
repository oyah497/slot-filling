from .utils import domain2desc, domainslot2desc, domainslot2example, domainslot2context


class QueryTemplate:
    def __init__(self, schema):
        if schema == 'slot_desc':
            self.template = 'find the %s in sentence: %s.'
        elif schema == 'slot_desc+domain_desc':
            self.template = 'in domain %s, find the %s in sentence: %s.'
        elif schema == 'example':
            self.template = 'find entities, like %s, in sentence: %s.'
        elif schema == 'context_example':
            self.template = 'find entities, like %s in %s, in sentence: %s.'
        elif schema == 'slot_desc+example':
            self.template = 'find the %s, like %s, in sentence: %s.'
        elif schema == 'slot_desc+context_example':
            self.template = 'find the %s, like %s in %s, in sentence: %s.'
        elif schema == 'slot_desc+domain_desc+context_example':
            self.template = 'in domain %s, find the %s, like %s in %s, in sentence: %s.'
        else:
            raise ValueError('Unsupported schema: %s.' % schema)
        self.schema = schema

    def __call__(self, domain, sentence, slot):
        if domain == 'atis':
            return 'find the %s in sentence: %s.' % (domainslot2desc[domain][slot], sentence)

        if self.schema == 'slot_desc':
            return self.template % (domainslot2desc[domain][slot], sentence)
        elif self.schema == 'slot_desc+domain_desc':
            return self.template % (domain2desc[domain], domainslot2desc[domain][slot], sentence)
        elif self.schema == 'example':
            return self.template % (domainslot2example[domain][slot], sentence)
        elif self.schema == 'context_example':
            return self.template % (domainslot2example[domain][slot], domainslot2context[domain][slot], sentence)
        elif self.schema == 'slot_desc+example':
            return self.template % (domainslot2desc[domain][slot], domainslot2example[domain][slot], sentence)
        elif self.schema == 'slot_desc+context_example':
            return self.template % (domainslot2desc[domain][slot], domainslot2example[domain][slot],
                                    domainslot2context[domain][slot], sentence)
        elif self.schema == 'slot_desc+domain_desc+context_example':
            return self.template % (domain2desc[domain], domainslot2desc[domain][slot],
                                    domainslot2example[domain][slot], domainslot2context[domain][slot],
                                    sentence)
        else:
            return ValueError('Unknown Error!')


class ResponseTemplate:
    def __init__(self, schema):
        if schema == 'plain':
            self.template = '%s.'
        else:
            raise ValueError('Unsupported schema: %s.' % schema)
        self.schema = schema

    def __call__(self, sentence, entity):
        if self.schema == 'plain':
            return self.template % (', '.join(entity))
        else:
            raise ValueError('Unknown Error!')
