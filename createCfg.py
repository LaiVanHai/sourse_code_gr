import os, sys, getopt, shutil

OutputlstDir = "./cfg"
lstDir = "./lst"

if (OutputlstDir[len(OutputlstDir) - 1] != "/"): OutputlstDir = OutputlstDir + "/"

for file in os.listdir("./lst"):
  fileName = file.split(".")[0]
  nameLength = len(fileName)
  startName = nameLength - 5
  if (fileName[startName:nameLength] == "train"):
    outputFile1 = OutputlstDir + "target_" + fileName.split("t")[0] + ".cfg"
    outputFile2 = OutputlstDir + "target_" + fileName.split("t")[0] + ".cfg.bak"
    shutil.copyfile("./cfg/target_DEMO.cfg", outputFile1)
    shutil.copyfile("./cfg/target_DEMO.cfg.bak", outputFile2)

print("Create all file config and save to ", OutputlstDir)
