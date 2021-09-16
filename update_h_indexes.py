
import yaml
import os

import glob

for y in glob.glob("./people/*.yaml"):
	with open(y) as f:
		dic = yaml.safe_load(f)
		print(dic)
		
conf = {"username":"TODO","password":"password"}

with open(r'config/conf.yaml.template', 'w') as file:
		documents = yaml.dump(conf, file)
