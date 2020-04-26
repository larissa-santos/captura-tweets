from pymongo import MongoClient
import pandas as pd

cliente = MongoClient('localhost', 27017)
banco = cliente.pfc

album = banco['sem_texto_repetido']
cursor = album.find({}, { 'id' : 1, 'full_text': 1, '_id': 0})

df =  pd.DataFrame(list(cursor))
df.to_csv('tabela2.csv', index=True)