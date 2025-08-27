import pandas as pd

df_novos = pd.read_excel("novos_funcionarios.xlsx")
#Empilha os novos funcionarios em uma nova tabela com os funcionarios antigos
#ignore_index=True para o indice continuar correto de 0, 1, 2, 3...
df_todos = pd.concat([df, df_novos], ignore_index=True)

print(df_todos)

#Vai gerar os novos funcionarios na tabela, pode se usar csv dentre outros
df_todos.to_excel('todos_os_funcinarios.xlsx', index=False)