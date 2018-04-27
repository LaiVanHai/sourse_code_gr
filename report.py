import os, sys, getopt, shutil

OutputlstDir = "./rpt"
resDir = "./res/"

if (OutputlstDir[len(OutputlstDir) - 1] != "/"): OutputlstDir = OutputlstDir + "/"

# viet danh sach file
saveFile = open(OutputlstDir + "report.txt", "w")
saveFile.write("FileTest\t")
for file in os.listdir("./ndx"):
  fileName = file.split(".")[0]
  saveFile.write(fileName.upper() + "\t")
saveFile.write("\n")
# ---
curName = "" # ten cua file test
curArr = [] # mang luu ket qua
count = 0 # dem so file test
for file in os.listdir("./res"):
  fileName = file.split("-")[0]
  if (curName != fileName):
    if ((len(curArr) > 0) and (curName != "")):
      saveFile.write(curName.upper() + "\t")
      for curVal in curArr:
        value = curVal / float(count)
        saveFile.write("%0.2f \t" %value)
      saveFile.write("\n")
    curName = fileName
    count = 0
    curArr = []

  curInput = open(resDir + file, "r")
  count += 1
  countArr = -1 # bien dung de duyet mang
  line = curInput.readline()
  while(line != ""):
    countArr += 1
    val = line.split(" ")
    if(len(curArr) <= countArr): curArr.append(int(val[2]))
    else:
      if (int(val[2]) == 1): curArr[countArr] += 1

    line = curInput.readline()
  curInput.close()

saveFile.close()

print("Write report successfully and save to ", OutputlstDir)
