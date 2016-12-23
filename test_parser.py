import sys

from nemo_parser import *

Intent = parse_Intent(sys.argv[1])
print Intent.sentences
