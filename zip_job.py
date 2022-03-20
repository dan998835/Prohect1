import os
from os.path import exists
import sys
from zipfile import Zipfile

def main():
  #a
  array=['a','b','b','d']
  #b
  for x in array:
    f=open(x + ".txt")
    f.close()
  #c
  for x in array:
    if (os.path.exists(x + ".txt") != true):
      print('file doesnt exist - quit script')
      sys.exit(1)
  #d
  for x in array:
    zip_file = ZipFile(x + '_' + ENV VERSION + '.zip', 'w')
    zip_file.write(x + '.txt')
    zip_file.close()
  #e 
  for x in array:
    if (os.path.exists(x + '_' + ENV VERSION + ".zip") != true):
      print('file doesnt exist - quit script')
      sys.exit(1)
    
      
