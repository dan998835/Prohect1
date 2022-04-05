import os
from os.path import exists
import sys
from zipfile import ZipFile
from os.path import basename

def main():
  array=['a','b','c','d']
  dir = format(os.getcwd())
  for x in array:
    f = open(x + ".txt" , 'w')
    f.close()
  for x in array:
    if (not os.path.isfile(str(dir) + str('/') + str(x) + str('.txt'))):
      print('dir =' + str(dir))
      print('file doesnt exist - quit script')
      sys.exit(1)
  version = os.environ['VERSION']
  #version = '1.2.0'#
  for x in array:
    zip_file = ZipFile(x + '_' + version + '.zip', 'w')
    filepath = os.path.join(dir , x + '.txt')
    zip_file.write(filepath , basename(filepath))
    zip_file.close()
  for x in array:
    if (not os.path.isfile( str(x) + str('_') + str(version) + str('.zip'))):
      print('file doesnt exist - quit script')
      sys.exit(1)
main()
