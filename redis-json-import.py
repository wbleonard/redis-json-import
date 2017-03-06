import json
import redis
from pprint import pprint

r = redis.StrictRedis(host='pub-redis-13418.us-central1-1-1.gce.garantiadata.com', port=13418, db=0)
with open('products.json') as data_file:
    product_data = json.load(data_file)
#pprint(product_data)
pprint(product_data[0]["name"])
#r.set('product_json', product_data[0]["name"])

for idx, name in enumerate(product_data):
	for attribute, value in name.iteritems():
		#print attribute, value
		if attribute == "name":
			#print idx, attribute, value
			#r.set(idx, value)
			r.zadd('products', 0, value)

