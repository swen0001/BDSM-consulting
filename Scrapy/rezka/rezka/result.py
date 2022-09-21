import csv
import os

import pandas as pd

with open(f'data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
# run spider
os.system("scrapy crawl rezka_film -o data.csv --nolog")

print('*' * 66 + ' PANDAS ' + '*' * 66)
df = pd.read_csv('data.csv')
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", 50)
pd.set_option('display.width', None)
print(df)
print('*' * 140)
