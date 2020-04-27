"""
Created on Thu Apr 22 14:32:50 2020

@author: Akanksha
"""

import xmltodict
import os,json

path_to_json = '.'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
print(json_files)
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        jsonString = json.dumps(json_text)
print(jsonString)
xmlString = xmltodict.unparse(json.loads(jsonString), pretty=True)

print('\nXML output(output.xml):')
print(xmlString)

with open('output.xml', 'w') as f:
    f.write(xmlString)


import pyAesCrypt
# encryption/decryption buffer size
bufferSize = 64 * 1024
password = "secret"
# encryption of file output.xml
pyAesCrypt.encryptFile("output.xml", "enoutput.xml.aes", password, bufferSize)
# get encrypted file size

print('\n----------------------------------------------------------------------')
print('\nJson to xml converted file : "output.xml"')
print('\nEncrypted file : "enoutput.xml.aes"')
print('\n----------------------------------------------------------------------')
