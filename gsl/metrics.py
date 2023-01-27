import torch
from transformers import BartForConditionalGeneration, BartTokenizer
from .datasets.utils import domainslot2before, domainslot2after, domainslot2example, domainslot2question, domain2slots, domainslot2dummy2, domainslot2desc, slot2question_rcsf, slot2question_qa, domainslot2desc2


def parse_plain(sentence):
    """
    Args:
        sentence: single sentence string

    Returns:
        Entities set
    """

    if sentence == ".":
        return set([])


    entities = sentence.strip().strip('.').split(',')
    entities_list = []
    for entity in entities:
        entities_list.append(entity.strip())
    return set(entities_list)


def parse_plain2(sentence, domain, query):
    """
    Args:
        sentence: single sentence string

    Returns:
        Entities set
    """

    idx = query.find("find the ")
    que = query[(idx + 9):]
    slot = "nnn"
    for sl in domain2slots[domain]:
        if que.startswith(domainslot2desc[domain][sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")



    if sentence == ".":
        return set([]), slot


    entities = sentence.strip().strip('.').split(',')
    entities_list = []
    for entity in entities:
        entities_list.append(entity.strip())
    return set(entities_list), slot

def parse_proposed(sentence, domain, query):
    """
    Args:
        sentence: single sentence string

    Returns:
        Entities set
    """
    idx = sentence.find(' is ')
    if (idx == -1):
        #return set([])
        pass

    if ("not found" in sentence):
        return set([])

    substring = sentence[(idx + 4):]
    entities = substring.strip().strip('.').split(',')
    entities_list = []
    for entity in entities:
        entities_list.append(entity.strip())
    return set(entities_list)


def parse_proposed_query2(sentence):

    #model_name = 'facebook/bart-base'
    #tokenizer = BartTokenizer.from_pretrained(model_name)

    if ' is.' in sentence:
        return set([])
    elif ' are.' in sentence:
        return set([])

    idx = sentence.rfind(' is ')
    idx_are = sentence.rfind(' are ')
    if idx_are != -1:
        if idx_are > idx:
            idx = idx_are + 1


    substring = sentence[(idx + 4):]

    #if f'{tokenizer.mask_token}' in substring:
    #    return set([])

    entities = substring.strip().strip('.').split(',')
    entities_list = []
    for entity in entities:
        entities_list.append(entity.strip())
    return set(entities_list)


def parse_each_slot(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("<s> " + domainslot2question[domain][sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")

    idx_before = sentence.find(domainslot2before[domain][slot])
    length = len(domainslot2before[domain][slot])
    idx_after = sentence.rfind(domainslot2after[domain][slot])

    if idx_before == -1 or idx_after == -1:
        return set([]), slot

    substring = sentence[(idx_before + length):idx_after]

    idx_sent = query.rfind("sentence")
    sent = query[idx_sent:]

    if ('\'' in substring):
        print('find \'')
    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_each_slot_dummy(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("<s> " + domainslot2question[domain][sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")

    idx_before = sentence.find(domainslot2before[domain][slot])
    length = len(domainslot2before[domain][slot])
    idx_after = sentence.rfind(domainslot2after[domain][slot])

    if idx_before == -1 or idx_after == -1:
        return set([]), slot

    substring = sentence[(idx_before + length):idx_after]

    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("answer")
    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_plain_not_found(sentence, domain, query):


    slot = "nnn"
    idx_sl = query.find("find")
    que = query[(idx_sl + 9):]
    for sl in domain2slots[domain]:
        if que.startswith(domainslot2desc[domain][sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")

    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("not found")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = sentence.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot



def parse_something(sentence, domain, query):

    slot = "nnn"
    idx_sl = query.find("find")
    que = query[(idx_sl + 9):]
    for sl in domain2slots[domain]:
        if que.startswith(domainslot2desc[domain][sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")


    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind(domainslot2dummy2[domain][slot])
    sent = query[idx_sent:idx_ans]

    idx = sentence.find(" is ")
    if idx == -1:
        print(" is not found")
        return set([]), slot

    substring = sentence[(idx + 4):]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_plain_dummy(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("<s> " + domainslot2question[domain][sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")

    if sentence == ".":
        return set([]), slot


    entities = sentence.strip().strip('.').split(',')
    entities_list = []
    for entity in entities:
        entities_list.append(entity.strip())
    return set(entities_list), slot

def parse_unk_ab(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("<s> " + domainslot2question[domain][sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx = sentence.find(" is ")
    if idx == -1:
        print(" is not found")
        return set([]), slot
    substring = sentence[(idx + 4):]

    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("answer")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_nosep(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + domainslot2question[domain][sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")

    idx_before = sentence.find(domainslot2before[domain][slot])
    length = len(domainslot2before[domain][slot])
    idx_after = sentence.rfind(domainslot2after[domain][slot])

    if idx_before == -1 or idx_after == -1:
        return set([]), slot

    substring = sentence[(idx_before + length):idx_after]

    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("answer")
    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_nosep_ab(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + domainslot2question[domain][sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx = sentence.find(" is ")
    if idx == -1:
        print(" is not found")
        return set([]), slot
    substring = sentence[(idx + 4):]

    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("answer")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_nosep_or(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + domainslot2question[domain][sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")

    idx_before = sentence.find(domainslot2before[domain][slot])
    length = len(domainslot2before[domain][slot])
    idx_after = sentence.rfind(domainslot2after[domain][slot])

    if idx_before == -1 or idx_after == -1:
        return set([]), slot

    substring = sentence[(idx_before + length):idx_after]

    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("or unknown")
    sent = query[idx_sent:idx_ans]

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("ororororor")

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_nosep_plain(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + domainslot2question[domain][sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")


    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("answer")
    sent = query[idx_sent:idx_ans]

    if sentence == '.':
        return set([]), slot

    entities = sentence.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_nosep_rcsf(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + slot2question_rcsf[sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")

    idx_before = sentence.rfind(domainslot2before[domain][slot])
    length = len(domainslot2before[domain][slot])
    idx_after = sentence.rfind(domainslot2after[domain][slot])

    if idx_before == -1 or idx_after == -1:
        return set([]), slot

    substring = sentence[(idx_before + length):idx_after]

    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("answer")
    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot




def parse_nosep_rcsf_upper(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("Question: " + slot2question_rcsf[sl].capitalize()):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")

    idx_before = sentence.find(domainslot2before[domain][slot])
    length = len(domainslot2before[domain][slot])
    idx_after = sentence.rfind(domainslot2after[domain][slot])

    if idx_before == -1 or idx_after == -1:
        return set([]), slot

    substring = sentence[(idx_before + length):idx_after]

    idx_sent = query.rfind("Sentence")
    idx_ans = query.rfind("Answer")
    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot




def parse_nosep_qa(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + slot2question_qa[sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")

    idx_before = sentence.find(domainslot2before[domain][slot])
    length = len(domainslot2before[domain][slot])
    idx_after = sentence.rfind(domainslot2after[domain][slot])

    if idx_before == -1 or idx_after == -1:
        return set([]), slot

    substring = sentence[(idx_before + length):idx_after]

    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("answer")
    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_nosep_rcsf_plain(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + slot2question_rcsf[sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")


    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("answer")
    sent = query[idx_sent:idx_ans]

    if sentence == '.':
        return set([]), slot

    entities = sentence.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_nosep_qa_plain(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + slot2question_qa[sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")


    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("answer")
    sent = query[idx_sent:idx_ans]

    if sentence == '.':
        return set([]), slot

    entities = sentence.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot



def parse_nosep_rcsf_ab(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + slot2question_rcsf[sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx = sentence.find(" is ")
    if idx == -1:
        print(" is not found")
        return set([]), slot
    substring = sentence[(idx + 4):]

    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("answer")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_nosep_rcsf_ab_or(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + slot2question_rcsf[sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx = sentence.find(" is ")
    if idx == -1:
        print(" is not found")
        return set([]), slot
    substring = sentence[(idx + 4):]

    idx_sent = query.find("sentence")
    idx_ans = query.find(", or unknown")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_nosep_rcsf_ab_or_wo_q(sentence, domain, query):

    slot = "nnn"
    idx_0 = query.find('answer')
    if idx_0 == 0:
        raise ValueError("nnn nnn")
    idx_1 = query[idx_0:].rfind(', the')
    if idx_1 == 0:
        raise ValueError("nnn nnn")

    for sl in domain2slots[domain]:
        if query[(idx_0 + idx_1 + 6):].startswith(domainslot2desc[domain][sl]  + ' is '):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx = sentence.find(" is ")
    if idx == -1:
        print(" is not found")
        return set([]), slot
    substring = sentence[(idx + 4):]

    idx_sent = query.find("sentence")
    idx_ans = query.find(", or unknown")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_wo_q_wo_or(sentence, domain, query):

    slot = "nnn"
    idx_0 = query.find('answer')
    if idx_0 == 0:
        raise ValueError("nnn nnn")
    idx_1 = query[idx_0:].rfind(', the')
    if idx_1 == 0:
        raise ValueError("nnn nnn")

    for sl in domain2slots[domain]:
        if query[(idx_0 + idx_1 + 6):].startswith(domainslot2desc[domain][sl]  + ' is '):
            slot = sl
            break
    if slot == "nnn":
        print(query)
        raise ValueError("nnn nnn")
    
    idx = sentence.find(" is ")
    if idx == -1:
        print(" is not found")
        return set([]), slot
    substring = sentence[(idx + 4):]

    idx_sent = query.find("sentence")
    idx_ans = query.find(" answer:")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_ablation(sentence, domain, query):

    slot = "nnn"
    #print(query)
    idx_0 = query.find('answer')
    if idx_0 == 0:
        raise ValueError("nnn nnn")
    #print(query[idx_0:])
    idx_1 = query[idx_0:].find(',')
    if idx_1 == 0:
        raise ValueError("nnn nnn")
    #print(query[(idx_0 + idx_1 + 1):])
    idx_2 = query[(idx_0 + idx_1 + 1):].find(',')
    if idx_2 == 0:
        raise ValueError("nnn nnn")

    for sl in domain2slots[domain]:
        if query[(idx_0 + idx_1 + 1 + idx_2 + 2):].startswith(domainslot2desc[domain][sl]  + ','):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx = sentence.find(',')
    if idx == -1:
        print(" , not found")
        return set([]), slot
    idx = sentence.find(',', idx + 1)
    if idx == -1:
        print(" , not found")
        return set([]), slot
    idx = sentence.find(',', idx + 1)
    if idx == -1:
        print(" , not found")
        return set([]), slot



    substring = sentence[(idx + 2):]

    idx_sent = query.find("sentence")
    idx_ans = query.find(" answer:")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_ablation2(sentence, domain, query):

    slot = "nnn"
    idx_0 = query.find('answer')
    if idx_0 == 0:
        raise ValueError("nnn nnn")
    idx_1 = query[idx_0:].rfind(', the')
    if idx_1 == 0:
        raise ValueError("nnn nnn")

    for sl in domain2slots[domain]:
        if query[(idx_0 + idx_1 + 6):].startswith(domainslot2desc[domain][sl]  + ' is '):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx = sentence.find(',')
    if idx == -1:
        print(" , not found")
        return set([]), slot
    idx = sentence.find(',', idx + 1)
    if idx == -1:
        print(" , not found")
        return set([]), slot
    idx = sentence.find(',', idx + 1)
    if idx == -1:
        print(" , not found")
        return set([]), slot



    substring = sentence[(idx + 2):]

    idx_sent = query.find("sentence")
    idx_ans = query.find(" answer:")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_ablation4(sentence, domain, query):

    slot = "nnn"
    idx_0 = query.find('answer')
    if idx_0 == 0:
        raise ValueError("nnn nnn")
    idx_1 = query[idx_0:].rfind(', the')
    if idx_1 == 0:
        raise ValueError("nnn nnn")

    for sl in domain2slots[domain]:
        if query[(idx_0 + idx_1 + 6):].startswith(domainslot2desc[domain][sl]  + ' is '):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx = sentence.find(',')
    if idx == -1:
        print(" , not found")
        return set([]), slot
    idx = sentence.find(',', idx + 1)
    if idx == -1:
        print(" , not found")
        return set([]), slot
    idx = sentence.find(',', idx + 1)
    if idx == -1:
        print(" , not found")
        return set([]), slot



    substring = sentence[(idx + 2):]

    idx_sent = query.find("sentence")
    idx_ans = query.find(" answer:")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot



def parse_aisfg_comp(sentence, domain, query):

    slot = "nnn"
    idx_0 = query.find('answer')
    if idx_0 == 0:
        raise ValueError("nnn nnn")
    idx_1 = query[idx_0:].rfind(', the')
    if idx_1 == 0:
        raise ValueError("nnn nnn")

    for sl in domain2slots[domain]:
        if query[(idx_0 + idx_1 + 6):].startswith(domainslot2desc[domain][sl]  + ' is '):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx = sentence.find(" is ")
    if idx == -1:
        print(" is not found")
        return set([]), slot
    substring = sentence[(idx + 4):]

    idx_sent = query.find("sentence")
    idx_ans = query.find(" example:")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_wo_q_wo_or_wo_ex(sentence, domain, query):

    slot = "nnn"
    idx_0 = query.find('answer: the ')
    if idx_0 == 0:
        raise ValueError("nnn nnn")

    for sl in domain2slots[domain]:
        if query[(idx_0 + 12):].startswith(domainslot2desc[domain][sl]  + ' is '):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx = sentence.find(" is ")
    if idx == -1:
        print(" is not found")
        return set([]), slot
    substring = sentence[(idx + 4):]

    idx_sent = query.find("sentence")
    idx_ans = query.find(" answer:")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_wo_q_wo_or_plain(sentence, domain, query):

    slot = "nnn"
    idx_0 = query.find('answer')
    if idx_0 == 0:
        raise ValueError("nnn nnn")
    idx_1 = query[idx_0:].rfind(', the')
    if idx_1 == 0:
        raise ValueError("nnn nnn")

    for sl in domain2slots[domain]:
        if query[(idx_0 + idx_1 + 6):].startswith(domainslot2desc[domain][sl]  + ' is '):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    

    idx_sent = query.find("sentence")
    idx_ans = query.find(" answer:")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = sentence.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_aisfg(sentence, domain, query):

    slot = "nnn"
    idx_0 = query.find('find the')
    if idx_0 == 0:
        raise ValueError("nnn nnn")

    for sl in domain2slots[domain]:
        if query[(idx_0 + 9):].startswith(domainslot2desc[domain][sl]  + ','):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")

    if sentence == '.':
        return set([]), slot
    

    idx_sent = query.rfind("sentence:")
    idx_ans = query.rfind(".")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = sentence.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_wo_q_wo_or2(sentence, domain, query):

    slot = "nnn"
    idx_0 = query.find('answer')
    if idx_0 == 0:
        raise ValueError("nnn nnn")
    idx_1 = query[idx_0:].rfind(', the')
    if idx_1 == 0:
        raise ValueError("nnn nnn")

    for sl in domain2slots[domain]:
        if query[(idx_0 + idx_1 + 6):].startswith(domainslot2desc2[domain][sl]  + ' is '):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx = sentence.find(" is ")
    if idx == -1:
        print(" is not found")
        return set([]), slot
    substring = sentence[(idx + 4):]

    idx_sent = query.find("sentence")
    idx_ans = query.find(" answer:")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_nosep_rcsf_or(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + slot2question_rcsf[sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")

    idx_before = sentence.find(domainslot2before[domain][slot])
    length = len(domainslot2before[domain][slot])
    idx_after = sentence.rfind(domainslot2after[domain][slot])

    if idx_before == -1 or idx_after == -1:
        return set([]), slot

    substring = sentence[(idx_before + length):idx_after]

    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("or unknown")
    sent = query[idx_sent:idx_ans]

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("ororororor")

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_nosep_rcsf_ex2_long(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + slot2question_rcsf[sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx_tmp = sentence.find('answer')
    if idx_tmp == -1:
        return set([]), slot
    _sentence = sentence[idx_tmp:]
    idx_before = _sentence.find(domainslot2before[domain][slot])
    length = len(domainslot2before[domain][slot])
    idx_after = _sentence.rfind(domainslot2after[domain][slot])

    if idx_before == -1 or idx_after == -1:
        return set([]), slot

    substring = _sentence[(idx_before + length):idx_after]

    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("example")
    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_nosep_rcsf_ex2_long_ab(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + slot2question_rcsf[sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx = sentence.rfind(" is ")
    if idx == -1:
        print(" is not found")
        return set([]), slot
    substring = sentence[(idx + 4):]

    idx_sent = query.rfind("sentence")
    idx_ans = query.rfind("example")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_sepsep(sentence, domain, query):

    slot = "nnn"
    idx1 = query.find('</s>')
    if idx1 == -1:
        print(sentence)
        print(query)
        raise ValueError("nnn nnn")
    
    query_ = query[idx1 + 9:]

    for sl in domain2slots[domain]:
        if query_.startswith(slot2question_rcsf[sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx = sentence.rfind(" is ")
    if idx == -1:
        print(" is not found")
        return set([]), slot
    substring = sentence[(idx + 4):]

    idx_utt_beginning = 3
    idx_utt_end = idx1

    if idx_utt_beginning == -1 or idx_utt_end == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_utt_beginning:idx_utt_end]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_arrow1(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("<s> " + slot2question_rcsf[sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")
    
    idx = sentence.rfind(" is ")
    if idx == -1:
        print(" is not found")
        return set([]), slot
    substring = sentence[(idx + 4):]

    idx_sent = query.rfind("</s></s>")
    idx_ans = query.rfind("=>")

    if idx_sent == -1 or idx_ans == -1:
        raise ValueError("nnn nnn")

    sent = query[idx_sent:idx_ans]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_t5_plain_or_unknown(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + slot2question_rcsf[sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")


    idx_sent = query.rfind("context")
    idx_ans = query.rfind("or unknown")
    sent = query[idx_sent:idx_ans]

    if sentence == '.':
        return set([]), slot

    entities = sentence.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_t5_said_plain(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + slot2question_rcsf[sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")


    idx_sent = query.find("\"")
    idx_ans = query.rfind("\"")
    sent = query[idx_sent:idx_ans]

    if sentence == '.':
        return set([]), slot

    entities = sentence.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_t5_said_the_is(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith("question: " + slot2question_rcsf[sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")


    idx_sent = query.find("\"")
    idx_ans = query.rfind("\"")
    sent = query[idx_sent:idx_ans]

    if sentence == '.':
        return set([]), slot
    
    idx_is = sentence.find(' is ')

    if (idx_is == -1):
        return set([]), slot

    entities = sentence[(idx_is + 4):].strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot

def parse_t5_openai_plain(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith(slot2question_rcsf[sl].lower()):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")


    idx_sent = query.rfind("\n")
    idx_ans = query.rfind(".")
    sent = query[idx_sent:idx_ans]

    if sentence == '.':
        return set([]), slot

    entities = sentence.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def parse_t5_openai_the_is(sentence, domain, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith(slot2question_rcsf[sl].lower()):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")


    idx_sent = query.rfind("\n")
    idx_ans = query.rfind(".")
    sent = query[idx_sent:idx_ans]

    if sentence == '.':
        return set([]), slot
    
    idx_is = sentence.find(' is ')

    if (idx_is == -1):
        return set([]), slot

    entities = sentence[(idx_is + 4):].strip().strip('.').split(',')
    entities_list = []

    for entity in entities:
        entity = entity.strip('\'')
        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([]), slot
    return set(entities_list), slot


def tp_count(query, true_response, pred_response, domain, response_schema='plain'):
    """
    Args:
        query: true_response.shape=[batch_size, 1]
        true_response: true_response.shape=[batch_size, 1]
        pred_response: pred_response.shape=[batch_size, 1]
        response_schema: plain

    Returns:
        tp, num_true, num_pred
    """
    if response_schema == 'plain':
        parse_func = parse_plain_dummy

    
    elif response_schema == 't5_plain':
        parse_func = parse_t5_plain_or_unknown
    
    elif response_schema == 't5_said_plain':
        parse_func = parse_t5_said_plain
    
    elif response_schema == 't5_said_the_is':
        parse_func = parse_t5_said_the_is
    
    elif response_schema == 't5_openai_plain':
        parse_func = parse_t5_openai_plain
    
    elif response_schema == 't5_openai_the_is':
        parse_func = parse_t5_openai_the_is
    
    elif response_schema == 'plain_not_found':
        parse_func = parse_plain_not_found

    elif response_schema == 'proposed':
        parse_func = parse_proposed
    elif response_schema == 'proposed2':
        parse_func = parse_proposed

    elif response_schema == 'proposed_query2_resp':
        parse_func = parse_proposed_query2

    elif response_schema == 'each_slot':
        parse_func = parse_each_slot

    elif response_schema == 'each_slot_dummy':
        parse_func = parse_each_slot_dummy
    
    elif response_schema == 'unk':
        parse_func = parse_each_slot_dummy
    
    elif response_schema == 'dummy_unk':
        parse_func = parse_each_slot_dummy

    elif response_schema == 'something':
        parse_func = parse_something
    
    elif response_schema == 'dummy_unk_ab':
        parse_func = parse_unk_ab
    
    elif response_schema == 'nosep':
        parse_func = parse_nosep

    elif response_schema == 'nosep_ab':
        parse_func = parse_nosep_ab
    
    elif response_schema == 'nosep_or':
        parse_func = parse_nosep_or

    elif response_schema == 'nosep_plain':
        parse_func = parse_nosep_plain

    elif response_schema == 'nosep_rcsf':
        parse_func = parse_nosep_rcsf

    elif response_schema == 'nosep_qa':
        parse_func = parse_nosep_qa
    
    elif response_schema == 'nosep_rcsf_plain':
        parse_func = parse_nosep_rcsf_plain

    elif response_schema == 'nosep_qa_plain':
        parse_func = parse_nosep_qa_plain
    
    elif response_schema == 'nosep_rcsf_ab':
        parse_func = parse_nosep_rcsf_ab

    elif response_schema == 'nosep_rcsf_or':
        parse_func = parse_nosep_rcsf_or
    
    elif response_schema == 'nosep_rcsf_ex2':
        parse_func = parse_nosep_rcsf

    elif response_schema == 'nosep_rcsf_ex2_long':
        parse_func = parse_nosep_rcsf_ex2_long

    elif response_schema == 'nosep_rcsf_ex2_long_ab':
        parse_func = parse_nosep_rcsf_ex2_long_ab
    
    elif response_schema == 'nosep_rcsf_ex2_upper':
        parse_func = parse_nosep_rcsf_upper
    
    elif response_schema == 'nosep_rcsf_ex2_mlm':
        parse_func = parse_nosep_rcsf

    
    elif response_schema == 'nosep_rcsf_ex2_ab':
        parse_func = parse_nosep_rcsf_ab
    
    elif response_schema == 'nosep_rcsf_ex2_ab_or':
        parse_func = parse_nosep_rcsf_ab_or
    
    elif response_schema == 'nosep_rcsf_ex2_ab_or_wo_q':
        parse_func = parse_nosep_rcsf_ab_or_wo_q
    
    elif response_schema == 'wo_q_wo_or':
        parse_func = parse_wo_q_wo_or
    
    elif response_schema == 'wo_q_wo_or_plain2':
        parse_func = parse_wo_q_wo_or
    
    elif response_schema == 'wo_q_wo_or_wo_ex':
        parse_func = parse_wo_q_wo_or_wo_ex
    
    
    elif response_schema == 'wo_q_wo_or_plain':
        parse_func = parse_wo_q_wo_or_plain
    
    elif response_schema == 'wo_q_wo_or2':
        parse_func = parse_wo_q_wo_or2
    
    elif response_schema == 'sepsep':
        parse_func = parse_sepsep
    
    #elif response_schema == 'arrow1':
     #   parse_func = parse_arrow1
    
    elif response_schema == 'arrow1_1':
        parse_func = parse_arrow1
    
    elif response_schema == 'aisfg':
        parse_func = parse_aisfg
    
    elif response_schema == 'aisfg_comp':
        parse_func = parse_aisfg_comp
    
    elif response_schema == 'ablation':
        parse_func = parse_ablation
    
    elif response_schema == 'ablation2':
        parse_func = parse_ablation2

    elif response_schema == 'ablation3':
        parse_func = parse_wo_q_wo_or
    
    elif response_schema == 'ablation4':
        parse_func = parse_ablation4


    else:
        raise ValueError('Unsupported response_schema: %s.' % response_schema)

    tp = num_true = num_pred = 0
    mistake_samples = []
    correct_samples = []
    count_each_slot = {}
    for slot in domain2slots[domain]:
        count_each_slot[slot] = {'tp': 0, 'num_true': 0, 'num_pred': 0}


    for query_, true_sentence, pred_sentence in zip(query, true_response, pred_response):
        true_entities, slot = parse_func(true_sentence, domain, query_)
        pred_entities, slot2 = parse_func(pred_sentence, domain, query_)

        if slot != slot2:
            return ValueError('slot slot2')

        intersection_num = len(true_entities & pred_entities)

        if (intersection_num == 1 and slot == 'playlist_owner'):
        #    print(query_, '\n', true_sentence, '\n', pred_sentence, '\n', true_entities, pred_entities)
            pass

        if intersection_num != len(true_entities) or intersection_num != len(pred_entities):
            mistake_samples.append([query_, true_sentence, pred_sentence, true_entities, pred_entities])
        else:
            correct_samples.append([query_, true_sentence, pred_sentence, true_entities, pred_entities])

        tp += intersection_num
        num_true += len(true_entities)
        num_pred += len(pred_entities)

        count_each_slot[slot]['tp'] += intersection_num
        count_each_slot[slot]['num_true'] += len(true_entities)
        count_each_slot[slot]['num_pred'] += len(pred_entities)

    return tp, num_true, num_pred, mistake_samples, correct_samples, slot, count_each_slot
