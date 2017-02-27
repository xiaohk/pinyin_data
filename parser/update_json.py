from yaml import load
from json import dump

with open("../polyphone/polyphone.yaml", 'r') as in_fp:
    with open("../polyphone/polyphone.json", 'w') as out_fp:
        new_dict = load(in_fp)
        dump(new_dict, out_fp, sort_keys = True, ensure_ascii = False,
            indent = 4)
