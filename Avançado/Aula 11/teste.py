import pandas as pd
import numpy as np

#Acesso aos dados
import pandas as pd

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)

#Exibir os dados - início
# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)

#Observe que não tem nome nas colunas

#Exibir os últimos dados
# Write your code below and press Shift+Enter to execute 
df.tail(10)


#Criando os cabeçalhos – jogar no pastebin 
# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

# Jogando os nomes para o cabeçalho
df.columns = headers
#df.columns = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
        #   "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
        #   "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
        #   "peak-rpm","city-mpg","highway-mpg","price"]

df.head(10)


# Arrumando células vazias
df.head()
import numpy as np


df1=df.replace('?',np.NaN)
df1.head(10)

# Excluir linhas com células vazias – especificando a coluna
df=df1.dropna(subset=["normalized-losses"], axis=0)
#df = df1.dropna(subset='price', )
df.head(20)




# Salvando o arquivo
df.head()
import numpy as np
import openpyxl as opx

df.replace('?', np.NaN, inplace=True)
print(df.head(10))

df.to_csv(path_or_buf='C:/Users/raoni/Downloads/novo.csv', mode='w')

df.to_excel(excel_writer='C:/Users/raoni/Downloads/novodf.xlsx',
 
sheet_name='planilha1')


