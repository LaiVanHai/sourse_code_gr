import os, sys, getopt, shutil

def main(argv):
  lstDir = ''
  try:
    opts, args = getopt.getopt(argv,"hi:o:n:")
  except getopt.GetoptError:
    print 'createTestCH_QH.py -i <inputfolder> -o <outputfolder> -n <ndxfolder>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'createTestCH_QH.py -i <inputfolder> -o <outputfolder> -n <ndxfolder>'
      sys.exit()
    elif opt in ("-i"):
      lstDir = arg
    elif opt in ("-o"):
      os.system("mkdir " + arg)
      OutputlstDir = arg
    elif opt in ("-n"):
      ndxDir = arg

  if (OutputlstDir[len(OutputlstDir) - 1] != "/"): OutputlstDir = OutputlstDir + "/"

  for file in os.listdir(lstDir):
    fileName = file.split(".")[0]
    outputFile = open(OutputlstDir + fileName + ".ndx", "w")
    outputFile.write(fileName + " ")
    for file2 in os.listdir(ndxDir):
      fileName2 = file2.split(".")[0]
      outputFile.write(fileName2 + "_gmm ")
    outputFile.write("\n")

    outputFile.close()

  print("Create all file TEST .NDX and save to ", OutputlstDir)

if __name__ == "__main__":
  main(sys.argv[1:])


