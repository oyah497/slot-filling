import argparse
#import setting
import os
from gsl.datasets import generate_text_data, slot_list, SLDataset
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
parser.add_argument('--model-name', help='Model name.', type=str, default='t5-base')
parser.add_argument('--batch-size', help='Batch size.', type=int, default=16)
parser.add_argument('--num-epochs', help='Train epochs.', type=int, default=100)
parser.add_argument('--lr', help='Learning rate of train step.', type=float, default=2e-5)
parser.add_argument('--query-max-seq-length', help='Max sequence length for query.', type=int, default=128)
parser.add_argument('--response-max-seq-length', help='Max sequence length for response.', type=int, default=64)
parser.add_argument('--num-beams', help='T5 generation beam number.', type=int, default=2)
parser.add_argument('--query-schema', help='Schema for query generation', type=str,
                    choices=['slot_desc',
                             'slot_desc+domain_desc',
                             'example',
                             'context_example',
                             'slot_desc+example',
                             'slot_desc+context_example',
                             'slot_desc+domain_desc+context_example',
                             'min',
                             'notSD',
                             'proposed_query1',
                             't5_query1',
                             'each_slot',
                             'each_slot_dummy',
                             'something',
                             'example_rcsf',
                             'example_rcsf2',
                             'example_rcsf3',
                             'without_example',
                             'unk_wo',
                             'dummy_unk',
                             'dummy_unk_ab',
                             'dummy_unk2',
                             'nosep',
                             'nosep_ab',
                             'nosep_or',
                             'nosep_rcsf',
                             'nosep_qa',
                             'nosep_rcsf_ab',
                             'nosep_rcsf_or',
                             'nosep_rcsf_ex2',
                             'nosep_rcsf_ex2_long',
                             'nosep_rcsf_ex2_long_ab',
                             'nosep_rcsf_ex2_slots',
                             'nosep_rcsf_ex2_upper',
                             "nosep_rcsf_ex2_negex",
                             'nosep_rcsf_ex2_ab',
                             'nosep_rcsf_ex2_ab_or',
                             'sepsep',
                             "nosep_rcsf_ex2_ab_num",
                             "arrow1",
                             't5',
                             't5_said',
                             't5_openai',
                             'nosep_rcsf_ex2_ab_or_wo_q',
                             'wo_q_wo_or',
                             'wo_q_wo_or2',
                             'wo_q_wo_or_plain',
                             'wo_q_wo_or_wo_ex',
                             'aisfg',
                             'aisfg_comp',
                             'ablation',
                             'ablation2',
                             'ablation3',
                             'ablation4',
                             'wo_q_wo_or_plain2',
                             ], default='slot_desc')
parser.add_argument('--response-schema', help='Schema for response generation', type=str,
                    choices=['plain', 'proposed', 'proposed2', 't5_resp1', 'each_slot', 'each_slot_dummy', 'something', 'plain_not_found', 'unk', 'dummy_unk', 'dummy_unk_ab', 'nosep', 'nosep_ab', 'nosep_or', 'nosep_plain', 'nosep_rcsf', 'nosep_qa', 'nosep_rcsf_plain', 'nosep_qa_plain', 'nosep_rcsf_ab', 'nosep_rcsf_or', 'nosep_rcsf_ex2', 'nosep_rcsf_ex2_long', 'nosep_rcsf_ex2_long_ab', 'nosep_rcsf_ex2_upper', 'nosep_rcsf_ex2_mlm',
                    'nosep_rcsf_ex2_ab',
                    'sepsep',
                    "arrow1",
                    "arrow1_1",
                    't5_plain',
                    't5_said_plain',
                    't5_said_the_is',
                    't5_openai_plain',
                    't5_openai_the_is',
                    'nosep_rcsf_ex2_ab_or',
                    'nosep_rcsf_ex2_ab_or_wo_q',
                    'wo_q_wo_or',
                    'wo_q_wo_or2',
                    'wo_q_wo_or_plain',
                    'wo_q_wo_or_wo_ex',
                    'aisfg',
                    'aisfg_comp',
                    'ablation',
                    'ablation2',
                    'ablation3',
                    'ablation4',
                    'wo_q_wo_or_plain2',
                    ], default='plain')
parser.add_argument('--shot-num', help='Shot number.', type=int, default=0)
parser.add_argument('--patience', help='Patience epoch for early stop.', type=int, default=5)
parser.add_argument('--dir-num', help='Dir-num.', type=str, default='0000')
#parser.add_argument('--decoder-input', help='decoder input', action='store_true')

args = parser.parse_args()


def process_args():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    DATA_DIR = os.path.join(BASE_DIR, 'data')
    SUMMARY_DIR = os.path.join(BASE_DIR, 'summary/summary' + args.dir_num)
    DUMP_DIR = os.path.join(BASE_DIR, 'dump/dump' + args.dir_num)

    os.makedirs(SUMMARY_DIR, exist_ok=True)
    os.makedirs(DUMP_DIR, exist_ok=True)
    args.summary_dir = SUMMARY_DIR #setting.SUMMARY_DIR
    args.dump_dir = DUMP_DIR #setting.DUMP_DIR
    args.data_dir = DATA_DIR #setting.DATA_DIR

    args.exp_name = '%s-%s-%s' % (args.model_name.replace('/', '_'), args.tgt_domain, args.shot_num)


process_args()
seed_everything(args.seed)


def train():
    train_data, valid_data, test_data, seen_data, unseen_data = generate_text_data(args.data_dir,
                                                                                   args.tgt_domain,
                                                                                   shot_num=args.shot_num)
    train_dataset = SLDataset(train_data, query_schema=args.query_schema, response_schema=args.response_schema) #,decode_input=args.decoder_input)
    valid_dataset = SLDataset(valid_data, query_schema=args.query_schema, response_schema=args.response_schema)#, decode_input=args.decoder_input)
    test_dataset = SLDataset(test_data, query_schema=args.query_schema, response_schema=args.response_schema)#, decode_input=args.decoder_input)
    seen_dataset = None if seen_data is None else SLDataset(seen_data, query_schema=args.query_schema,
                                                            response_schema=args.response_schema)#, decode_input=args.decoder_input)
    unseen_dataset = None if unseen_data is None else SLDataset(unseen_data, query_schema=args.query_schema,
                                                                response_schema=args.response_schema)#, decode_input=args.decoder_input)


    #valid_slot_list = slot_list(valid_data)
    #test_slot_list = slot_list(test_data)
    #seen_slot_list = slot_list(seen_data)
    #unseen_slot_list = slot_list(unseen_data)

    trainer = Trainer(args.model_name, args)
    trainer.fit(train_dataset, valid_dataset, test_dataset, seen_dataset, unseen_dataset,
                #valid_slot_list, test_slot_list, seen_slot_list, unseen_slot_list,
                batch_size=args.batch_size, lr=args.lr, epochs=args.num_epochs, patience=args.patience,
                query_max_seq_length=args.query_max_seq_length, response_max_seq_length=args.response_max_seq_length,
                num_beams=args.num_beams)


if __name__ == '__main__':
    train()
