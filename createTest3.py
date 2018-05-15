# so sanh phan tram nhan dang theo loai
import os, sys, getopt, shutil

OutputlstDir1 = "./test_ch/"
OutputlstDir2 = "./test_qh/"
lstDir = "./res"
rptDir = "./rpt"
curName = ""
countName = 0

rptFile = open(rptDir + "/" + "report.txt", "r")
lineRpt = rptFile.readline()

for file in os.listdir(lstDir):
  if (file.split("-")[0] != lineRpt.split("\t")[0]): lineRpt = rptFile.readline()
  result = 0
  if (lineRpt.split("_")[0] == "CH"):
    if (float(lineRpt.split("\t")[1]) > 0.5):
      OutputFolder = OutputlstDir1
      ndxFolder = "./ndx_ch"
      result = 1
    else: result = 0
  elif (lineRpt.split("_")[0] == "QH"):
    if (float(lineRpt.split("\t")[2]) > 0.5):
      OutputFolder = OutputlstDir2
      ndxFolder = "./ndx_qh"
      result = 1
    else: result = 0

  if (result == 1):
    fileName = file.split(".")[0]
    outputFile = open(OutputFolder + fileName + ".ndx", "w")
    outputFile.write(fileName + " ")
    for file2 in os.listdir(ndxFolder):
      fileName2 = file2.split(".")[0]
      outputFile.write(fileName2 + "_gmm ")
    outputFile.write("\n")
    outputFile.close()

print("Create all file TEST .NDX successfully!\n")
