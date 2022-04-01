import yaml

import glob
countries={}
institutions={}
alllst=[]

from urllib.parse import unquote

 
for y in glob.glob("./people/*.yaml"):
	person = y.split("/")[2]
	name = person.split("_")[0]
	surname = person.split("_")[1].split(".")[0]
	
	newname = name.upper()[0]+name.lower()[1:]+"_"+surname.upper()[0]+surname.lower()[1:]+".yaml"
	print(newname)
	 
	with open(y) as f:
		dic = yaml.safe_load(f)
	with open(y, 'w') as file:
		documents = yaml.dump([], file)
		

	with open("./people/"+newname, 'w') as file:
	   documents = yaml.dump(dic, file)
	 


