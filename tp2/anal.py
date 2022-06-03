import re
from googletrans import Translator
import functools

def sig(n):
    if n>=0:
        return 1
    return -1

def mult(current,mult):
    if abs(mult)<=1:
        return current * added
    else:
        m = abs(mult)
        mod_change = (1-abs(current) )
        return (abs(current) + mod_change*((m-1)/m)) * sig(current*mult)

def mean(x,y):
    return (x+y)/2

def prod(x,y):
    return x*y

#lista de valores absolutos para palavras, entre -1 e 1
lista = {"gosto":1,"desteto":-1,"passar":1,"reprovar":-1,"lido":1,"saboroso":1,"chumbei":-1}

#palavras que alteral a intensidade do que foi dito. valores negativos passam de bom para mau e vice versa.
#valores em mod maiores que 1 aumentam a intensidade, menores diminuem
multiplicadores = {"nao":-1,"muito":2,"pouco":-1}

strings = [
 "passei no exame de condução",
 "chumbei muito no exame de condução",
 "reprovei no exame de condução",
 "hoje choveu torrencialmente",
 "hoje está um lindo sol",
 "ontem comi uma pizza saborosa"
]

s = strings[1]
sums =[]
mults=[]
for word in s.split():
    print(word)
    if word in list(lista):
        sums.append(word)
    if word in list(multiplicadores):
        mults.append(word)
    # se estiver em multiplicadores chamamos mult
print(sums)
print(mults)
m = list(map(lambda a: multiplicadores[a], mults))
m = functools.reduce(prod, m ,1)

a = list(map(lambda a: lista[a], sums))
if len(a)>0:
    a = sum(a)/len(a)
else:
    a=0.5

print(mult(a, m))