# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:50:06 2019

@author: Kish
"""
import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_298754.json'

fhand = urllib.request.urlopen(url).read().decode()
#just read() gives a byte array
#decode() gives us a string

#print(type(fhand))
#print(fhand)

root = json.loads(fhand)

#print(root['comments'])
#print(type(root['comments']))   #its a list of dictionaries

#initializing sum 
s = 0
for d in root['comments']:
    #print(d['count'])
    #print(type(d['count']))
    s += d['count']
        
print(s)