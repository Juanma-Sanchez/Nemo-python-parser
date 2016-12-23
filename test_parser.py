import sys

from nemo_parser import *

Intent = parse_Intent(sys.argv[1])
print Intent.sentences
for node in Intent.objects.nodes:
    print
    print "Node:"
    print node
for con in Intent.objects.connections:
    print
    print "Connection:"
    print con
