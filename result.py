import json
filePath = 'results/database'
def save(name, data):
	database = load()
	database[name] = data
	
	f = open(filePath,'w')
	f.write(json.dumps(database))
	f.close()

def load():
	f = open(filePath,'r')
	data = json.loads(f.read())
	f.close()
	return data
	