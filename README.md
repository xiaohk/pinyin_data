# Pinyin Data
Easy to use and portable pronunciation data for Hanzi characters.

## Pinyin
`./pinyin/pinyin.json` and `./pinyin/pinyin.yaml` contain the same Pinyin records
for 41216 Hanzi characters (both traditional and simplified).

Each file is a dictionary mapping Hanzi character to a list of Pinyin's.
```python
{'长' : ['zhǎng', 'cháng'],
 '長' : ['zhǎng', 'cháng', 'zhàng']}
```

- First element of the Pinyin list is the most frequently used pronunciation.
- All Pinyin records are from `kMandarin`, `kXHC1983`("现代汉语词典"), 
`kHanyuPinlu`("现代汉语频率词典"), `kHanyuPinyin`("汉语大字典") feilds of 
Unihan reading database.
- Unihan reading database version: `2016-06-01 07:01:48 GMT`

## Polyphone
Some Hanzi characters have multiple pronunciation, 
`./polyphone/polyphone.json` and `./polyphone/polyphone.yaml` are used to map
the particular pronunciation to corresponding word context.

Each file is a dictionary mapping Hanzi character to an inner dictionary. The
inner dictionary map Pinyin to a list containing three lists of words. Three 
lists contain the words where the Hanzi character is at the beginning, in the 
middle or at the end.

```python
{'会': {huì:[['会合'], [], ['都会']],
        kuài:[['会计'], [], ['财会']]}}
```

In this version, all polyphone data are parsed from this [website](http://www.fuhaoku.com/duoyinzi/). The overall coverage is still limited, so you are more than
welcome to add more example words and entries into the polyphone collection.

1. You can parse data from other websites and add non-duplicate words into the 
Polyphone dictionary using the same structure. Just a heads up, there might be
lots of errors on the websites.
2. You can simply add new words into the correct list in 
`./polyphone/polyphone.yaml`, then run `./parse/update_json.py` to sync it to
`./polyphone/polyphone.json`. 

## Use
Clone the git, then copy the interested data to your project.

Use of the Pinyin information should follow [Unicode® Terms of Use](http://www.unicode.org/copyright.html). Other codes use MIT licence.

## TODO List
- Add Jyuping records


## How to Contribute:
1. Create an issue.
2. Add words into Polyphone collection, fix bugs, add features, then pull request.

