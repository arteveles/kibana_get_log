from elasticsearch import Elasticsearch


es = Elasticsearch('http://es123.vistgroup.ru:80/')

query = {
   "bool": {
      "must": [
         {"match": {"kub_container_name": "proc-server"}},
         {"range": {"@timestamp": {"gte": "now-500m", "lt": "now"}}}
      ]
   }
}


resp = es.search(index="branches-mirror-2022.09.26", query=query)
#print(resp)

for r in resp['hits']['hits']:
   print(r['_source']['log'])
