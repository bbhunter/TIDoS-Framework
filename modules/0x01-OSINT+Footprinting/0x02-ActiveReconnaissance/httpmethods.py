#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID
#This module requires TIDoS Framework
#https://github.com/theInfectedDrake/TIDoS-Framework

import httplib
import time
from colors import *

def httpmethods(web):

	try:
		print R+'\n    ========================='
		print R+'     H T T P   M E T H O D S '
		print R+'    =========================\n'

		print GR+' [*] Parsing Url...'
		time.sleep(0.7)
		web = web.replace('https://','')
		web = web.replace('http://','')
		print O+' [!] Making the connection...'
		conn = httplib.HTTPConnection(web)
		conn.request('OPTIONS','/')
		response = conn.getresponse()
		q = str(response.getheader('allow'))
		if 'None' not in q:
			print G+' [+] The following HTTP methods are allowed...'
			methods = q.split(',')
			for method in methods:
				print O+'     '+method
		else:
			print R+' [-] HTTP Method Options Request Unsuccessful...'

	except Exception as e:
		print R+' [-] Exception Encountered!'
		print R+' [-] Error : '+str(e)
 
