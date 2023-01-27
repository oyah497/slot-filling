from .utils import domain2desc, domainslot2desc, domainslot2example, domainslot2context, domainslot2temp, domainslot2question, domainslot2dummy, domainslot2dummy2, slot2example_rcsf, slot2question_rcsf, slot2question_qa, domain2slots, domain2slotsnum, domainslot2desc2
from transformers import BartForConditionalGeneration, BartTokenizer

class QueryTemplate:
    def __init__(self, schema):
        if schema == 'slot_desc':
            self.template = 'find the %s in sentence: %s.'
        
        
        elif schema == 't5':
            self.template = 'question: %s context: %s, or unknown.'
        
        elif schema == 't5_said':
            self.template = 'question: %s context: The %s was unknown. Then he said \"%s\".'
        
        elif schema == 't5_openai':
            self.template = '%s \n the %s \n %s.'


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
            self.template = 'in domain %s, find the %s, like %s in %s, in sentence: %s, or not found.'
        
        elif schema == 'aisfg':
            self.template = 'in domain %s, find the %s, like %s in %s, in sentence: %s.'
        
        elif schema == 'aisfg_comp':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'sentence: %s. example: %s in %s. answer: like %s, the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'

        elif schema == 'min':
            self.template = '%s.'        
        
        elif schema == 'notSD':
            self.template = 'in domain %s, like %s in %s, in sentence: %s.'


        elif schema == 'proposed_query1':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'when he wants to %s, like %s in %s, in sentence %s. the %s is ' + f'{tokenizer.mask_token}' + '.'

        elif schema == 'proposed_query2':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'he wants to %s. in sentence: %s, the %s is %s. in sentence: %s, the %s is ' + f'{tokenizer.mask_token}' + '.'


        elif schema == 'each_slot':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            #self.template = bos + ' %s ' + sep + sep + ' %s. ' + sep + sep + ' %s ' + sep + sep + ' sentence: %s. ' + sep + sep + ' %s ' + sep
            self.template = bos + ' %s ' + sep + sep + ' sentence: %s. answer: %s ' + sep + sep + ' sentence: %s. answer: %s ' + sep
            self.mask_token = f'{tokenizer.mask_token}'

        elif schema == 'each_slot_dummy':
            #print('\nccccc\n')
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            #self.template = bos + ' %s ' + sep + sep + ' %s. ' + sep + sep + ' %s ' + sep + sep + ' sentence: %s. ' + sep + sep + ' %s ' + sep
            self.template = bos + ' %s ' + sep + sep + ' sentence: %s. answer: %s ' + sep + sep + ' sentence: %s. answer: %s ' + sep + sep + ' %s ' + sep
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'something':
            #print("\nbbbbbbbb\n")
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            self.template = bos + ' in domain %s, find the %s, like %s in %s, in sentence: %s. ' + sep + sep + ' the %s is %s. ' + sep
        
        elif schema == 'example_rcsf':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            self.template = bos + ' %s ' + sep + sep + ' %s ' + sep + sep + ' %s ' + sep + sep + ' sentence: %s. answer: %s ' + sep + sep + ' %s ' + sep
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'example_rcsf2':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            self.template = bos + ' %s ' + sep + sep + ' %s ' + sep + sep + ' %s ' + sep + sep + ' sentence: %s. answer: %s ' + sep + sep + ' %s ' + sep
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'example_rcsf3':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            self.template = bos + ' %s find the %s, like %s or %s. ' + sep + sep + ' sentence: %s. answer: %s ' + sep + sep + ' %s ' + sep
            self.mask_token = f'{tokenizer.mask_token}'


        elif schema == 'without_example':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            self.template = bos + ' %s ' + sep + sep + ' sentence: %s. answer: %s ' + sep + sep + ' %s ' + sep
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'unk_wo':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            unk = f'{tokenizer.unk_token}'
            self.template = bos + ' %s ' + sep + sep + ' sentence: %s. answer: %s ' + sep + sep + ' ' + unk + ' ' + sep
            self.mask_token = f'{tokenizer.mask_token}'

        elif schema == 'unk_rcsf':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            self.template = bos + ' %s ' + sep + sep + ' %s ' + sep + sep + ' %s ' + sep + sep + ' sentence: %s. answer: %s ' + sep + sep + ' %s ' + sep
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'dummy_unk':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            self.template = bos + ' %s ' + sep + sep + ' sentence: %s. answer: %s ' + sep
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'dummy_unk_ab':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            self.template = bos + ' %s ' + sep + sep + ' sentence: %s. answer: the %s is %s. ' + sep
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'dummy_unk2':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            self.template = bos + ' %s ' + sep + sep + ' sentence: %s. ' + sep + sep + ' answer: %s ' + sep
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'question: %s sentence: %s. answer: %s'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_ab':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            self.template = 'question: %s sentence: %s. answer: the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_or':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'question: %s sentence: %s, or unknown. answer: %s'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_rcsf':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'question: %s sentence: %s. answer: %s'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_qa':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'question: %s sentence: %s. answer: %s'
            self.mask_token = f'{tokenizer.mask_token}'

        elif schema == 'nosep_rcsf_ab':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            self.template = 'question: %s sentence: %s. answer: the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_rcsf_or':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'question: %s sentence: %s, or unknown. answer: %s'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_rcsf_ex2':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'question: %s sentence: %s. answer: like %s or %s, %s'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_rcsf_ex2_long':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'question: %s sentence: %s. example: %s %s answer: %s'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_rcsf_ex2_long_ab':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'question: %s sentence: %s. example: the %s is %s. the %s is %s. answer: the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_rcsf_ex2_slots':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'question: %s positive: %s. negative: %s. sentence: %s. answer: like %s or %s, %s'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_rcsf_ex2_upper':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'Question: %s Sentence: %s. Answer: Like %s or %s, %s'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_rcsf_ex2_negex':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'question: %s examples of incorrect entities are %s. sentence: %s. answer: like %s or %s, %s'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_rcsf_ex2_ab':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'question: %s sentence: %s. answer: like %s or %s, the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_rcsf_ex2_ab_or':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'question: %s sentence: %s, or unknown. answer: like %s or %s, the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_rcsf_ex2_ab_or_wo_q':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'sentence: %s, or unknown. answer: like %s or %s, the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'wo_q_wo_or':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'sentence: %s. answer: like %s or %s, the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'ablation':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'sentence: %s. answer: %s, %s, %s, %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'ablation2':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'sentence: %s. answer: like %s or %s, the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'ablation3':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'sentence: %s. answer: %s, %s, the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'ablation4':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'sentence: %s. answer: %s, %s, the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'wo_q_wo_or_wo_ex':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'sentence: %s. answer: the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'wo_q_wo_or_plain':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'sentence: %s. answer: like %s or %s, the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'wo_q_wo_or_plain2':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'sentence: %s. answer: like %s or %s, the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        

        elif schema == 'wo_q_wo_or2':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'sentence: %s. answer: like %s or %s, the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'sepsep':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            self.template = bos + ' %s ' + sep + sep + ' %s like %s and %s, the %s is %s. ' + sep
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_rcsf_ex2_ab_num':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'question: %s there are %d slots. sentence: %s. answer: like %s or %s, the %s is %s.'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'arrow1':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            bos = f'{tokenizer.bos_token}'
            sep = f'{tokenizer.sep_token}'
            self.template = bos + ' %s ' + sep + sep + ' %s => the %s is %s. ' + sep + sep + ' %s => the %s is %s. ' + sep
            self.mask_token = f'{tokenizer.mask_token}'

        else:
            raise ValueError('Unsupported schema: %s.' % schema)
        self.schema = schema

    def __call__(self, domain, sentence, slot):
        #if domain == 'atis':
        #    return 'find the %s in sentence: %s.' % (domainslot2desc[domain][slot], sentence)

        if self.schema == 'slot_desc':
            return self.template % (domainslot2desc[domain][slot], sentence)


        elif self.schema == 't5':
            return self.template % (slot2question_rcsf[slot],
                                    sentence
                                    )

        elif self.schema == 't5_said':
            return (self.template % (slot2question_rcsf[slot],
                                    domainslot2desc[domain][slot],
                                    sentence
                                    ))
        
        elif self.schema == 't5_openai':
            return (self.template % (slot2question_rcsf[slot].lower(),
                                    domainslot2desc[domain][slot],
                                    sentence
                                    ))

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
        
        elif self.schema == 'aisfg':
            return self.template % (domain2desc[domain], domainslot2desc[domain][slot],
                                    domainslot2example[domain][slot], domainslot2context[domain][slot],
                                    sentence)
        
        elif self.schema == 'aisfg_comp':
            return self.template % (
                                    sentence,
                                    domainslot2example[domain][slot], domainslot2context[domain][slot],
                                    domainslot2example[domain][slot], 
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )
        
        elif self.schema == 'min':
            return self.template % (sentence)
        
        elif self.schema == 'notSD':
            return self.template % (domain2desc[domain], 
                                    domainslot2example[domain][slot], domainslot2context[domain][slot],
                                    sentence)
        elif self.schema == 'proposed_query1':
            return self.template % (domain2desc[domain], #domainslot2desc[domain][slot],
                                    domainslot2example[domain][slot], domainslot2context[domain][slot],
                                    domainslot2desc[domain][slot],
                                    sentence)

        elif self.schema == 'proposed_query2':
            #template = domainslot2temp[domain][slot]
            return self.template % (domain2desc[domain], #domainslot2desc[domain][slot],
                                    #domainslot2example[domain][slot], 
                                    domainslot2context[domain][slot],
                                    domainslot2desc[domain][slot],
                                    domainslot2example[domain][slot], 
                                    sentence,
                                    domainslot2desc[domain][slot]
                                    #,sentence
                                    )

        elif self.schema == 'each_slot':
            return self.template % (domainslot2question[domain][slot],
                                    domainslot2context[domain][slot],
                                    (domainslot2temp[domain][slot] % ( '\'' + domainslot2example[domain][slot] + '\'' )),
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )

        elif self.schema == 'each_slot_dummy':
            #print('\ndddd\n')
            return self.template % (domainslot2question[domain][slot],
                                    domainslot2context[domain][slot],
                                    (domainslot2temp[domain][slot] % (domainslot2example[domain][slot])),
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token)),
                                    domainslot2dummy[domain][slot]
                                    )
        elif self.schema == 'something':
            #print("\naaaaa\n")
            return self.template % (domain2desc[domain], domainslot2desc[domain][slot],
                                    domainslot2example[domain][slot], domainslot2context[domain][slot],
                                    sentence,
                                    domainslot2desc[domain][slot], domainslot2dummy2[domain][slot])

        elif self.schema == "example_rcsf":
            return self.template % (domainslot2question[domain][slot],
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token)),
                                    domainslot2dummy[domain][slot]
                                    )
        
        elif self.schema == "example_rcsf2":
            return self.template % (domainslot2question[domain][slot],                    
                                    (domainslot2temp[domain][slot] % (slot2example_rcsf[slot][0])),
                                    (domainslot2temp[domain][slot] % (slot2example_rcsf[slot][1])),
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token)),
                                    domainslot2dummy[domain][slot]
                                    )
        elif self.schema == "example_rcsf3":
            return self.template % (domainslot2question[domain][slot],
                                    domainslot2desc[domain][slot],                    
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token)),
                                    domainslot2dummy[domain][slot]
                                    )
        
        elif self.schema == "without_example":
            return self.template % (domainslot2question[domain][slot],
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token)),
                                    domainslot2dummy[domain][slot]
                                    )
        
        elif self.schema == "unk_wo":
            return self.template % (domainslot2question[domain][slot],
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )

        elif self.schema == "dummy_unk":
            return self.template % (domainslot2question[domain][slot],
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )
        elif self.schema == "dummy_unk_ab":
            return self.template % (domainslot2question[domain][slot],
                                    sentence,
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )
        
        elif self.schema == "dummy_unk2":
            return self.template % (domainslot2question[domain][slot],
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )
        elif self.schema == "nosep":
            return self.template % (domainslot2question[domain][slot],
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )
        elif self.schema == "nosep_ab":
            return self.template % (domainslot2question[domain][slot],
                                    sentence,
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )
        elif self.schema == "nosep_or":
            return self.template % (domainslot2question[domain][slot],
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )
        
        elif self.schema == "nosep_rcsf":
            return self.template % (slot2question_rcsf[slot],
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )
        elif self.schema == "nosep_qa":
            return self.template % (slot2question_qa[slot],
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )
        elif self.schema == "nosep_rcsf_ab":
            return self.template % (slot2question_rcsf[slot],
                                    sentence,
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )

        elif self.schema == "nosep_rcsf_or":
            return self.template % (slot2question_rcsf[slot],
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )
        
        elif self.schema == "nosep_rcsf_ex2":
            return self.template % (slot2question_rcsf[slot],
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )

        elif self.schema == "nosep_rcsf_ex2_long":
            return self.template % (slot2question_rcsf[slot],
                                    sentence,
                                    (domainslot2temp[domain][slot] % slot2example_rcsf[slot][0]),
                                    (domainslot2temp[domain][slot] % slot2example_rcsf[slot][1]),
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )
        elif self.schema == "nosep_rcsf_ex2_long_ab":
            return self.template % (slot2question_rcsf[slot],
                                    sentence,
                                    domainslot2desc[domain][slot],
                                    slot2example_rcsf[slot][0],
                                    domainslot2desc[domain][slot],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )
        elif self.schema == "nosep_rcsf_ex2_slots":
            negative_slots = []
            for sl in domain2slots[domain]:
                if sl != slot:
                    negative_slots.append(domainslot2desc[domain][sl])
            return self.template % (slot2question_rcsf[slot],
                                    domainslot2desc[domain][slot],
                                    ', '.join(negative_slots),
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )
        elif self.schema == "nosep_rcsf_ex2_upper":
            return self.template % (slot2question_rcsf[slot].capitalize(),
                                    sentence.capitalize(),
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )
        
        elif self.schema == "nosep_rcsf_ex2_negex":
            neg_ex = []
            for sl in domain2slots[domain]:
                if sl != slot:
                    neg_ex.append(slot2example_rcsf[sl][0])
                    neg_ex.append(slot2example_rcsf[sl][1])
            return self.template % (slot2question_rcsf[slot],
                                    ', '.join(neg_ex),
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )
        
        elif self.schema == "nosep_rcsf_ex2_ab":
            return self.template % (slot2question_rcsf[slot],
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )
        
        elif self.schema == "nosep_rcsf_ex2_ab_or":
            return self.template % (slot2question_rcsf[slot],
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )

        elif self.schema == "nosep_rcsf_ex2_ab_or_wo_q":
            return self.template % (
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )

        elif self.schema == "wo_q_wo_or":
            return self.template % (
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )
        elif self.schema == "ablation":
            return self.template % (
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )
        
        elif self.schema == "ablation2":
            return self.template % (
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )
        
        elif self.schema == "ablation3":
            return self.template % (
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )
        
        elif self.schema == "ablation4":
            return self.template % (
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )
        
        elif self.schema == "wo_q_wo_or_wo_ex":
            return self.template % (
                                    sentence,
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )
        
        elif self.schema == "wo_q_wo_or_plain":
            return self.template % (
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )
        elif self.schema == "wo_q_wo_or_plain2":
            return self.template % (
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )

        elif self.schema == "wo_q_wo_or2":
            return self.template % (
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc2[domain][slot],
                                    self.mask_token
                                    )

        elif self.schema == "sepsep":
            return self.template % (sentence,
                                    slot2question_rcsf[slot],
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )
        elif self.schema == "nosep_rcsf_ex2_ab_num":
            return self.template % (slot2question_rcsf[slot],
                                    domain2slotsnum[domain],
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )

        elif self.schema == "arrow1":
            return self.template % (slot2question_rcsf[slot],
                                    domainslot2context[domain][slot],
                                    domainslot2desc[domain][slot],
                                    domainslot2example[domain][slot],
                                    sentence,
                                    domainslot2desc[domain][slot],
                                    self.mask_token
                                    )

        else:
            return ValueError('Unknown Error!')


class ResponseTemplate:
    def __init__(self, schema):
        if schema == 'plain':
            self.template = '%s.'
        
        elif schema == 'aisfg':
            self.template = '%s.'
        
        elif schema == 'aisfg_comp':
            self.template = 'like %s, the %s is %s.'

        elif schema == 't5_plain':
            self.template = '%s'

        elif schema == 't5_said_plain':
            self.template = '%s'
        
        elif schema == 't5_said_the_is':
            self.template = 'The %s is %s'
        
        elif schema == 't5_openai_plain':
            self.template = '%s'
        
        elif schema == 't5_openai_the_is':
            self.template = 'the %s is %s'

        elif schema == 'proposed':
            self.template = '%s is %s.'
        elif schema == 'proposed2':
            self.template = 'the %s is %s.'
        
        elif schema == 'plain_not_found':
            self.template = '%s.'

        elif schema == 'proposed_query2_resp':
            #model_name = 'facebook/bart-base'
            #tokenizer = BartTokenizer.from_pretrained(model_name)
            #self.template = 'when he wants to %s, like %s in %s. in sentence %s. the %s is %s.'
            #self.template_not_found = 'when he wants to %s, like %s in %s, in sentence %s. the %s is ' + f'{tokenizer.mask_token}' + '.'
            self.template = 'the %s is %s.'
            self.template_not_found = 'the %s is.'
        
        elif schema == 'each_slot':
            pass
        elif schema == 'each_slot_dummy':
            pass

        elif schema == 'unk':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.unk_token = f'{tokenizer.unk_token}'
        
        elif schema == 'something':
            self.template = 'the %s is %s.'
        
        elif schema == 'dummy_unk':
            pass
        
        elif schema == 'dummy_unk_ab':
            self.template = 'the %s is %s.'
        
        elif schema == 'nosep' or schema == 'nosep_or' or schema == 'nosep_rcsf' or schema == 'nosep_qa' or schema == 'nosep_rcsf_or':
            pass
    
        elif schema == 'nosep_ab':
            self.template = 'the %s is %s.'
        
        elif schema == 'nosep_plain':
            self.template = '%s.'
        
        elif schema == 'nosep_rcsf_plain':
            self.template = '%s.'
        elif schema == 'nosep_qa_plain':
            self.template = '%s.'

        elif schema == 'nosep_rcsf_ab':
            self.template = 'the %s is %s.'
        
        elif schema == 'nosep_rcsf_ex2':
            self.template = 'like %s or %s, %s'
        
        elif schema == 'nosep_rcsf_ex2_long':
            self.template = 'example: %s %s answer: %s'
        
        elif schema == 'nosep_rcsf_ex2_long_ab':
            self.template = 'example: the %s is %s. the %s is %s. answer: the %s is %s.'
        
        elif schema == 'nosep_rcsf_ex2_upper':
            self.template = 'Like %s or %s, %s'
        
        elif schema == 'nosep_rcsf_ex2_mlm':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'question: %s sentence: %s. answer: like %s or %s, %s'
            self.mask_token = f'{tokenizer.mask_token}'
        
        elif schema == 'nosep_rcsf_ex2_ab':
            self.template = 'like %s or %s, the %s is %s.'
        
        elif schema == 'nosep_rcsf_ex2_ab_or' or schema == 'nosep_rcsf_ex2_ab_or_wo_q' or schema == 'wo_q_wo_or' or schema == 'wo_q_wo_or2':
            self.template = 'like %s or %s, the %s is %s.'
        
        elif schema == 'ablation':
            self.template = '%s, %s, %s, %s.'
        elif schema == 'ablation2':
            self.template = '%s, %s, %s, %s.'
        
        elif schema == 'ablation3':
            self.template = '%s, %s, the %s is %s.'
        
        elif schema == 'ablation4':
            self.template = '%s, %s, %s, %s.'
        
        elif schema == 'wo_q_wo_or_plain':
            self.template = '%s.'
        
        elif schema == 'wo_q_wo_or_plain2':
            self.template = 'the %s is %s.'
        
        elif schema == 'wo_q_wo_or_wo_ex':
            self.template = 'the %s is %s.'
        
        elif schema == 'sepsep':
            self.template = '%s like %s and %s, the %s is %s.'
        
        elif schema == 'arrow1':
            self.template = 'the %s is %s.'
        
        elif schema == 'arrow1_1':
            self.template = '%s => the %s is %s.'
        

        else:
            raise ValueError('Unsupported schema: %s.' % schema)
        self.schema = schema

    def __call__(self, domain, sentence, slot, entity):
        if self.schema == 'plain':
            return self.template % (', '.join(entity))
        
        elif self.schema == 'aisfg':
            return self.template % (', '.join(entity))
        
        elif self.schema == 'aisfg_comp':
            if entity[0] == "":
                return self.template % (
                                        domainslot2example[domain][slot],
                                        domainslot2desc[domain][slot],
                                        'unknown'
                                        )
            
            return self.template % (
                                    domainslot2example[domain][slot],
                                    domainslot2desc[domain][slot],
                                    (', '.join(entity))
                                    )


        elif self.schema == 't5_plain':
            if entity[0] == '':
                return self.template % ('unknown')
            return self.template % (', '.join(entity))
        
        elif self.schema == 't5_said_plain':
            if entity[0] == '':
                return self.template % ('unknown')
            return self.template % (', '.join(entity))
        
        elif self.schema == 't5_said_the_is':
            if entity[0] == '':
                return (self.template % (domainslot2desc[domain][slot], 'unknown'))
            return (self.template % (domainslot2desc[domain][slot], ', '.join(entity)))

        elif self.schema == 't5_openai_plain':
            if entity[0] == '':
                return self.template % ('unknown')
            return self.template % (', '.join(entity))
        
        elif self.schema == 't5_openai_the_is':
            if entity[0] == '':
                return (self.template % (domainslot2desc[domain][slot], 'unknown'))
            return (self.template % (domainslot2desc[domain][slot], ', '.join(entity)))



        elif self.schema == 'proposed':
            return self.template % (domainslot2desc[domain][slot], ', '.join(entity))
        elif self.schema == 'proposed2':
            if (entity[0] == ""):
                return 'the ' +  domainslot2desc[domain][slot] + ' is not found.'
            return self.template % (domainslot2desc[domain][slot], ', '.join(entity))


        elif self.schema == 'plain_not_found':
            if entity[0] == '':
                return 'not found.'
            else:
                return self.template % (', '.join(entity))

        elif self.schema == 'proposed_query2_resp':
            if (entity[0] == ""):
                return self.template_not_found % (
                                    #sentence,
                                    domainslot2desc[domain][slot]
                                    #,sentence
                                    )
            else:
                return self.template % (
                                    #sentence,
                                    domainslot2desc[domain][slot],
                                    ', '.join(entity)
                                    #,sentence
                                    )
        

        elif self.schema == 'each_slot':
            if entity[0] == "":
                return domainslot2temp[domain][slot] % ( '\'' + domainslot2example[domain][slot]  + '\'')
            
            _entity = []
            for ent in entity:
                _entity.append('\'' + ent + '\'')
            return domainslot2temp[domain][slot] % (', '.join(_entity))
        
        elif self.schema == 'each_slot_dummy':
            if entity[0] == "":
                return domainslot2temp[domain][slot] % (domainslot2dummy[domain][slot])
            
            return domainslot2temp[domain][slot] % (', '.join(entity))
        
        elif self.schema == 'unk':
            if entity[0] == "":
                return domainslot2temp[domain][slot] % (self.unk_token)
            
            return domainslot2temp[domain][slot] % (', '.join(entity))
        
        elif self.schema == 'something':
            if entity[0] == '':
                return self.template % (domainslot2desc[domain][slot], domainslot2dummy2[domain][slot])
            return self.template % (domainslot2desc[domain][slot], ', '.join(entity))
        
        elif self.schema == 'dummy_unk':
            if entity[0] == "":
                return domainslot2temp[domain][slot] % ('unknown')
            
            return domainslot2temp[domain][slot] % (', '.join(entity))
        
        elif self.schema == 'dummy_unk_ab':
            if entity[0] == '':
                return self.template % (domainslot2desc[domain][slot], 'unknown')
            return self.template % (domainslot2desc[domain][slot], ', '.join(entity))
        
        elif self.schema == 'nosep' or self.schema == 'nosep_or' or self.schema == 'nosep_rcsf' or self.schema == 'nosep_qa' or self.schema == 'nosep_rcsf_or' :
            if entity[0] == "":
                return domainslot2temp[domain][slot] % ('unknown')
            
            return domainslot2temp[domain][slot] % (', '.join(entity))

        elif self.schema == 'nosep_ab':
            if entity[0] == '':
                return self.template % (domainslot2desc[domain][slot], 'unknown')
            return self.template % (domainslot2desc[domain][slot], ', '.join(entity))
        
        elif self.schema == 'nosep_plain':
            if entity[0] == '':
                return '.'
            else:
                return self.template % (', '.join(entity))
        
        elif self.schema == 'nosep_rcsf_plain':
            if entity[0] == '':
                return '.'
            else:
                return self.template % (', '.join(entity))
            
        elif self.schema == 'nosep_qa_plain':
            if entity[0] == '':
                return '.'
            else:
                return self.template % (', '.join(entity))
        
        elif self.schema == 'nosep_rcsf_ab':
            if entity[0] == '':
                return self.template % (domainslot2desc[domain][slot], 'unknown')
            return self.template % (domainslot2desc[domain][slot], ', '.join(entity))
        
        elif self.schema == 'nosep_rcsf_ex2':
            if entity[0] == "":
                return self.template % (
                                        slot2example_rcsf[slot][0],
                                        slot2example_rcsf[slot][1],
                                        domainslot2temp[domain][slot] % ('unknown')
                                        )
            
            return self.template % (
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2temp[domain][slot] % (', '.join(entity))
                                    )
        elif self.schema == 'nosep_rcsf_ex2_long':
            if entity[0] == "":
                return self.template % (
                                        (domainslot2temp[domain][slot] % slot2example_rcsf[slot][0]),
                                        (domainslot2temp[domain][slot] % slot2example_rcsf[slot][1]),
                                        (domainslot2temp[domain][slot] % ('unknown'))
                                        )
            
            return self.template % (
                                    (domainslot2temp[domain][slot] % slot2example_rcsf[slot][0]),
                                    (domainslot2temp[domain][slot] % slot2example_rcsf[slot][1]),
                                    (domainslot2temp[domain][slot] % (', '.join(entity)))
                                    )
        
        elif self.schema == 'nosep_rcsf_ex2_long_ab':
            if entity[0] == "":
                return self.template % (
                                    domainslot2desc[domain][slot],
                                    slot2example_rcsf[slot][0],
                                    domainslot2desc[domain][slot],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    'unknown'
                                    )
            
            return self.template % (
                                    domainslot2desc[domain][slot],
                                    slot2example_rcsf[slot][0],
                                    domainslot2desc[domain][slot],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    ', '.join(entity)
                                    )
        
        elif self.schema == 'nosep_rcsf_ex2_upper':
            if entity[0] == "":
                return self.template % (
                                        slot2example_rcsf[slot][0],
                                        slot2example_rcsf[slot][1],
                                        domainslot2temp[domain][slot] % ('unknown')
                                        )
            
            return self.template % (
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2temp[domain][slot] % (', '.join(entity))
                                    )
        
        elif self.schema == "nosep_rcsf_ex2_mlm":
            if entity[0] == "":
                return self.template % (slot2question_rcsf[slot],
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    (domainslot2temp[domain][slot] % ('unknown'))
                                    )
            return self.template % (slot2question_rcsf[slot],
                                    sentence,
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    (domainslot2temp[domain][slot] % (', '.join(entity)))
                                    )
        
        elif self.schema == 'nosep_rcsf_ex2_ab':
            if entity[0] == "":
                return self.template % (
                                        slot2example_rcsf[slot][0],
                                        slot2example_rcsf[slot][1],
                                        domainslot2desc[domain][slot],
                                        'unknown'
                                        )
            
            return self.template % (
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    (', '.join(entity))
                                    )
        
        elif self.schema == 'nosep_rcsf_ex2_ab_or' or self.schema == 'nosep_rcsf_ex2_ab_or_wo_q' or self.schema == 'wo_q_wo_or':
            if entity[0] == "":
                return self.template % (
                                        slot2example_rcsf[slot][0],
                                        slot2example_rcsf[slot][1],
                                        domainslot2desc[domain][slot],
                                        'unknown'
                                        )
            
            return self.template % (
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    (', '.join(entity))
                                    )
        elif self.schema == 'ablation':
            if entity[0] == "":
                return self.template % (
                                        slot2example_rcsf[slot][0],
                                        slot2example_rcsf[slot][1],
                                        domainslot2desc[domain][slot],
                                        'unknown'
                                        )
            
            return self.template % (
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    (', '.join(entity))
                                    )
        
        elif self.schema == 'ablation2':
            if entity[0] == "":
                return self.template % (
                                        slot2example_rcsf[slot][0],
                                        slot2example_rcsf[slot][1],
                                        domainslot2desc[domain][slot],
                                        'unknown'
                                        )
            
            return self.template % (
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    (', '.join(entity))
                                    )
        
        elif self.schema == 'ablation3':
            if entity[0] == "":
                return self.template % (
                                        slot2example_rcsf[slot][0],
                                        slot2example_rcsf[slot][1],
                                        domainslot2desc[domain][slot],
                                        'unknown'
                                        )
            
            return self.template % (
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    (', '.join(entity))
                                    )
                                
        elif self.schema == 'ablation4':
            if entity[0] == "":
                return self.template % (
                                        slot2example_rcsf[slot][0],
                                        slot2example_rcsf[slot][1],
                                        domainslot2desc[domain][slot],
                                        'unknown'
                                        )
            
            return self.template % (
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    (', '.join(entity))
                                    )
        

        elif self.schema == 'wo_q_wo_or_wo_ex':
            if entity[0] == "":
                return self.template % (
                                       
                                        domainslot2desc[domain][slot],
                                        'unknown'
                                        )
            
            return self.template % (
                                    
                                    domainslot2desc[domain][slot],
                                    (', '.join(entity))
                                    )
        
        elif self.schema == 'wo_q_wo_or_plain':
            if entity[0] == "":
                return self.template % (
                                        'unknown'
                                        )
            
            return self.template % (
                                    (', '.join(entity))
                                    )
        
        elif self.schema == 'wo_q_wo_or_plain2':
            if entity[0] == "":
                return self.template % (
                                       
                                        domainslot2desc[domain][slot],
                                        'unknown'
                                        )
            
            return self.template % (
                                    
                                    domainslot2desc[domain][slot],
                                    (', '.join(entity))
                                    )


        elif self.schema == 'wo_q_wo_or2':
            if entity[0] == "":
                return self.template % (
                                        slot2example_rcsf[slot][0],
                                        slot2example_rcsf[slot][1],
                                        domainslot2desc2[domain][slot],
                                        'unknown'
                                        )
            
            return self.template % (
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc2[domain][slot],
                                    (', '.join(entity))
                                    )
        
        elif self.schema == 'sepsep':
            if entity[0] == "":
                return self.template % (
                                        slot2question_rcsf[slot],
                                        slot2example_rcsf[slot][0],
                                        slot2example_rcsf[slot][1],
                                        domainslot2desc[domain][slot],
                                        'unknown'
                                        )
            
            return self.template % (
                                    slot2question_rcsf[slot],
                                    slot2example_rcsf[slot][0],
                                    slot2example_rcsf[slot][1],
                                    domainslot2desc[domain][slot],
                                    (', '.join(entity))
                                    )
        
        elif self.schema == 'arrow1':
            if entity[0] == '':
                return self.template % (domainslot2desc[domain][slot], 'unknown')
            return self.template % (domainslot2desc[domain][slot], ', '.join(entity))
        
        elif self.schema == 'arrow1_1':
            if entity[0] == '':
                return self.template % (sentence, domainslot2desc[domain][slot], 'unknown')
            return self.template % (sentence, domainslot2desc[domain][slot], ', '.join(entity))

        else:
            raise ValueError('Unknown Error!')

class DecoderInput:
    def __init__(self, decode_input, schema):
        if schema == 'plain':
            self.template = ''
        elif schema == 'proposed':
            self.template = '%s is'
        elif schema == 'proposed2':
            self.template = 'the %s is'
        else:
            raise ValueError('Unsupported schema: %s.' % schema)
        self.schema = schema
        self.decoder_input = decode_input
    
    def __call__(self, domain, sentence, slot, entity):

        if self.decoder_input == False:
            return ''
        elif self.schema == 'plain':
            return self.template
        elif self.schema == 'proposed':
            return self.template % (domainslot2desc[domain][slot])
        elif self.schema == 'proposed2':
            return self.template % (domainslot2desc[domain][slot])
        else:
            raise ValueError('Unknown Error!')
