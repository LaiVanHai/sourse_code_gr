import os, sys, getopt, shutil

OutputlstDir = "./test"
lstDir = "./lst"

if (OutputlstDir[len(OutputlstDir) - 1] != "/"): OutputlstDir = OutputlstDir + "/"


for file in os.listdir("./lst"):
  fileName = file.split(".")[0]
  nameLength = len(fileName)
  startName = nameLength - 4

  if (fileName[startName:nameLength] == "test"):
    inputFile = open("./lst/" + file, "r")
    line = inputFile.readline()

    while(line != ""):
      outputFile = open(OutputlstDir + line.rstrip() + ".ndx", "w")
      outputFile.write(line.rstrip() + " ")
      for file2 in os.listdir("./ndx"):
        fileName2 = file2.split(".")[0]
        outputFile.write(fileName2 + "_gmm ")
      outputFile.write("\n")
      outputFile.close()
      line = inputFile.readline()

    inputFile.close()

print("Create all file TEST .NDX and save to ", OutputlstDir)
