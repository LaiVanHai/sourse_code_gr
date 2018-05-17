import os, sys, getopt, shutil

def main(argv):
  try:
    opts, args = getopt.getopt(argv,"ho:")
  except getopt.GetoptError:
    print 'createLst_part.py -o <outputfolder>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'createLst_part.py -o <outputfolder>'
      sys.exit()
    elif opt in ("-o"):
      OutputlstDir = arg

  lstDir = "./lst/"
  if (OutputlstDir[len(OutputlstDir) - 1] != "/"): OutputlstDir = OutputlstDir + "/"

  inputFile = open(lstDir + "all1.lst", "r")

  line = inputFile.readline()
  curList = []
  curName = ""

  while(line != ""):
    if (curName == ""): curName = line.split("_")[0]
    if (curName == line.split("_")[0]):
      curList.append(line)
      line = inputFile.readline()
    else:
      outputFile = open(OutputlstDir + curName + "train.lst", "w+")
      listLength = len(curList)
      i0 = 0
      while(i0 < listLength):
        outputFile.write(curList[i0])
        i0 += 1

      curList = []
      curName = ""
      outputFile.close()

  outputFile = open(OutputlstDir + curName + "train.lst", "w+")
  i0 = 0
  listLength = len(curList)
  while(i0 < listLength):
    outputFile.write(curList[i0])
    i0 += 1

  outputFile.close()
  print("Create all file .LST successfully save to " + OutputlstDir)

if __name__ == "__main__":
  main(sys.argv[1:])