import re
from json import load, dump
from yaml import dump as ydump

"""
Parse from the text file to data structure

Data structure is designed as the following:
    - A dictionary mapping one <String> hanzi to a dictionary pinyin -> list:
        - The inner dictionary key is a <String> pinyin:
            - First inner list contains all words where the hanzi is the first 
            character and uses the 'key' prounciation
            - Second inner list contains all words where the hanzi is in the
            middle and uses the 'key' prounciation
            - Third innter list contains all words where the hanzi is the last 
            character and uses the 'key' prounciation
"""
with open("../pinyin/pinyin.json", 'r') as data:
    pinyin_dict = load(data)

def add_wrod(pinyin, word, out_dict):
    print(word)
    # Find the character having that pronunciation
    target_char = ''
    target_index = 0
    for char in word:
        if pinyin in pinyin_dict[char]:
            target_char = char
            break
        target_index += 1

    # Add the word into out_dict
    # No char entry in out_dict
    if target_char not in out_dict:
        # Initialize the inner dictionary
        out_dict[target_char] = dict()
        for p in pinyin_dict[char]:
            out_dict[target_char][p] = [[], [], []]
        
    # Add this word into the correct entry
    if target_index == 0:
        out_dict[target_char][pinyin][0].append(word)
    elif target_index == len(word) - 1:
        out_dict[target_char][pinyin][2].append(word)
    else:
        out_dict[target_char][pinyin][1].append(word)

# Make the dictionary
with open("../data/raw1.txt", 'r') as fp:
    out_dict = {}
    lines = fp.readlines()
    for line in lines:
        formated = list(filter(None, re.split(':|,|\s', line)))
        for word in formated[1:]:
             add_wrod(formated[0], word, out_dict)

# Dump the dictionary into yaml and json
with open("../polyphone/polyphone.yaml", 'w') as fp:
    ydump(out_dict, fp, allow_unicode = True)

with open("../polyphone/polyphone.json", 'w') as fp:
    dump(out_dict, fp, indent = 4, ensure_ascii = False, sort_keys = True)
