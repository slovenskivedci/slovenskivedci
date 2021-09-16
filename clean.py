import yaml

import glob
countries={}
institutions={}
alllst=[]

from urllib.parse import unquote

 
for y in glob.glob("./people/*.yaml"):
	with open(y) as f:
		dic = yaml.safe_load(f)
		
	 
	#with open(y, 'w') as file:
	#	documents = yaml.dump(dic, file)
	 


