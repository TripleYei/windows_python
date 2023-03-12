import os
import sys

argument = len(sys.argv)

url = sys.argv[1]

print("url : " , url)
os.system("start chrome  " + url )