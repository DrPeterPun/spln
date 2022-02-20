#! /usr/bin/env python3
from ctypes import sizeof
import re
import functools

file = open('ABM_807', "r")
lines = file.readlines()
recasamento = re.compile(r'Registo de casamento n.º \d*: (.*\S) c.c. (.*\S)\s*')
rebatismo = re.compile(r'Registo de batismo n.º \d*: (.*\S) \. Pai: (.*\S) ; M.e: (.*\S)')


nomes = []

for line in lines:
    r = recasamento.search(line)
    if r:
        nomes.append(r.groups()[0])
        nomes.append(r.groups()[1])
    r = rebatismo.search(line)
    if r:
        c = r.groups()[0]
        pai =r.groups()[1]
        mae = r.groups()[2]
        # print(c + ";" + pai  + ";" + mae) 
        # primeiro ver se o nome da mae acaba em "de qlqr coisa"
        relastname = re.compile(r'(d(a|e|o ) )?\w+\Z')
        lnpai = relastname.search(pai)
        lnmae = relastname.search(mae)
        if c and lnpai and lnmae:
            c =  f"{c} {lnmae[0]} {lnpai[0]}"
            nomes.append(c)
            #print(c)
            nomes.append(mae)
            nomes.append(pai)

print(f"existem {len(nomes)} nomes")

dict = {}
for n in nomes:
    if not dict.get(n):
        dict.update({n:0})
    dict.update({n: dict.get(n)+1})


def scnd(a):
    fst, snd = a
    return snd

def frst(a):
    fst, snd = a
    return fst

dictitems = dict.items()
print(f"existem {len(dictitems)} nomes")
#print("por ordem de frequencia: ")
#print(list(map(frst , sorted(dictitems, key=scnd , reverse=True))))
print(sorted(dict.keys()) )






