import pandas as pd

df = pd.read_csv('tabela_funcionarios.csv')

# 5 primeiras linhas
print(df.head())

# 5 ultimas linhas
print(df.tail())

# Verificando informações gerais como tipo de dados e valores nulos
print(df.info())

# Estatísticas descritivas das colunas numericas
print(df.describe())

# Soma de uma coluna
df = ['Salário'].sum()
print (df)

# Media de uma coluna
df = ['Salário'].mean()
print (df)

# Visualizar todos os nomes
print(df["Nome"])

# Selecionar coluna(s) especificas
print(df['Nome', 'Idade'])

#Se o arquivo estiver Lendo uma planilha Excel

#df = pd.read_excel('tabela_funcionarios.xlsx', sheet_name='Nome da aba')
#print(dados.keys()) mostra o titulo das abas // sheet_name=None