import requests
import re

# Parse from the HTML file
with open("../data/polyphone1.html.txt", 'r') as fp:
    with open("../data/raw1.txt", 'w') as out_fp:
        lines = fp.readlines()
        out = []
        for line in lines:
            if '【' in line:
                # Remove HTML tags and spaces
                add = line.replace("<td>", "")
                add = add.replace("</td>", "")
                add = add.replace("            ", "")

                # Format each line
                temp = add.split('【')
                # The first one is empty string
                for entry in temp[1:]:
                    pinyin = entry[:entry.find('】')]
                    # Clean the pinyin format
                    # 1.replace 'iǜ' as 'iù'
                    pinyin = pinyin.replace('iǜ', 'iù')

                    words = re.split(',|\s', entry[entry.find('】') + 1:])

                    # Get rid of the empty string and parenthesis
                    final = [re.sub('（.*?）|（.*?\s? | \s?.*? ）', '', word) \
                             for word in words if word !='']
                    final = [f for f in final if f != '']
                    formated = pinyin + ' : ' + ', '.join(final) + '\n'
                    out_fp.write(formated)


