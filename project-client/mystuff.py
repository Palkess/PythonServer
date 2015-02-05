#!/usr/bin/env python
l = []

while 1:
    try:
        myMessage = raw_input("Enter the filename: ")
        f = open(myMessage, 'rb')
        break
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)

while 1:
	x = f.read(4096)
	if not x:
		break
	l.append(x)
	print x

print len(l)