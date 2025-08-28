import pandas as pd

df = pd.read_excel("Lista_Funcionarios")

#ordenar dados
print (df.sort_values(by='Idade'))

#ordenar dados maior para menor
print (df.sort_values(by='Idade', ascending=False))

#ordenar dados menor para maior
print (df.sort_values(by='Idade', ascending=True))

#ordenar dados modificando o original
#print (df.sort_values(by='Idade', inplace=True))


