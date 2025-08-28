import pandas as pd

#Criando uma coluna adicional Salario anual que recebe Salário * 12
df = pd.read_excel("tabela_funcionarios.xlsx")
df['Salario Anual'] = df['Salário'] * 12

print (df)

#Removendo a coluna anterior
df = df.drop('Salario Anual', axis=1)

print (df)