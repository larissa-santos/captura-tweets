# python C:\xampp\htdocs\captura-tweets\limpar-tweets.py %23eleicoes2018

from pymongo import MongoClient
import datetime, time
import sys
import re


def removeString(tweet):
	hashtags = ['#JuntosPodemosMais', '#AlvaroDias', '#CaboDaciolo', '#CaboDaciolo2018', '#Daciolo', '#Daciolo2018', '#CiroPresidente12', '#CiroGomes', '#VemPraMassa', '#TodosComCiro', '#CiroNaGlobo', '#CiroNaGloboNews', '#CiroNoJornalNacional', '#HaddadNoSBT', '#HaddadSim', '#Haddad', '#HaddadPresidente', '#HaddadAmarelou', '#HaddadÉLulaNoSBT', '#HaddadNoJornalNacional', '#HaddadNoSBT', '#EquipePSDB', '#PreparadoParaOBrasil', '#GeraldoAlckimin', '#GeraldoAlckimin2018', '#Alckimin', '#AlckminNaGloboNews', '#AlckminNoJornalNacional', '#GeraldoNoJN', '#BoulosESonia', '#PSOL2018', '#VamosSemMedo', '#HenriqueMeirelles', '#Meirelles', '#Meirelles2018', '#Bolsonaro', '#JairBolsonaro', '#BolsonaroPresidente', '#BrasilComBolsonaro', '#Elenao', '#BolsonaroNoPanico', '#BolsonaroNoJornalNacional', '#JBnaGlobo   ', '#BolsonaroNoRodaViva ', '#OndaLaranja', '#VamosRenovarTudo', '#JoaoAmoedo', '#JoaoAmoedo2018', '#JoaoNoJN', '#JoaoNoJornalNacional', '#JoaoAmoedo30 ', '#VemComJoao30', '#JoaoGoulart2018', '#JoaoGoulart', '#JoseMariaEymael', '#JoseEymael', '#JoseEymael2018', '#TIMELULA', '#OBrasilFelizdeNovo', '#Lula2018', '#Marina', '#MarinaSilva', '#MarinaSilva2018', '#MarinaNaGloboNews', '#MarinaNoJN', '#MarinaNoJornalNacional ', '#JornalNacional', '#DebateNaRecord', '#OVotoNaRecord', '#OVotoNaRecord2018', '#DebateSBT', '#SegundoTurno', '#DebateRedeTV', '#DebateGlobo', '#DebateNaGlobo', '#eleicoes2018', '#Eleicoes2018', '#VeraLucia', '#VeraLucia2018']
	candidatos = ['Álvaro Dias', 'Alvaro Dias', 'Cabo Daciolo', 'Ciro Gomes', 'Fernando Haddad', 'Geraldo Alckimin', 'Guilherme Boulos ', 'Henrique Meirelles', 'Jair Bolsonaro', 'João Amoêdo', 'Joao Amoedo', 'João Goulart', 'Joao Goulart', 'José Maria Eymael', 'Ze Eymael', 'Lula', 'Marina Silva', 'Vera Lúcia', 'Vera Lucia', 'Alvaro', 'Dias', 'Cabo', 'Daciolo', 'Ciro', 'Fernando', 'Haddad', 'Geraldo', 'Alckimin', 'Guilherme', 'Boulos', 'Henrique', 'Meirelles', 'Jair', 'Bolsonaro', 'João', 'Amoêdo', 'Joao', 'Amoedo', 'Goulart', 'Eymael', 'Lula', 'Marina', 'Silva', 'Vera', 'Lúcia', 'Lucia']
	
	# retirando tags usadas para pesquisa
	for hashtag in hashtags:
		tweet = re.sub(hashtag, '#', tweet, flags=re.IGNORECASE)

	# retirando candidatos
	for nome in candidatos:
		tweet = re.sub(nome, 'candidato', tweet, flags=re.IGNORECASE)

	# retirando marcacao de user
	userER = re.compile('@[a-zA-Z]+')
	return userER.sub('@fulano', tweet)

def buscaDados(banco, collect):
	album = banco[collect]
	return album.find({})
	

argumentos = sys.argv[1:]

if len(argumentos) == 0 :
	exit()

count = 0

for argumento in argumentos:
	
	# &result_type=recent&since=2018-07-15&count=100

	# print(type(resultados))

	# nome_arq = "tweets-"  +  argumento.replace('%','') + datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")

	# f = open( 'C:\\Users\\larri\\OneDrive\\Documentos\\database\\' + nome_arq + ".json","w+")
	# for s in resultados:
	# 	# f.write([s.text for s in resultados])
	# 	f.write("%s\r\n" % (s))
	# f.close() 


	cliente = MongoClient('localhost', 27017)
	banco = cliente.pfc

	# listando todas as collections do bd
	collections = banco.collection_names()

	# removendo collections com lixo
	collectionsRemove = ['tweets_truncated','tweets_truncated_no']
	collections.remove('tweets_truncated')
	collections.remove('tweets_truncated_no')

	print(collections)
	collections = ['tweets-20180811190552', 'tweets-23Alckimin20180822212810']
	for collect in collections:
	    # print (collect)
		resultados = buscaDados(banco, collect)
		for tweet in resultados:
			count = count +1
			print(tweet['full_text'])
			print('--->')
			print(removeString(tweet['full_text']))
	
	print(count)