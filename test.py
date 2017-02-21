from json import load
from yaml import load as lld
import time

with open("data/pinyin.json", 'r') as data_fp:
    hanzi = load(data_fp)

print(hanzi["說"])

