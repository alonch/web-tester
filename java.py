import subprocess
import os

class File:

	currentPath = os.path.dirname(os.path.realpath(__file__))

	def __init__(self, name, source):
		self.name = name
		self.source = source

	def create(self):
		filePath = 'output/%s.java' % (self.name)
		f = open(filePath,'w')
		f.write(self.source)
		f.close() 

	def copile(self):
		cmd = """cd %s/output; javac %s.java""" % (self.currentPath, self.name)
		output = self.execute(cmd)

	
	def run(self):
		cmd = """cd %s/output; $JRE_HOME/bin/java Test %s""" % (self.currentPath, self.name)
		return self.execute(cmd)

	def execute(self, cmd):
		process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		output, errput = process.communicate()
		if self.hasErrors(errput):
			raise Exception(errput)
		return output

	def hasErrors(self, err):
		return len(err)>0
