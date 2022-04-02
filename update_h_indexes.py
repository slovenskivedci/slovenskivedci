
import oyaml as yaml
import os
from serpapi import GoogleSearch
import glob
import pickle 
from datetime import datetime


for y in glob.glob("./config/conf.yaml"):
	with open(y) as f: conf = yaml.safe_load(f)


people=[]
for y in glob.glob("./people/*.yaml"):
	with open(y) as f:
		dic = yaml.safe_load(f)
		if "last_update" not in dic:
			dic["last_update"]="2020-12-31"
			with open(y, 'w') as file:
			   documents = yaml.dump(dic, file)
		people.append([y,dic])
		
people = sorted(people, key = lambda kv: kv[1]["last_update"])

for kv in people: # we start updating the last updated person
	y, dic = kv
	try:
		print(y,dic)
		url = dic["scholar"]
		print("URL",url)
		id = url.split("user=")[1][:12]
		print("--------------------------")
		print(y)
		print(dic)
		params = {
		  "engine": "google_scholar_author",
		  "author_id": id,
		  "api_key": conf["key"]
		}

		search = GoogleSearch(params)
		results = search.get_dict()
		
		print(results)
		
		author = results['author']
		

		cited_by = results["cited_by"]["table"]
		for e in cited_by:
			if "h_index" in e:
				
				dic["hindex"] = e["h_index"]["all"]
				if int(dic["hindex"]) < 25:
					
					print(y)
					print(cited_by)
					pickle.dump(results,open("/tmp/debug.pkl","wb"))
					
					print("error", y); die
				#dic["cited_by"] = cited_by
				print("\n\n processing....")
				print(y, dic["hindex"])
				dic["last_update"] = datetime.today().strftime('%Y-%m-%d')
				with open(y, 'w') as file:
				   documents = yaml.dump(dic, file) 
				#print(dic)

	except:
		print("erro",y)
 
