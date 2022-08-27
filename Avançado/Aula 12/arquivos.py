#Pandas - Análise de dados

#passo 1: import das biblioteca
import pandas as pd
#pd.read_csv('')

#dataframe = necessário caminho, indicação se tem cabeçalho
caminho = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

#especificar o tipo e arquivo que vai ser lido
df = pd.read_csv(caminho, header=None)

#ler o arquivo
#print(df.head())

#print('Exibindo as ultimas linhas do arquivo')
#print(df.tail())

#formalizando o cabeçalho das colunas
cabecalho = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


df.columns = cabecalho

#print(df.info())

import numpy as np

#método replace substitui conteudo do arquivo de dados
df.replace('?', np.NaN, inplace=True )                              #substitui de todas as colunas
#df['normalized-losses'].replace('?', np.NaN)                       #substitui de uma coluna específica

#inplace = não gera um dataframe virtual, ele modifica o dataframe que está
        #   sendo manipulado no momento

#print(df.head(20))

#método para excluir linhas ou colunas
#DROP apaga utilizando um argumento/critério
#DROPNA apaga tudo o que estiver vazio
#df.dropna(subset=['price'], axis=0) #apaga apenas da coluna PRICE

#cria um novo excel, que recebe a planilha antiga, com as linhas apagadas
novo_df = df.dropna(axis=0)

#quando se faz qualquer alteração em dataframe, o python gera um novo dataframe "escondido"
df.dropna(axis=0, inplace=True) #apaga todas as linhas de todas colunas que estão vazias

#print(df.info())

df.to_csv('C:/Users/Public/Downloads/novo.csv', mode='w')
df.to_excel('C:/Users/Public/Downloads/novo.xlsx', sheet_name='dados')





