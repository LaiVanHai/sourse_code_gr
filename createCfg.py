import os, sys, getopt, shutil

def main(argv):
  lstDir = ''
  try:
    opts, args = getopt.getopt(argv,"hi:")
  except getopt.GetoptError:
    print 'createWorld.py -i <inputfolder>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'createWorld.py -i <inputfolder>'
      sys.exit()
    elif opt in ("-i"):
      lstDir = arg

  OutputlstDir = "./cfg"

  if (OutputlstDir[len(OutputlstDir) - 1] != "/"): OutputlstDir = OutputlstDir + "/"

  for file in os.listdir(lstDir):
    fileName = file.split(".")[0]
    nameLength = len(fileName)
    startName = nameLength - 5
    if (fileName[startName:nameLength] == "train"):
      outputFile1 = OutputlstDir + "target_" + fileName.split("t")[0] + ".cfg"
      outputFile2 = OutputlstDir + "target_" + fileName.split("t")[0] + ".cfg.bak"
      shutil.copyfile("./cfg/target_DEMO.cfg", outputFile1)
      shutil.copyfile("./cfg/target_DEMO.cfg.bak", outputFile2)

  print("Create all file config and save to ", OutputlstDir)

if __name__ == "__main__":
 main(sys.argv[1:])