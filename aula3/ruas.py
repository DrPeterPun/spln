f = open("ruasBraga_v1",r).read()

# nomes = open("nomes.txt").read()

na = set(nomes.strip() for nomes in open("nomes.txt"))

#isto da print a todos os nomes
# print(a)

pat = "|".join(na)

print(pat)

comAT = re.sub(rf'\b({pat})\b', "@\1@", f)
ncomAT = re.sub(rf"@\s*@",r" ", comAt)
ncomAT2 = re.sub(rf"@\s*(de|do|da|dos|das)\s*@",r"\1", ncomAt)

def fs(m):
    return f"@{m[1]}@" if m[1] in na else m[1]

comAT = re.sub(rf'\b({pat})\b', fs, f)
