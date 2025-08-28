import pandas as pd

df = pd.read_csv['tabela_funcionarios.csv']

#Remove todas as linhas que contem valor nulo
df.dropna()
print (df)

#Remover dados nulos de uma tabela especifica
df.dropna(subset="Idade")

#Preencher valor nulos com outro tipo de dados (no caso uma media)
media_idade = df['Idade'].mean()
df['Idade'] = df['idade'].fillna(media_idade)
print (df)

#Trocar o tipo de dado
df['idade'] = df['Idade'].astype(int)
print (df)

