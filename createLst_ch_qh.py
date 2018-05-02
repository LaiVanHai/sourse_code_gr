import os, sys, getopt, shutil

OutputlstDir = "./lst_ch_qh/"
lstDir = "./lst/"

inputFile = open(lstDir + "all1.lst", "r")

line = inputFile.readline()
curList = []
curName = ""

while(line != ""):
  if (curName == ""): curName = line.split("-")[0]
  if (curName == line.split("-")[0]):
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

i0 = 0
listLength = len(curList)
while(i0 < listLength):
  outputFile.write(curList[i0])
  i0 += 1

outputFile.close()
print("Create all file .LST successfully save to ./lst_ch_qh")
