#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:43:16 2020

@author: neerajkulshrestha
"""

import json
import xmltodict
import os


os.getcwd()
with open("sample.json", 'r') as f:
    jsonString = f.read()
 
print('JSON input (sample.json):')
print(jsonString)
 
xmlString = xmltodict.unparse(json.loads(jsonString), pretty=True)
 
print('\nXML output(output.xml):')
print(xmlString)
 
with open('output.xml', 'w') as f:
    f.write(xmlString)
