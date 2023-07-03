
import oyaml as yaml
import os
#from serpapi import GoogleSearch
import glob
import pickle 
from datetime import datetime





import requests

 

for y in glob.glob("./config/conf.yaml"):
	with open(y) as f: conf = yaml.safe_load(f)


 
payload = {'api_key': conf['apikey'],
  'url': 'URL'}
  

def getHIndex(resp):
	data = resp
	dat = data.split("h-index</a></td><td class=")[1]
	dat = dat.split(">")[1]
	dat = dat.split("<")[0]
	return dat







 



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
		print("\n\n processing....")
		print("BEFORE",y, dic["hindex"])
		url = dic["scholar"]
		
		
		if "hl=en&amp;" in url:
			print('ccccccc',url)
			url = url.replace("hl=en&amp;","hl=en&")  
			
		if "&amp;hl=sk" in url:
			print('ccccccc',url)
			url = url.replace("&amp;hl=sk","&hl=en")  
		if "hl=sk&amp;" in url:
			print('ccccccc',url)
			url = url.replace("hl=sk&amp;","hl=en&")  
				
		if "hl=" not in url:
			url = url+"&hl=en"
			
			
		
		payload['url']=url
		resp = requests.get('http://api.scraperapi.com', params=payload)
		resp = resp.text
		 
		
		hindex = int(getHIndex(resp))
		
		print("AFTER",y, hindex)
		 
		
		dic["hindex"] =  hindex
		if  dic["hindex"] < 25:
					
					print(y)
					print(hindex)
					pickle.dump(results,open("/tmp/debug.pkl","wb"))
					print(payload)
					print("error", y); die		
		
		
		
		 
		dic["last_update"] = datetime.today().strftime('%Y-%m-%d')
		
		 
	 
		with open(y, 'w') as file:
			documents = yaml.dump(dic, file) 
		 
		
	except:
		print("erro",y)
		print(resp)
		print("\n\n")
		print(url)
		
		afdafa
 
'''
				
				print(dic)
				afafafsafsafsas
'''
	
