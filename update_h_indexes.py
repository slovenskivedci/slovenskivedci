
import yaml
import os

import glob

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


 
