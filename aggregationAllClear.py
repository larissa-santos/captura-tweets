from pymongo import MongoClient
import datetime
import re

def buscaDados(album, value = None):
    if value != None:
        return album.find( value, { '_id': 0})
    else :
        return album.find({}, { '_id': 0})
	
def salvarEmCollection(album, element):
	album.insert_one(element)

cliente = MongoClient('localhost', 27017)
banco = cliente.pfc

regx = re.compile("^RT ", re.IGNORECASE)

## trecho de código que retira os tweets repetidos (mesmo ID)
album = banco['all_tweets_3']
pipeline = [ 
  #       { 
		# "$addFields": {
	 #        "date": {
	 #            "$toDate": "$created_at"
	 #        }
  #   	}
{
    "$match": {
        "tweet.full_text": {
            "$not":  regx
        },
        "tweet.lang":  "pt"
    }
# }
#     {
#         "$match": {
#             "created_at": { 
#                 "$gte": datetime.datetime(2018, 8, 20, 00, 00, 00, 000000),
#                 "$lt": datetime.datetime(2018, 10, 30, 00, 00, 00, 000000)
#             }
#         }     
    # },{ 
    #     "$group": {
    #         "_id": {
    #             "id": "$tweet.id", 
    #             "texto": "$tweet.full_text"
    #         },
    #         "created_at": { "$first": "$created_at"},
    #         "tweet": { "$first": "$tweet"},
    #         "count": { "$sum": 1 }
    #     }
    # },{
    #     "$sort": {
    #         "count": -1
    #     }
    # },{
    #     "$project": {
    #         "_id": 0,
    #         "created_at": 1,
    #         "tweet": 1,
    #         "count": 0
    #     }
    }
]
# newCollection = 'sem_ids_tweets_repetidos'

## trecho que retira os tweets com mesmo texto
# album = banco['teste_clear']
# pipeline = [ { 
#     "$group": {
#         "_id": "$full_text",
#         "id": { "$first": "$id"},
#         "created_at": { "$first": "$created_at"},
#         "count": { "$sum": 1 }
#         }
#     },{
#         "$sort": {
#             "created_at": -1
#         }
#     },{
#         "$project": {
#             "_id": 0,
#             "full_text": "$_id",
#             "created_at": 1,
#             "count": 1,
#             "id": 1
#         }
#     }
# ]
newCollection = 'all_tweets_4'

aggr = album.aggregate(pipeline, allowDiskUse=True)

for tweet in aggr:
#     # newItem = {
#     #     'created_at': tweet.pop('date'),
#     #     'tweet': tweet
#     # }
    print(tweet['tweet']['id'])
    # break
    salvarEmCollection(banco[newCollection], tweet)

# album = banco[newCollection]
# valor = buscaDados(album, {'tweet.id': 1031938574948741125 })

# valor = buscaDados(album, {created_at: { $gte: ISODate("2018-08-20T00:00:00.000Z"),$lt: ISODate("2018-10-30T00:00:00.000Z")}} )
# for e in valor:
# 	print(e['tweet']['full_text'])
	# aux = 
	# salvarEmCollection(album, e['retweeted_status'])
	# if ('retweeted_status' in e):
	# 	print(e['retweeted_status'])
	# 	salvarEmCollection(album, e['retweeted_status'])

	# if ('quoted_status' in e):
	# 	print(e['quoted_status'])
	# 	salvarEmCollection(album, e['quoted_status'])