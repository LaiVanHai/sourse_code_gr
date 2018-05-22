import os, sys, getopt, shutil
from time import gmtime, strftime

def main(argv):
  typeTime = ''
  try:
    opts, args = getopt.getopt(argv,"hc:o:")
  except getopt.GetoptError:
    print 'getTime.py -c <typeTime> -o <outputfolder>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'getTime.py -c <typeTime> -o <outputfolder>'
      sys.exit()
    elif opt in ("-c"):
      typeTime = arg
    elif opt in ("-o"):
      OutputDir = arg
      os.system("mkdir " + OutputDir)

  saveFile = open(OutputDir + "/" + "time.txt", "a")
  saveFile.write(typeTime + ":" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
  saveFile.close()

if __name__ == "__main__":
  main(sys.argv[1:])