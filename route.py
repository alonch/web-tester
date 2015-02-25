from bottle import route, run, view, request
from datetime import datetime
import result
import java
@route('/')
@view('index.html')
def index():
	data = dict()
	data['totalTests'] = 6
	data['students'] = result.load()
	
	return data

@route('/save')
@view('save.html')
def save():
	nick = request.GET.get('nick')
	code = request.GET.get('code')
	java.createFile(nick, code)
	java.copile(nick)
	out = java.run(nick)
	
	data = dict()
	data['output'] = []
	for line in out.split('\n'):
		if ":" not in line:
			continue
		data['output'].append(line.split(':'))

	result.save(nick, data['output'])
	return data

run(host='10.163.101.24', port=4040)