#By Ronald Liu 01/02/2019

#import socket module
from socket import *

import sys # In order to terminate the program


print ( 'get\n' )

s = socket(AF_INET, SOCK_STREAM)
	
s.connect( (sys.argv[1], int(sys.argv[2]) ) )
	
#list = ["GET /", sys.argv[3], "HTTP/1.1\r\n\r\n"]
	#message = "".join('GET /')
	#message = message.join(sys.argv[3])
	#message = message.join(' HTTP/1.1/')
line = "GET /"+sys.argv[3]+" HTTP/1.1\r\n\r\n"

s.send(line)
	
data = s.recv(1024)

print( 'Received from server: ' + str(data) )
	
s.close()

