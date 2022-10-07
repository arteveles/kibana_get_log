query = {
   "bool": {
      "must": [
         {"match": {"kub_container_name": "proc-server"}},
         {"range": {"@timestamp": {"gte": "now-1440m", "lt": "now"}}}
      ]
   }
}