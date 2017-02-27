from json import load
from yaml import load as yload
import time

with open("pinyin/pinyin.json", 'r') as data_fp:
    hanzi = load(data_fp)

print(hanzi["說"])


with open("pinyin/pinyin.yaml", 'r') as data_fp:
    hanzi = yload(data_fp)

print(hanzi["說"])

