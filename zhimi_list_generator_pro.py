# 使用方法: python zhimi_list_generator.py text.txt list.txt
# 其中text.txt是待抽取单词本的文本，list.txt是生成单词本
import sys
import re
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.probability import FreqDist
from nltk import RegexpTokenizer
toknizer = RegexpTokenizer(r'''\w'|\w+|[^\w\s]''')
def get_unique_words(path,exclude, coding):
    f = open(path,encoding=coding)
    text = f.read()
    f.close()
    words = toknizer.tokenize(text)
    words = [WordNetLemmatizer().lemmatize(WordNetLemmatizer().lemmatize(word,'v'),'n') for word in words]
    fdist = FreqDist(words)
    tops = fdist.most_common(len(fdist))
    return tops

    
tops = get_unique_words(sys.argv[1],sys.argv[3] if len(sys.argv)==4 else "",'utf8')

topf = open(sys.argv[2],'w',encoding='utf8')
for j in tops:
    i = j[0]
    if all((char>='a' and char<='z') or (char>='A' and char<='Z') or (char>='Ï' and char<='œ')  for char in i):
        topf.write(i)
        topf.write('\n')
topf.close()
