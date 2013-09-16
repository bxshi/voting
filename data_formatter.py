#!/usr/bin/python2.6
import sys
print sys.argv[1]
fi = open(sys.argv[1],'r+')

data = fi.read().replace("[","").replace("]","")
fi.write(data)
fi.close()
