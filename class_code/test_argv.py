#!/usr/bin/env python3

from sys import argv

print("type of argv: %s" % type(argv))
print("length of argv:%d" % len(argv) )
print("content in the argv")

for i in range(len(argv)):
    print("\t %d: %s" % (i,argv[i]))

#for i,el in enumerate(argv):
#    print("\t %d: %s" % (i,el))
