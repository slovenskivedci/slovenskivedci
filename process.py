import yaml

import glob
countries={}
institutions={}
alllst=[]
for y in glob.glob("./people/*.yaml"):
	with open(y) as f:
		dic = yaml.safe_load(f)
		if dic['country'] not in countries:
			countries[dic['country']] = []
		if dic['affiliation'] not in institutions:
			institutions[dic['affiliation']] = []
		institutions[dic['affiliation']].append(dic)			
		countries[dic['country']].append(dic)
		alllst.append(dic)
		
		
for k in countries:
	countries[k] = sorted(countries[k],key= lambda e: -int(e['hindex']))
	with open(r'_data/country_%s.yaml'%k.replace(" ","_"), 'w') as file:
			documents = yaml.dump(countries[k], file)		
for k in institutions:
	institutions[k] = sorted(institutions[k],key= lambda e: -int(e['hindex']))		
	with open(r'_data/institution_%s.yaml'%k.replace(" ","_"), 'w') as file:
			documents = yaml.dump(institutions[k], file)		



alllst = sorted(alllst,key= lambda e: -int(e['hindex']))		
with open(r'_data/all.yaml', 'w') as file:
	documents = yaml.dump(alllst, file)


