import wikipedia
from textblob import TextBlob, Word
import re
import nltk
#nltk.download('omw-1.4')

def isWord(s):
    return re.search("\s", s) == None

#traduz uma word list para En
def toEn(word_list):
    newwl = []
    for w in word_list:
        newwl.append( str(Word(w).translate(from_lang="pt",to="en")) )

def test_word(word,words):

    wikipedia.set_lang("en")
    result = wikipedia.search(word)

    # pega no texto todo da pagina e poe em body
    body = wikipedia.page(result[0]).content
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
    related = filter(ordered_counts , lambda x: x[1]>0)
    unrelated = filter(ordered_counts , lambda x: x[1]==0)

    #print(body)
    print("palavras relacionadas:\n")
    print(related)
    print("palavras nao relacionadas:\n")
    print(unrelated)

words = ["tooth","gingiva","tooth decay"]
en_words = toEn(words)

#palavra que vamos testar
word = "human teeth"
test_word(word, words_en)
