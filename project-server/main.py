#!/usr/bin/env python
import Cserver
import sys
from thread import *

server = Cserver.Server()
response = ""

# Start the server
server.start()
print 'Type stop or kill to kill the server'

# Listen to ports
start_new_thread(server.listen, ())

# Enter stop or exit to stop the server
while 1:
    response = raw_input('')
    if response == 'stop' or response == 'kill':
        break

# Closing the server
server.close()
