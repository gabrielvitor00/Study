



import pandas as pd
import os

# Lista de arquivos Excel para juntar
arquivos_excel = ['arquivo1.xlsx', 'arquivo2.xlsx', 'arquivo3.xlsx']

# Lista para armazenar dataframes
dfs = []

# Para cada arquivo, leia o arquivo para um dataframe e adicione à lista
for arquivo in arquivos_excel:
    df = pd.read_excel(arquivo)
    dfs.append(df)

# Concatene todos os dataframes na lista
df_final = pd.concat(dfs)

# Escreva o dataframe final para um novo arquivo Excel
df_final.to_excel('arquivo_final.xlsx', index=False)