# python script-captura-tweets.py %23testei

import twitter
from pymongo import MongoClient
import datetime, time
import sys

argumentos = sys.argv[1:]

if len(argumentos) == 0 :
	exit()

consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

api = twitter.Api (consumer_key=consumer_key, 
	consumer_secret=consumer_secret, 
	access_token_key=access_token_key, 
	access_token_secret=access_token_secret,
	tweet_mode='extended')

# print (api.VerifyCredentials ())

for argumento in argumentos:
	
	# &result_type=recent&since=2018-07-15&count=100
	resultados  =  api.GetSearch(raw_query='l=pt&count=100&q=' + argumento)

	# print(type(resultados))

	nome_arq = "tweets-"  +  argumento.replace('%','') + datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")

	# backup em arquivo .json
	f = open( 'backup-' + nome_arq + ".json","w+")
	for s in resultados:
		# f.write([s.text for s in resultados])
		f.write("%s\r\n" % (s))
	f.close() 

	# gravando tweets no Mongo
	cliente = MongoClient('localhost', 27017)
	banco = cliente.pfc
	album = banco[nome_arq]

	for s in resultados:
		element = s.AsDict()
		print(element)
		album.insert_one(element)