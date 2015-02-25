import subprocess
import os
currentPath = os.path.dirname(os.path.realpath(__file__))
print currentPath
def createFile(name, code):
	filePath = 'output/%s.java' % (name)
	print filePath
	f = open(filePath,'w')
	print code
	f.write(code)
	f.close() 

def copile(name):
	bashCommand = """cd %s/output; 
		javac %s.java""" % (currentPath, name)
	process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
	output = process.communicate()[0]

def run(name):
	bashCommand = """cd %s/output; 
		$JRE_HOME/bin/java Test %s""" % (currentPath, name)
	process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
	output = process.communicate()[0]
	return output