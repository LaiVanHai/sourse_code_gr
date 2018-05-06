import os, sys, getopt, shutil

def main(argv):
  try:
    opts, args = getopt.getopt(argv,"hi:o:n:")
  except getopt.GetoptError:
    print 'report_CH_QH.py -i <inputfolder> -o <outputfolder> -n <ndxFolder>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'report_CH_QH.py -i <inputfolder> -o <outputfolder> -n <ndxFolder>'
      sys.exit()
    elif opt in ("-i"):
      resDir = arg
    elif opt in ("-o"):
      os.system("mkdir " + arg)
      OutputlstDir = arg
    elif opt in ("-n"):
      ndxDir = arg

  if (OutputlstDir[len(OutputlstDir) - 1] != "/"): OutputlstDir = OutputlstDir + "/"

  # viet danh sach file
  saveFile = open(OutputlstDir + "report.txt", "w")
  saveFile.write("FileTest\t")
  for file in os.listdir(ndxDir):
    fileName = file.split(".")[0]
    saveFile.write(fileName.upper() + "\t")
  saveFile.write("\n")
  # ---
  curName = "" # ten cua file test
  curArr = [] # mang luu ket qua
  count = 0 # dem so file test
  for file in os.listdir(resDir):
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
      curVal = []

    curInput = open(resDir + "/" + file, "r")
    count += 1
    countArr = -1 # bien dung de duyet mang
    line = curInput.readline()

    while(line != ""):
      countArr += 1
      val = line.split(" ")
      if(len(curArr) <= countArr):
        curVal.append(float(val[4].rstrip()))
        curArr.append(0)
      else:
        curVal.append(float(val[4].rstrip()))
      line = curInput.readline()

    sub_count = -1
    element_max = 0
    max_val = 0
    for cur in curVal: # tim ra phan tu co gia tri lon nhat
      sub_count += 1
      if (cur > max_val):
        max_val = cur
        element_max = sub_count
    curVal = []
    if (max_val > 0) : curArr[element_max] += 1 # tang gia tri len mot don vi

    curInput.close()

  saveFile.write(curName.upper() + "\t")
  for curVal in curArr:
    value = curVal / float(count)
    saveFile.write("%0.2f \t" %value)
  saveFile.write("\n")

  saveFile.close()

  print("Write report successfully and save to ", OutputlstDir)

if __name__ == "__main__":
  main(sys.argv[1:])

