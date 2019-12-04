#!/usr/bin/python
import sys,commands, pycurl, StringIO, logging

def curlpage(args):
	response = StringIO.StringIO()
	c=pycurl.Curl()
	c.setopt(c.URL, str(args.strip()))
	#proxy='genproxy.amdocs.com:8080'
	#c.setopt(pycurl.PROXY, "%s" % (proxy))
	c.setopt(c.WRITEFUNCTION, response.write)
	try:
		c.perform()
	except pycurl.error as e:
		print ("Error: "+e)
	output=response.getvalue()
	c.close()
	if not output:
		output=-256
	else:
		output=0
	return output

def validateContainer(url):
	out= curlpage(url)
	return out

def processSteps(url):
	if int(validateContainer(url)) == 0:
		exitcode=0
	else:
		exitcode=-1
	return exitcode

def finalStatus(exitcode):
	exit(exitcode)

try:
	url="http://ilcepoc0590.corp.amdocs.com:9299/"
	exitcode=processSteps(url)
except:
	exitcode=-100
finally:
	finalStatus(exitcode)