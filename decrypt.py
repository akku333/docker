"""
Created on Wed Apr 22 16:26:15 2020

@author: Akanksha
"""


import pyAesCrypt

bufferSize = 64 * 1024
password = "secret"
# decryption of file enoutput.xml.aes

pyAesCrypt.decryptFile("enoutput.xml.aes", "dfinaloutput.xml", password, bufferSize)

print('\n----------------------------------------------------------------------')
print('\nFinal file after decryption:',"dfinaloutput.xml")
print('\n----------------------------------------------------------------------')
