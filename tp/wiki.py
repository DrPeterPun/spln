import wikipedia
from textblob import TextBlob, Word
import re
import sys
import nltk
import pprint
#nltk.download('omw-1.4')

f = open("med_nomes")

med_list = f.readlines()
words = []
#print(med_list)
for w in med_list:
    ww = w.strip("\n")
    words.append(ww)
    #blob = TextBlob(ww)
    #traducao = blob.translate(to='en')
    #translated.append(traducao)
    #print(ww)

def isWord(s):
    return re.search("\s", s) == None

#traduz uma word list para En
#def toEn(word_list):
#    newwl = []
#    for w in word_list:
#        newwl.append( str(Word(w).translate(from_lang="pt",to="en")) )
#   return newwl

def test_word(word,words):
    wikipedia.set_lang("pt")
    result = wikipedia.search(word)

    # pega no texto todo da pagina e poe em body
    page = wikipedia.page(result[0])
    print("url: " + page.url)
    body = page.content
    blob = TextBlob(body)

    body_l= ' '.join([w.lemmatize() for w in blob.words])
    blob_l = TextBlob(body_l)

    
    # numero de ocorrencias de palavras e noun phrases
    np = blob.np_counts
    nl = blob_l.word_counts
    word_counts = {}

    for w in words:
        if(isWord(w)):
            # procura na lista lematizada
            w_l = Word(w).lemmatize()
            word_counts.update({w :nl[w_l] })
        else:
            #faz procura nas nps
            word_counts.update({w :np[w] })

    ordered_counts = sorted(word_counts.items(),key=lambda x :x[1], reverse=True)
    related = dict(filter(lambda x: x[1]>0, ordered_counts ))
    unrelated = dict(filter(lambda x: x[1]==0, word_counts.items() ))
    #print(ordered_counts)
    #print(body)
    #print("palavras relacionadas:\n")
    pp = pprint.pformat(related,sort_dicts=False)
    print("relacoes de " + word)
    print(pp)
    #print(related)
    #print("palavras nao relacionadas:\n")
    #print(unrelated)

#words = ["tooth","gingiva","tooth decay","arm"]

#palavra que vamos testar
word = "cerebro"
if len(sys.argv)==2:
    word= sys.argv[1]
test_word(word, words)
