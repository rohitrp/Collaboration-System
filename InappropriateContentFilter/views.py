from django.shortcuts import render
import re
import json

bad_words = json.load(open('InappropriateContentFilter/bad-words.json'))
bad_words.sort(key=len, reverse=True)
bad_words_pattern = r'\b(?:%s)\b' % '|'.join(bad_words)
bad_words_regex = re.compile(bad_words_pattern, re.I)

def inappropriate_content_filter(*arg):
    text = arg[0] + ' ' + arg[1]
    inappropriate_words = re.findall(bad_words_regex, text)     
    
    res = { 'inappropriate': True, 'inappropriate_words': inappropriate_words }

    if len(inappropriate_words) == 0:
        res['inappropriate'] = False

    return res
