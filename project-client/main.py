#!/usr/bin/env python

import client

tcp_ip = '127.0.0.1'
tcp_port = 5005
buffersize = 4096
connection = client.Client(tcp_ip, tcp_port, buffersize)
myMessage = ''
listData = []
l = ''

print str(len(listData))

connection.connect()
print "Connection established to " + str(tcp_ip) + ":" + str(tcp_port)
print connection.recieve()

while 1:
    try:
        myMessage = raw_input("Enter the filename: ")
        f = open(myMessage, 'rb')
        break
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)

verboseCount = 1
while 1:
    l = f.read(buffersize)
    if not l:
        break
    listData.append(l)
    print 'Added: ' + str(verboseCount)
    verboseCount += 1

for x in range(0, len(listData)):
    print 'Storlek_' + str(x) + ':' + str(len(listData[x]))

if len(listData) > 0:
    # Send the length of the following data-transmission
    connection.send(str(len(listData)))
    recvData = connection.recieve()

    print "Length: " + str(len(listData))

    # If we received the same length from
    # the server we can begin the data-transmission
    if recvData == str(len(listData)):

        # Send each "block" of data
        for x in range(0, int(recvData)):
            connection.send(listData[x])
            recvData = connection.recieve()
            if recvData != listData[x]:
                print "Not the same data"
                print "Message nr. " + str(x)
                print "Length sent: " + str(len(listData[x]))
                print "Length received: " + str(len(recvData))
                print recvData
                break

        connection.send("End")
        print connection.recieve()
    else:
        print 'Wrong data received: ' + recvData
        print 'Transmission terminated'

f.close()

connection.close()
print "Connection closed"
