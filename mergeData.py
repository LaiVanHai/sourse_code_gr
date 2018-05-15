import os, sys, getopt, shutil

def main(argv):
  InputDir = ''
  fileArr = [] # mang luu danh sach file
  try:
    opts, args = getopt.getopt(argv,"hi:")
  except getopt.GetoptError:
    print 'mergeData.py -i <inputfolder>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'mergeData.py -i <inputfolder>'
      sys.exit()
    elif opt in ("-i"):
      InputDir = arg

  for file in os.listdir(InputDir):
    fileArr.append(InputDir + "/" + file)

  file0 = open(fileArr[0], "r")
  file1 = open(fileArr[1], "r")
  file2 = open(fileArr[2], "r")
  file3 = open(fileArr[3], "r")
  file4 = open(fileArr[4], "r")

  saveFile = open(InputDir + "/mergeData.txt", "w")

  line0 = file0.readline()
  line1 = file1.readline()
  line2 = file2.readline()
  line3 = file3.readline()
  line4 = file4.readline()

  arrType = [] # mang luu lan dieu
  sumVal = 0
  curLine = line0.split("\t")
  lineLen = len(curLine) - 1
  for i in range(1, lineLen):
    arrType.append(curLine[i])

  saveFile.write(line0)

  line0 = file0.readline()
  line1 = file1.readline()
  line2 = file2.readline()
  line3 = file3.readline()
  line4 = file4.readline()
  count = -1
  arrVal = []

  while((line0 != "") or (line1 != "") or (line2 != "") or (line3 != "") or (line4 != "")):
    if (line0 != ""): curLine0 = line0.split("\t")
    if (line1 != ""): curLine1 = line1.split("\t")
    if (line2 != ""): curLine2 = line2.split("\t")
    if (line3 != ""): curLine3 = line3.split("\t")
    if (line4 != ""): curLine4 = line4.split("\t")
    count += 1 # bien duyet ten cac lan dieu
    lineLen = len(curLine0) - 1
    for i in range(1, lineLen):
      arrVal.append(0)

    if (curLine0[0] == arrType[count]):
      lineLen = len(curLine0) - 1
      subCount = -1
      for i in range(1, lineLen):
        subCount += 1
        arrVal[subCount] += float(curLine0[i])
      line0 = file0.readline()

    if (curLine1[0] == arrType[count]):
      lineLen = len(curLine1) - 1
      subCount = -1
      for i in range(1, lineLen):
        subCount += 1
        arrVal[subCount] += float(curLine1[i])
      line1 = file1.readline()

    if (curLine2[0] == arrType[count]):
      lineLen = len(curLine2) - 1
      subCount = -1
      for i in range(1, lineLen):
        subCount += 1
        arrVal[subCount] += float(curLine2[i])
      line2 = file2.readline()

    if (curLine3[0] == arrType[count]):
      lineLen = len(curLine3) - 1
      subCount = -1
      for i in range(1, lineLen):
        subCount += 1
        arrVal[subCount] += float(curLine3[i])
      line3 = file3.readline()

    if (curLine4[0] == arrType[count]):
      lineLen = len(curLine4) - 1
      subCount = -1
      for i in range(1, lineLen):
        subCount += 1
        arrVal[subCount] += float(curLine4[i])
      line4 = file4.readline()

    saveFile.write(arrType[count] + "\t")
    sumVal += arrVal[count] / 5
    for val in arrVal:
      value = val / 5
      saveFile.write("%0.2f \t" %value)
    saveFile.write("\n")
    arrVal = []

  avgVal = sumVal / len(arrType)
  saveFile.write("Ket qua nhan dang trung binh %0.2f \n" %avgVal)
  saveFile.close()
  print("Merge file successfully!!!")
if __name__ == "__main__":
  main(sys.argv[1:])