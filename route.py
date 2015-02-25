from bottle import route, run, view, request
from datetime import datetime
import pages

@route('/')
@view('index.html')
def index():
	return {'page':pages.Index()}

@route('/save')
@view('save.html')
def save():
	return {'page':pages.Save()}

run(host='localhost', port=4040)