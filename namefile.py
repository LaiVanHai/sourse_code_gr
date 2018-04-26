import os
import shutil
import sys

InputwavtDir = "./wav"
OutputlstDir = "./lst"

if (InputwavtDir[len(InputwavtDir) - 1] != "/"): InputwavtDir = InputwavtDir + "/"
if (OutputlstDir[len(OutputlstDir) - 1] != "/"): OutputlstDir = OutputlstDir + "/"

outFile = open(OutputlstDir + "all.lst", "w")
outFile1 = open(OutputlstDir + "all1.lst", "w")

for file in os.listdir("./wav"):
  outFile.write(file + "\n")
  outFile1.write(file.split(".")[0] + "\n")

outFile.close()
outFile1.close()

print("Create all and all1 file and save to ", OutputlstDir)

