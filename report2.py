import os, sys, getopt, shutil

# viet danh sach file
saveFile1 = open("./rpt/" + "report_ch.txt", "w")
saveFile2 = open("./rpt/" + "report_qh.txt", "w")
saveFile1.write("FileTest\t")
saveFile2.write("FileTest\t")
for file in os.listdir("./ndx_ch"):
  fileName = file.split(".")[0]
  saveFile1.write(fileName.upper() + "\t")
saveFile1.write("\n")

for file in os.listdir("./ndx_qh"):
  fileName = file.split(".")[0]
  saveFile2.write(fileName.upper() + "\t")
saveFile2.write("\n")
# ---
curName = "" # ten cua file test
curArr = [] # mang luu ket qua
count = 0 # dem so file test
for file in os.listdir("./res_ch"):
  fileName = file.split("-")[0]
  if (curName != fileName):
    if ((len(curArr) > 0) and (curName != "")):
      saveFile1.write(curName.upper() + "\t")
      for curVal in curArr:
        value = curVal / float(count)
        saveFile1.write("%0.2f \t" %value)
      saveFile1.write("\n")
    curName = fileName
    count = 0
    curArr = []

  curInput = open("./res_ch/" + file, "r")
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

saveFile1.close()

#====
# ---
curName = "" # ten cua file test
curArr = [] # mang luu ket qua
count = 0 # dem so file test
for file in os.listdir("./res_qh"):
  fileName = file.split("-")[0]
  if (curName != fileName):
    if ((len(curArr) > 0) and (curName != "")):
      saveFile2.write(curName.upper() + "\t")
      for curVal in curArr:
        value = curVal / float(count)
        saveFile2.write("%0.2f \t" %value)
      saveFile2.write("\n")
    curName = fileName
    count = 0
    curArr = []

  curInput = open("./res_qh/" + file, "r")
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

saveFile2.close()

print("Write report successfully!")
