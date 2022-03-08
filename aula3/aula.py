import pandas as pd

nomesFem = pd.read_csv("NF.csv")
nomesMan = pd.read_csv("NM.csv")

listaNomes = nomesFem.NOME.tolist() + nomesMan.NOMES.tolist()

print(listaNomes)
