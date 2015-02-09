#!/usr/bin/env python

import socket
import sys
import datetime
from datetime import *
from thread import *


class Server(object):

    def __init__(self, verboseMode=0):
        self.TCP_IP = ''
        self.TCP_PORT = 5005
        self.BUFFER_SIZE = 4096
        self.file_counter = 1
        self.verbose = verboseMode

    # --------------------------Helper-functions
    def currentTime(self):
        return str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def start(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.TCP_IP, self.TCP_PORT))
        self.s.listen(10)
        current = self.currentTime()
        print current + " Server started!"

    def listen(self):

        def clientthread(conn):
            welcomeMessage = 'Welcome to the server!'
            welcomeMessage += ' Your connection is now ready to be used!\n'
            conn.sendall(welcomeMessage)

            # Recieve length of following transmission
            data = conn.recv(self.BUFFER_SIZE)
            # Send back a confirmation
            conn.sendall(data)

            # If no data was recieved we raise an exception
            if not data:
                raise Exception('No data recieved')

            # If we received a length we start receiving the transmission
            if data > 0:
                length = int(data)

                f = open('file_' + str(self.file_counter) + '.txt', 'wb')
                self.file_counter += 1

                # For verbose purpose
                print 'Length: ' + str(length)

                for x in range(0, length):
                    data = conn.recv(self.BUFFER_SIZE)
                    print "Length received: " + str(len(data))
                    f.write(data)

                    conn.sendall(data)
                    print str(x)

                # Saves a reply for the client to receive
                reply = "Your file has been saved to " + f.name
                f.close
                conn.sendall(reply)

            # Close the connection and print out message
            addr = conn.getpeername()
            conn.close()
            print self.currentTime() + " Connection with " + \
                addr[0] + ":" + str(addr[1]) + " closed"
        # End Clientthread()

        def process():

            print self.currentTime() + " Listening for connections"

            while 1:
                conn, addr = self.s.accept()
                print self.currentTime() + " Connection address:" + \
                    addr[0] + ":" + str(addr[1])

                # Start a thread with the connection
                start_new_thread(clientthread, (conn,))
        # End of Process()

        # Start the process
        start_new_thread(process, ())

    def close(self):
        self.s.close()
        print self.currentTime() + " Socket closed"
