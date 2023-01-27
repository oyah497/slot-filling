import torch
from .datasets.utils import domainslot2before, domainslot2after, domainslot2example, domainslot2question, domain2slots


def parse_plain(sentence, domain, slot, query):
    """
    Args:
        sentence: single sentence string

    Returns:
        Entities set
    """

    if sentence == ".":
        return set([])
    if ("not found" in sentence):
        return set([])
    entities = sentence.strip().strip('.').split(',')
    entities_list = []
    for entity in entities:
        entities_list.append(entity.strip())
    return set(entities_list)


def parse_proposed(sentence, domain, slot, query):
    """
    Args:
        sentence: single sentence string

    Returns:
        Entities set
    """
    idx = sentence.find(' is ')
    if (idx == -1):
        #print("is not found")
        pass

    if ("not found" in sentence):
        return set([])
    
    if ("other" in sentence):
        return set([])

    substring = sentence[(idx + 4):]
    entities = substring.strip().strip('.').split(',')
    entities_list = []
    for entity in entities:
        entities_list.append(entity.strip())
    return set(entities_list)


def parse_t5_resp1(sentence, domain, slot, query):
    idx0 = sentence.find("<extra_id_0>") # <extra_id_0>
    idx1 = sentence.find("<extra_id_1>") # <extra_id_1>
    if (idx0 == -1):
        print("<extra_id_0> not found")
    if (idx1 == -1):
        print("<extra_id_1> not found")
    
    substring = sentence[(idx0 + 13):(idx1 - 1)]
    entities = substring.strip().strip('.').split(',')
    entities_list = []
    for entity in entities:
        entities_list.append(entity.strip())
    return set(entities_list)


def parse_each_slot(sentence, domain, slot, query):

    slot = "nnn"
    for sl in domain2slots[domain]:
        if query.startswith(domainslot2question[domain][sl]):
            slot = sl
            break
    if slot == "nnn":
        raise ValueError("nnn nnn")

    idx_before = sentence.find(domainslot2before[domain][slot])
    length = len(domainslot2before[domain][slot])
    idx_after = sentence.rfind(domainslot2after[domain][slot])

    if idx_before == -1 or idx_after == -1:
        return set([])

    substring = sentence[(idx_before + length):idx_after]

    idx_sent = query.rfind("sentence")
    sent = query[idx_sent:]

    entities = substring.strip().strip('.').split(',')
    entities_list = []

    for entity in entities:

        if entity in sent:
            entities_list.append(entity.strip())
        else:
            return set([])
    return set(entities_list)
    






def tp_count(query, true_response, pred_response, slot_list, domain, response_schema='plain'):
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
        parse_func = parse_plain
    elif response_schema == 'proposed':
        parse_func = parse_proposed
    elif response_schema == 'proposed2':
        parse_func = parse_proposed
    elif response_schema == 't5_resp1':
        #parse_func = parse_t5_resp1
        parse_func = parse_plain
    
    elif response_schema == 'each_slot':
        parse_func = parse_each_slot

    else:
        raise ValueError('Unsupported response_schema: %s.' % response_schema)

    tp = num_true = num_pred = 0
    mistake_samples = []
    correct_samples = []

    for query_, true_sentence, pred_sentence, slot in zip(query, true_response, pred_response, slot_list):
        true_entities = parse_func(true_sentence, domain, slot, query_)
        pred_entities = parse_func(pred_sentence, domain, slot, query_)
        intersection_num = len(true_entities & pred_entities)


        if intersection_num != len(true_entities) or intersection_num != len(pred_entities):
            mistake_samples.append([query_, true_sentence, pred_sentence, true_entities, pred_entities])
        else:
            correct_samples.append([query_, true_sentence, pred_sentence, true_entities, pred_entities])

        tp += intersection_num
        num_true += len(true_entities)
        num_pred += len(pred_entities)
    return tp, num_true, num_pred, mistake_samples, correct_samples
