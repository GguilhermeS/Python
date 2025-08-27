import pandas as pd

df = pd.read_csv('tabela_funcionarios.csv')

# 5 primeiras linhas
print(df.head())

# Verificando informações gerais
print(df.info())

# Estatísticas descritivas
print(df.describe())

# Visualizar todos os nomes
print(df["Nome"])

#Se o arquivo estiver Lendo uma planilha Excel

#df = pd.read_excel('tabela_funcionarios.xlsx', sheet_name='Nome da aba')
#print(dados.keys()) mostra o titulo das abas // sheet_name=None