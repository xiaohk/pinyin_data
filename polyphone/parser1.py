import re

# Parse from the HTML file
with open("polyphone1.html", 'r') as fp:
    with open("raw1.txt", 'w') as out_fp:
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
                    words = re.split(',|\s', entry[entry.find('】') + 1:])
                    # Get rid of the empty string and parenthesis
                    final = [re.sub('（.*?）|（.*?\s? | \s?.*? ）', '', word) \
                             for word in words if word !='']
                    final = [f for f in final if f != '']
                    print(final)
                    formated = pinyin + ' : ' + ', '.join(final) + '\n'
                    print(formated)
                    out_fp.write(formated)

# Parse from the text file
#with open("raw1.txt", 'r') as fp:
#    with open("polyphone1.txt", 'w') as out_fp:

