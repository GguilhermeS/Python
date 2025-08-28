import pandas as pd
df = pd.read_excel("tabela_funcionarios.xlsx")
df_dept = pd.read_excel("Departamentos.xlsx")

# Visualizar tabelas
print("Funcionários:")
print(df)
print("Departamentos:")
print(df_dept)

# Combinar tabelas pelo ID do departamento
df_final = pd.merge(df, df_dept, left_on='ID Departamento', right_on='ID Departamento')

print(df_final)
