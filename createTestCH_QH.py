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
      os.system("mkdir " + arg)
      OutputlstDir = arg

  if (OutputlstDir[len(OutputlstDir) - 1] != "/"): OutputlstDir = OutputlstDir + "/"

  for file in os.listdir(lstDir):
    fileName = file.split(".")[0]
    outputFile = open(OutputlstDir + fileName + ".ndx", "w")
    outputFile.write(fileName + " ")
    for file2 in os.listdir("./ndx_ch_qh"):
      fileName2 = file2.split(".")[0]
      outputFile.write(fileName2 + "_gmm ")
    outputFile.write("\n")

    outputFile.close()

  print("Create all file TEST .NDX and save to ", OutputlstDir)

if __name__ == "__main__":
  main(sys.argv[1:])


