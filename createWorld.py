import os, sys, getopt, shutil

OutputlstDir = "./lst"
lstDir = "./lst"

if (OutputlstDir[len(OutputlstDir) - 1] != "/"): OutputlstDir = OutputlstDir + "/"

outputFile = open("./lst/World.lst", "w")
countLine = 0

for file in os.listdir("./lst"):
  fileName = file.split(".")[0]
  nameLength = len(fileName)
  startName = nameLength - 5
  if (fileName[startName:nameLength] == "train"):
    cur_str = "D:\Alize\lst\ " + file
    str_arr = cur_str.split(" ")
    outputFile.write(str_arr[0] + str_arr[1])
    outputFile.write("\n")
    countLine += 1

outputFile.close()

outputFile2 = open("./lst/World.weight", "w")
weight = 1 / float(countLine)
while(countLine != 0):
  outputFile2.write(str(weight))
  outputFile2.write("\n")
  countLine -= 1

outputFile2.close()

print("Create file World.lst and World.weitght successfully and save to ", OutputlstDir)
