#! /usr/bin/python

import cgi,cgitb

#cgitb.enable() enables debugging
#cgitb.enable()
login = cgi.FieldStorage()

user = login.getvalue("username")
password = login.getvalue("password")


with open(".security","r") as f:
	name = f.readline().strip("\n")
	word = f.readline().strip("\n")

if user == name and word == password:

	print 'Content-Type: text/html'
	print
	print '<html>'
	print '<head><title>Thanks for submitting!</title></head>'
	print '<body>'
	print '<p> <a href="https://www.google.com">google...</a></p>'
	print '</body>'
	print '</html>'

else:
	print 'Content-Type: text/html'
        print
        print '<html>'
        print '<head><title>Thanks for submitting!</title></head>'
        print '<body>'
        print '<p>incorrect credentials, this incident will be reported</p>'
	print '</body>'
        print '</html>'

