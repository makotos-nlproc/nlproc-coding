import MeCab
import itertools
import collections
import string

DATA_TXT_PATH = ''


def split_text_only_noun(text):
    tokenizer = MeCab.Tagger()
    node = tokenizer.parseToNode(text)
    keywords = []
    while node:
        if node.feature.split(",")[0] == u"名詞":
            keywords.append(node.surface)
            print(keywords)
        node = node.next
    return ','.join(keywords)

with open(DATA_TXT_PATH, 'r', encoding='utf-8') as data_file:
        txt_data = data_file.read().splitlines()



#１つ1つのリストaの要素を形態素解析して名詞抽出
r_aa = []

for aa in a:
     r_a = ''.join(split_text_only_noun(aa)).split(',')
     r_aa.append(r_a)

#形態素解析、リストの平坦化、記号の削除
r_aa = list(itertools.chain.from_iterable(r_aa))
kigo = string.punctuation
table = str.maketrans( '', '',kigo)

word_list = []
for bb in r_aa:
    word_list.append(bb.translate(table))

#空白を削除
count = 0
words_list = []
while count < len(word_list):
    if word_list[count] != '':
        words_list.append(word_list[count])
    count += 1

#単語の頻出数
count_num = 0
c = collections.Counter(words_list)

#テキストに書き込み
with open('結果.txt',mode='w') as f:
    for word,count in c.most_common():
        if  count > 50:
            f.writelines(str(f"{word}:{count}"))
            f.writelines("\n")
