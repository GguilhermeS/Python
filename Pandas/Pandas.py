#Importação para utilizar os pandas
import pandas as pd

dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'idade': [25, 47, 32],
}

df = pd.DataFrame(dados)

print(df)

