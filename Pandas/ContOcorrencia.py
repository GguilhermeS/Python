import pandas as pd

df = pd.read_excel("tabela_funcionarios.xlsx")

#Contagem de ocorrencia de funcionarios ativos
print(df["Ativo"].value_counts())

#Contagem de id (para saber quantos funcionarios tem em cada departamento)
print(df["ID Departamento"].value_counts())