import yaml
import os

import glob
countries={}
institutions={}
alllst=[]


os.system("rm country_*")
os.system("rm affiliation_*")
os.system("rm _data/*yaml")


import unicodedata

def repl(text):
	return unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('UTF-8').replace(",","_")

for y in glob.glob("./people/*.yaml"):
	with open(y) as f:
		dic = yaml.safe_load(f)
		if dic['country'] not in countries:
			countries[dic['country']] = []
		if dic['affiliation'] not in institutions:
			institutions[dic['affiliation']] = []
		dic["countryurl"]=repl(dic["country"].replace(" ","_"))
		dic["affiliationurl"]=repl(dic["affiliation"].replace(" ","_"))
		
		institutions[dic['affiliation']].append(dic)			
		countries[dic['country']].append(dic)
		alllst.append(dic)
		
	
for k in countries:
	countries[k] = sorted(countries[k],key= lambda e: -int(e['hindex']))
	countrycode = repl(k.replace(" ","_"))
	with open(r'_data/country_%s.yaml'%countrycode, 'w') as file:
			documents = yaml.dump(countries[k], file)	

	os.system("sed 's/DATAFILE/country_%s/g' template.style > country_%s.html"%(countrycode,countrycode))
	
			
			
				
for k in institutions:
	institutions[k] = sorted(institutions[k],key= lambda e: -int(e['hindex']))		
	affcode = repl(k.replace(" ","_"))
	print(affcode)
	 
	with open(r'_data/institution_%s.yaml'%affcode, 'w') as file:
			documents = yaml.dump(institutions[k], file)		
	os.system("sed 's/DATAFILE/institution_%s/g' template.style > affiliation_%s.html"%(affcode,affcode))

os.system("sed 's/DATAFILE/all/g' template.style > index.html")


alllst = sorted(alllst,key= lambda e: -int(e['hindex']))		
with open(r'_data/all.yaml', 'w') as file:
	documents = yaml.dump(alllst, file)


