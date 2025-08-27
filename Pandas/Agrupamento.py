import pandas as pd

df = pd.read_excel("tabela_funcionarios.xlsx")

#Agrupar por departamento
print(df.groupby("ID Departamento"))

#Agrupar a media salarial pelo departamento
print(df.groupby("ID Departamento") ["Salário"].mean())

#Agrupar a soma salarial pelo departamento
print(df.groupby("ID Departamento") ["Salário"].sum())

#Agrupar a maxima salarial pelo departamento
print(df.groupby("ID Departamento") ["Salário"].max())