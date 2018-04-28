import os, sys, getopt, shutil

OutputlstDir1 = "./test_ch/"
OutputlstDir2 = "./test_qh/"
lstDir = "./res"

for file in os.listdir(lstDir):
  inputFile = open(lstDir + "/" + file, "r")
  line1 = inputFile.readline() # doc dong CH
  line2 = inputFile.readline() # doc dong QH
  res1 = line1.split(" ")[2]
  res2 = line2.split(" ")[2]
  name1 = line1.split(" ")[1]
  name2 = line2.split(" ")[3]
  result = 0
  if (res1 != res2):
    name1_1 = line1.split(" ")[1].split("_")[0].upper()
    name1_2 = line1.split(" ")[3].split("_")[0]
    name2_1 = line2.split(" ")[1].split("_")[0].upper()
    name2_2 = line2.split(" ")[3].split("_")[0]
    if ((int(res1) == 1) and (name1_1 == name1_2)):
      OutputFolder = OutputlstDir1
      ndxFolder = "./ndx_ch"
      result = 1

    if ((int(res2) == 1) and (name2_1 == name2_2)):
      OutputFolder = OutputlstDir2
      ndxFolder = "./ndx_qh"
      result = 1

    if (result == 1):
      fileName = file.split(".")[0]
      outputFile = open(OutputFolder + fileName + ".ndx", "w")
      outputFile.write(fileName + " ")
      for file2 in os.listdir(ndxFolder):
        fileName2 = file2.split(".")[0]
        outputFile.write(fileName2 + "_gmm ")
      outputFile.write("\n")
      outputFile.close()

inputFile.close()

print("Create all file TEST .NDX successfully!\n")
