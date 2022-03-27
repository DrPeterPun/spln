import re

f = open('medicina.xml')
#print(f.read())
texto = f.read()

# 1
res = re.sub(r'.*?<page number="20"', '', texto, flags=re.S, count=1)
# 2
res = re.sub(r'<page number="544".*', '', res, flags=re.S, count=1)
# 3
res = re.sub(r'<text top="862" left="320" width="23" height="18" font="8">.*?</text>', '', res)
res = re.sub(r'<text top="862" left="324" width="15" height="18" font="8">.*?</text>', '', res)

res = re.sub(r'<text.*?>', '', res)
res = re.sub(r'</text>', '', res)
# 4 
res = re.sub(r'<[bi]>\s*</[bi]>','',res)
# 5
res = re.sub(r'<page.*?>','',res)
res = re.sub(r'</page>', '', res)

res = re.sub(r'V\nocabulario', '', res)

#Tratamento de entradas
def trataEntrada(entry):
    c = re.split(r'<b/>', entry,maxsplit=1)
    m = re.fullmatch("\s*(\d+)\s*(.*?)\s*(\w+)", c[0]) 
    if m :
        print(m.groups())
    else:
        print(c[0].strip())
    info = re.sub(r"\b(en|pt|es|ls)\b",r"@\1",c[1])
    info = re.sub(r"((?:SIN|Nota|VAR|Vid)\.-)",r"$$\1",info)
    print("///////////////////////////",info)
    # procura todas as traducoes
    traducoes = re.findall(r"@\1[^@\1]+*", info)
    # procurar os sin,nota,var , vid
    sinvar = re.findall(r"$$[^$$]+*", string)
    #
    
    print("tracucoes", traducoes)
    print("sin var notas etc...", sinvar)
    

for elem in re.split(r'<b>',res):
    trataEntrada(elem)


#print(res)