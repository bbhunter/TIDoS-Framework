#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID (Modified version from wascan)
#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework

from re import search,I

def asm(headers,content):
	detect = False
	detect |= search(r'The requested URL was rejected. Please consult with your administrator.',content,I) is not None
	if detect : 
		return "Application Security Manager (F5 Networks)" 
