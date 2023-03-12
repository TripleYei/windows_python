import os
import sys

argument = len(sys.argv)

ping = sys.argv[1]
os.system("ping " + ping)