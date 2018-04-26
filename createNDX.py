import os, sys, getopt, shutil

OutputlstDir = "./ndx"
lstDir = "./lst"

if (OutputlstDir[len(OutputlstDir) - 1] != "/"): OutputlstDir = OutputlstDir + "/"


for file in os.listdir("./lst"):
  fileName = file.split(".")[0]
  nameLength = len(fileName)
  startName = nameLength - 5
  if (fileName[startName:nameLength] == "train"):
    outputName = OutputlstDir + fileName.split("t")[0].lower() + ".ndx"
    inputFile = open("./lst/" + file, "r")
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
