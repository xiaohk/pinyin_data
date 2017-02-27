from yaml import dump as yaml_dump
from json import dump as json_dump
import argparse
import re

# Command line argument setting
parser = argparse.ArgumentParser(description='Parse some pinyin.')
parser.add_argument('-y', '--yaml', action = 'store_true', help = "Output to" + 
                    " a YAML file")
parser.add_argument('-j', '--json', action = 'store_true', help = "Output to" +
                    " a JSON file")
parser.add_argument('-d', '--debug', action = 'store_true', help = "Do not" +
                   " dump to files")
args = parser.parse_args()

# Parse from the DB
result = dict()

def format_u(capital):
    # Use 32-bit
    escape = "\\U" + capital[2:].zfill(8)
    return escape.encode('ascii').decode('unicode-escape')

def update_pinyin(uni, pinyin_list, result):
    if uni in result:
        # Can't directly update set, want to keep kMandarin as 
        # the first
        diff_set = set(pinyin_list) - set(result[uni])
        result[uni] = result[uni] + list(diff_set)
    else:
        result[uni] = pinyin_list 

def parse_pinyin():
    # Read from the file
    with open("../data/Unihan_Readings.txt", 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            words = line.split()

            # Comment line or empty line
            if (len(words) < 2 or words[0] == '#'):
                continue

            uni = format_u(words[0])
            # The most common used reading, keep it as the first entry of 
            # value list
            if words[1] == "kMandarin":
                if uni in result:
                    if words[2] not in result[uni]:
                        result[uni] = [words[2]] + result[uni]
                else:            
                    result[uni] = [words[2]]
            
            elif words[1] == "kXHC1983":
                pinyin_list = [p[p.find(':') + 1:] for p in words[2:]]
                update_pinyin(uni, pinyin_list, result)
                
            elif words[1] == "kHanyuPinyin":
                pinyin_list = words[2][words[2].find(':') + 1 : ].split(',')
                update_pinyin(uni, pinyin_list, result)

            elif words[1] == "kHanyuPinlu":
                pinyin_list = [re.sub('\(.*?\)', '', p) for p in words[2:]]
                update_pinyin(uni, pinyin_list, result)

    return result
#def parse_jyutping()
result = parse_pinyin()
                
# Dump the dictionary
if args.yaml:
    with open("../pinyin/pinyin.yaml", 'w') as stream:
        yaml_dump(result, stream, allow_unicode = True)

if (not args.json and not args.yaml and not args.debug) or args.json:
    with open("../pinyin/pinyin.json", 'w') as stream:
        json_dump(result, stream, indent=4, ensure_ascii = False,
                 sort_keys = True)
