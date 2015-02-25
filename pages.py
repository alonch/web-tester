import result, java
from bottle import request
import sys

class Index:

	totalTests = 6

	def __init__(self):
		self.students = result.load()

class Save:

	def __init__(self):
		self.loadData()
		self.process()
		

	def process(self):
		try:
			self.processCode()
			self.processOutput()
			result.save(self.nick, self.rawOutput)	
		except Exception as ex:
			self.rawOutput=str(ex)

	def loadData(self):
		self.nick = request.GET.get('nick')
		self.code = request.GET.get('code')

	def processCode(self):
		javaFile = java.File(self.nick, self.code)
		javaFile.create()
		self.rawOutput = javaFile.copile()
		self.rawOutput = javaFile.run()
		
	def processOutput(self):
		self.output = []
		for line in self.rawOutput.split('\n'):
			if ":" not in line:
				continue
			self.output.append(line.split(':'))
		self.rawOutput = None