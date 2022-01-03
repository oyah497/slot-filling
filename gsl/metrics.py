import torch


def parse_plain(sentence):
    """
    Args:
        sentence: single sentence string

    Returns:
        Entities set
    """
    entities = sentence.strip().strip('.').split(',')
    entities_list = []
    for entity in entities:
        entities_list.append(entity.strip())
    return set(entities_list)


def tp_count(query, true_response, pred_response, response_schema='plain'):
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
    else:
        raise ValueError('Unsupported response_schema: %s.' % response_schema)

    tp = num_true = num_pred = 0
    mistake_samples = []
    for query_, true_sentence, pred_sentence in zip(query, true_response, pred_response):
        true_entities = parse_func(true_sentence)
        pred_entities = parse_func(pred_sentence)
        intersection_num = len(true_entities & pred_entities)
        if intersection_num != len(true_entities):
            mistake_samples.append([query_, true_sentence, pred_sentence])

        tp += intersection_num
        num_true += len(true_entities)
        num_pred += len(pred_entities)
    return tp, num_true, num_pred, mistake_samples
