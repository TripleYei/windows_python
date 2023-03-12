import os
import sys

argument = len(sys.argv)

dns = sys.argv[1]
os.system("nslookup " + dns)