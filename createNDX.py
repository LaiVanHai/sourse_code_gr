import os, sys, getopt, shutil

def main(argv):
  lstDir = ''
  try:
    opts, args = getopt.getopt(argv,"hi:o:")
  except getopt.GetoptError:
    print 'createNDX.py -i <inputfolder> -o <outputfolder>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'createNDX.py -i <inputfolder> -o <outputfolder>'
      sys.exit()
    elif opt in ("-i"):
      lstDir = arg
    elif opt in ("-o"):
      OutputlstDir = arg

  if (OutputlstDir[len(OutputlstDir) - 1] != "/"): OutputlstDir = OutputlstDir + "/"

  for file in os.listdir(lstDir):
    fileName = file.split(".")[0]
    nameLength = len(fileName)
    startName = nameLength - 5
    if (fileName[startName:nameLength] == "train"):
      outputName = OutputlstDir + fileName.split("t")[0].lower() + ".ndx"
      inputFile = open(lstDir + "/" + file, "r")
      outputFile = open(outputName, "w")
      line = inputFile.readline()
      outputFile.write(fileName.split("t")[0] + "_gmm ")
      while(line != ""):
        outputFile.write(line.rstrip() + " ")
        line = inputFile.readline()
      outputFile.write("\n")
      outputFile.close()
      inputFile.close()

      # shutil.copyfile("./lst/" + file, outFile)

  print("Create all file .NDX and save to ", OutputlstDir)

if __name__ == "__main__":
  main(sys.argv[1:])
