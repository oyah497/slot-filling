import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, 'data')
SUMMARY_DIR = os.path.join(BASE_DIR, 'summary/summary18')
DUMP_DIR = os.path.join(BASE_DIR, 'dump/dump18')

os.makedirs(SUMMARY_DIR, exist_ok=True)
os.makedirs(DUMP_DIR, exist_ok=True)

