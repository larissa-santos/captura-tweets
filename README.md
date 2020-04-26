# captura-tweets
Algoritmo de captura de tweets com uso da biblioteca python-twitter e salva em arquivo `.json` e no Mongo.

Após a captura de tweets, é sugerido um algoritmo que reuni todos os tweets em uma unica collection no Mongo, seguindo os seguintes passos:
- Somente tweets publicados em determinado periodo;
- tweets com language "pt";
- Removendo os tweets com mesmo id, deixando apenas um;
- Removendo os retweets, deixando apenas os tweets originais;
- Adicionando um contador no tweets original para cada retweet removido; 
