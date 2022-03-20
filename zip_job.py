from os.path import exists
import sys

array=['a','b','b','d']
for x in array:
  f=open(x + ".txt")
  
for x in array:
  if (os.path.exists(x + ".txt") != true):
    print('file doesnt exist - quit script')
    sys.exit(1)
    
      
