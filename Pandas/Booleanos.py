import pandas as pd

df = pd.read_excel("tabela_funcionarios.xlsx")

#Retorna resultados True ou False
print (df['Idade'] > 30)

#Retorna os dados seguindo o filtro, exemplo idade maior que 30
print(df[df['Idade'] > 30])

#Exemplo de filtro
print(df[df['Salário'] > 5000])

#Filtros combinados e aplicados em variaveis
filtro_maior_que_30 = df['Idade'] > 30
filtro_mais_de_5mil = df["Salário"] > 5000

print(df[filtro_maior_que_30 & filtro_mais_de_5mil])