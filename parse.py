from yaml import dump as yaml_dump
from json import dump as json_dump
import argparse

# Command line argument setting
parser = argparse.ArgumentParser(description='Parse some pinyin.')
parser.add_argument('-y', '--yaml', action = 'store_true', help = "Output to" + 
                    "a YAML file")
parser.add_argument('-j', '--json', action = 'store_true', help = "Output to" +
                    "a JSON file")
args = parser.parse_args()

# Parse from the DB
hanzi = dict()

def format_u(capital):
    # Use 32-bit
    escape = "\\U" + capital[2:].zfill(8)
    return escape.encode('ascii').decode('unicode-escape')

# Read from the file
with open("unihan/Unihan_Readings.txt", 'r') as fp:
    lines = fp.readlines()
    for line in lines:
        words = line.split()

        # Comment line or empty line
        if (len(words) < 3 or words[0] == '#'):
            continue

        uni = format_u(words[0])
        # The most common used reading, keep it as the first entry of value list
        if words[1] == "kMandarin":
            if uni in hanzi:
                if words[2] not in hanzi[uni]:
                    hanzi[uni] = [words[2]] + hanzi[uni]
            else:            
                hanzi[uni] = [words[2]]

        elif words[1] == "kXHC1983" or words[1] == "kHanyuPinyin":
            pinyin_list = words[2][words[2].find(':') + 1 : ].split(',')
            if uni in hanzi:
                # Can't directly update set, want to keep kMandarin as the first
                diff_set = set(pinyin_list) - set(hanzi[uni])
                hanzi[uni] = hanzi[uni] + list(diff_set)
            else:
                hanzi[uni] = pinyin_list 
            
# Dump the dictionary
if args.yaml:
    with open("data/pinyin.yaml", 'w') as stream:
        yaml_dump(hanzi, stream)

if (not args.json and not args.yaml) or args.json:
    with open("data/pinyin.json", 'w') as stream:
        json_dump(hanzi, stream, indent=4)
