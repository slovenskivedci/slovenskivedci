

import glob
countries={}
institutions={}
alllst=[]

from urllib.parse import unquote

 
for y in glob.glob("./people/*.yaml"):
	print(y) 
	with open(y) as f:
		dic = yaml.safe_load(f)
		
#	with open("/tmp/test.yaml", 'w') as file:
#	   documents = yaml.dump(dic, file)
#	afsadf
#	with open("./people/"+newname, 'w') as file:
#	   documents = yaml.dump(dic, file)
	 


