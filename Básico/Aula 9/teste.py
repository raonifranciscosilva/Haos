# import csv
# from this import d
# from unicodedata import decimal

# #%precision 2

# with open('C:/Users/raoni/OneDrive - UNIP/Python/Haos/Aula 9/mpg.csv') as csvfile:
#     mpg = list(csv.DictReader(csvfile))

# #print(mpg[0].keys()) 
# #mpg[:3] # The first three dictionaries in our list.



# modelos = set(dict['model']for dict in mpg)


# #print(modelos)

import datetime as dt
import time as tm



teste = dt.datetime.fromtimestamp(tm.time())

print(teste)