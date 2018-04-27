import os, sys, getopt, shutil

OutputlstDir = "./lst_g"
lstDir = "./lst/"

if (OutputlstDir[len(OutputlstDir) - 1] != "/"): OutputlstDir = OutputlstDir + "/"

outputFile = open(OutputlstDir + "all1.lst", "w")

for file in os.listdir("./lst"):
  fileName = file.split(".")[0]
  nameLength = len(fileName)
  startName = nameLength - 5
  if (fileName[startName:nameLength] == "train"):
    inputFile = open(lstDir + file, "r")
    line = inputFile.readline()
    while(line != ""):
      outputFile.write(line)
      line = inputFile.readline()
    inputFile.close()

outputFile.close()

print("Merge file CHtrain and QHtrain successfully to all1.lst in ", OutputlstDir)
