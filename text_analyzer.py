'''import re
import pymorphy2

morph = pymorphy2.MorphAnalyzer(lang='uk')

from collections import defaultdict
print(defaultdict(list))


def analyzePos(file):
    pos_dict = {}

    text = re.sub(r'[^\w]', ' ', file).lower().split()

    for word in text:
        p = morph.parse(word)[0]
        pos_dict[word] = p.tag.POS
        # pos_dict[p.normal_form] = p.tag.POS - return lemma and pos

    return pos_dict


def analyzeLemma(file):
    lemma_dict = {}

    text = re.sub(r'[^\w]', ' ', file).lower().split()

    for word in text:
        p = morph.parse(word)[0]
        lemma_dict[word] = p.normal_form

    return lemma_dict
'''


import re
import pymorphy2
from collections import defaultdict

morph = pymorphy2.MorphAnalyzer(lang='uk')


def analyze(file):
    words = defaultdict(list)

    with open(file, 'r', encoding='utf-8') as f:
        rawtext = f.read()

    text = re.sub(r'[^\w]', ' ', rawtext).lower().split()

    for w in text:
        words[morph.parse(w)[0].normal_form] = (morph.parse(w)[0].tag.POS, [
            inf[0] for inf in morph.parse(w)[0].lexeme])

    return words
