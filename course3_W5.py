# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:30:17 2019

@author: Kish
"""
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_298753.xml'

fhand = urllib.request.urlopen(url).read().decode()
#just read() gives a byte array
#decode() gives us a string

#print(type(fhand))
#print(fhand)

root = ET.fromstring(fhand)

lst = root.findall('comments/comment')
#print(lst)
#print(len(lst))

#initializing sum variable
s = 0

for i in lst:
    s += int(i.find('count').text)
    #print(i.find('count').text)

print(s)
