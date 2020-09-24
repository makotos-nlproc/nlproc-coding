import MeCab
import itertools
import collections
import string

DATA_TXT_PATH = 'test_text.txt'

def get_noun_list(text):
    tokenizer = MeCab.Tagger()
    node = tokenizer.parseToNode(text)
    nouns = []
    while node:
        if node.feature.split(",")[0] == u"名詞":
            nouns.append(node.surface)
        node = node.next
    return ','.join(nouns)


def clean_text(string_list):
    noun_list = []
    for element in list(itertools.chain.from_iterable(string_list)):
        table = str.maketrans('', '', string.punctuation)
        noun_list.append(element.translate(table))
    nouns_list = []
    while noun_list:
        noun = noun_list.pop()
        if noun != '':
            nouns_list.append(noun)
    return nouns_list


def output_noun_frequency(nouns_list):
    with open('result.txt',mode='w') as f:
        for noun, freq in collections.Counter(nouns_list).most_common():
            if  freq > 29:
                f.writelines(str(f"{noun}:{freq}"))
            f.writelines("\n")


if __name__ == '__main__':
    with open(DATA_TXT_PATH, 'r', encoding='utf-8') as data_file:
        text_data = data_file.read().splitlines()
        noun_list = [''.join(get_noun_list(line)).split(',') for line in text_data]
        nouns_list = clean_text(noun_list)
        output_noun_frequency(nouns_list)
