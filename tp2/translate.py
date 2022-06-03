#pip install googletrans==3.1.0a0
# a versao 3.0.0 da erro
import googletrans

trans = googletrans.Translator()

def getneg():
        
    f = open("neg_en.cat","r")
    lines = f.readlines()

    neg=[]
    neg = trans.translate(lines,dest='pt',src='en')
    print(neg)
    for s in lines:
        t = trans.translate(s,dest='pt',src='en')
        print(t.text)
        neg.append(t.text)

    f.close()
    return neg
def getpos():
    f = open("pos_en.cat","r")
    lines = f.readlines()

    pos=[]
    for s in lines:
        t = trans.translate(s,dest='pt',src='en')
        print(t.text)
        neg.append(t.text)
    f.close()
    return pos

badlist = getneg()
f = open("neg_pt.cat","w")
for w in badlist:
    f.write(w)
    f.write("\n")
f.close()

goodlist = getpos()
f = open("pos_pt.cat","w")
for w in goodlist:
    f.write(w)
    f.write("\n")
f.close()