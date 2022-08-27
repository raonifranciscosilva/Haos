from importlib.resources import path
import pandas as pd
import numpy as np

caminho = 'C:/Users/raoni/Downloads/arquivo.csv'
#caminho = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv'

arquivo = pd.read_csv(caminho)

print(arquivo.tail())



