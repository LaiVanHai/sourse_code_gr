import os, sys, getopt, shutil

OutputlstDir1 = "./lst_ch/"
OutputlstDir2 = "./lst_qh/"
lstDir = "./lst"
for file in os.listdir("./lst"):
  fileName = file.split(".")[0]
  nameLength = len(fileName)
  startName = nameLength - 5
  if (fileName[startName:nameLength] == "train"):
    inputFile = open("./lst/" + file, "r")
    line = inputFile.readline()
    curList = []
    curName = ""

    while(line != ""):
      if (curName == ""): curName = line.split("-")[0]
      if (curName == line.split("-")[0]):
        curList.append(line)
        line = inputFile.readline()
      else:
        if (curName.split("_")[0] == "CH"):
          outputfolder = OutputlstDir1
        else:
          outputfolder = OutputlstDir2

        outputFile = open(outputfolder + curName + "train.lst", "w+")
        listLength = len(curList)
        i0 = 0

        while(i0 < listLength):
          outputFile.write(curList[i0])
          i0 += 1

        outputFile.close()
        curList = []
        curName = ""

    if (curName.split("_")[0] == "CH"):
      outputfolder = OutputlstDir1
    else:
      outputfolder = OutputlstDir2

    outputFile = open(outputfolder + curName + "train.lst", "w+")
    listLength = len(curList)
    i0 = 0

    while(i0 < listLength):
      outputFile.write(curList[i0])
      i0 += 1
    outputFile.close()
  print("Create all file .LST successfully")
