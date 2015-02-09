#!/usr/bin/env python

import socket
import sys
from thread import *

TCP_IP = ''
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

print "Server started!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)

print "Listening for connections. Waiting for clients ..."

#Function for handling connections using threads
def clientthread(conn):
	#Send message to the connected client
	conn.send("Welcome to the server. Type something and hit enter\n")

	#infinite loop so that function doesn't terminate and end thread
	while 1:
		#Recieve data from the client
		data = conn.recv(BUFFER_SIZE)
		reply = "OK..." + data
		if not data:
			break

		conn.sendall(reply)

	#Came out of the loop
	#Saves the address and port of the connection in addr
	addr = conn.getpeername()
	conn.close
	print "Connection with " + addr[0] + ":" + str(addr[1]) + " closed"

#Keep talking to the client
while 1:
	conn, addr = s.accept()
	print 'Connection address:' + addr[0] + ":" + str(addr[1])

	#start a new thread takes 1st arg as a function name to be run, second is the tuple of arg to the function
	start_new_thread(clientthread, (conn,))
"""
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    conn.send(data)  # echo
"""
s.close()
