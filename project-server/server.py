#!/usr/bin/env python

import socket
import sys
import datetime
from thread import *
from datetime import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
file_counter = 1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)
print str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " " + "Server started!"

def process():
	global s
	print str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " " + "Listening for connections. Waiting for clients ..."

	#Keep talking to the client
	while 1:
		conn, addr = s.accept()
		print str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ' ' + 'Connection address:' + addr[0] + ":" + str(addr[1])

		#start a new thread takes 1st arg as a function name to be run, second is the tuple of arg to the function
		start_new_thread(clientthread, (conn,))

#Function for handling connections using threads
def clientthread(conn):
	global file_counter
	#Send message to the connected client
	conn.send("Welcome to the server. Type something and hit enter\n")

	f = open('file_' + str(file_counter)+".txt", 'wb')
	file_counter += 1

	#infinite loop so that function doesn't terminate and end thread
	#while 1:
		#Recieve data from the client
		#data = conn.recv(BUFFER_SIZE)

		#If there is no data we break out of the loop
		#if not data:
		#	break

		# While there is data to write, we keep writing to the file
	count = 1
	while 1:
		data = conn.recv(BUFFER_SIZE)
		if not data:
			break
		f.write(data)
		
		print count
		count += 1 
	
	#Saves a reply for the client to recieve
	reply = "Your file has been saved to " + f.name
	f.close
	conn.sendall(reply)

	#Came out of the loop
	#Saves the address and port of the connection in addr
	addr = conn.getpeername()
	conn.close
	print str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " " + "Connection with " + addr[0] + ":" + str(addr[1]) + " closed"

# Begin the thread to handle connections
start_new_thread(process,())

myInput = ""
while myInput != "stop" and myInput != "exit":
	myInput = raw_input("Type stop or exit to close the server\n")
	myInput = myInput.lower()

s.close()
print "socket closed"

"""
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    conn.send(data)  # echo
"""