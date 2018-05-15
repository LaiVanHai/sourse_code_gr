# viet report phan theo tung lan dieu
import os, sys, getopt, shutil

def main(argv):
  try:
    opts, args = getopt.getopt(argv,"hc:q:o:")
  except getopt.GetoptError:
    print 'report2.py -c <resfolder_ch> -q <resfolder_qh> -o <output_folder>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'report2.py -c <resfolder_ch> -q <resfolder_qh> -o <output_folder>'
      sys.exit()
    elif opt in ("-c"):
      resCh = arg
    elif opt in ("-q"):
      resQh = arg
    elif opt in ("-o"):
      outputDir = arg + "/"


  # viet danh sach file
  saveFile1 = open(outputDir + "report_ch.txt", "w")
  saveFile2 = open(outputDir + "report_qh.txt", "w")
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
  for file in os.listdir(resCh):
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
      curVal = []

    curInput = open(resCh + "/" + file, "r")
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
    curArr[element_max] += 1 # tang gia tri len mot don vi

    curInput.close()

  saveFile1.write(curName.upper() + "\t")
  for curVal in curArr:
    value = curVal / float(count)
    saveFile1.write("%0.2f \t" %value)
  saveFile1.write("\n")

  saveFile1.close()

  #====
  # ---
  curName = "" # ten cua file test
  curArr = [] # mang luu ket qua
  count = 0 # dem so file test
  for file in os.listdir(resQh):
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
      curVal = []

    curInput = open(resQh + "/" + file, "r")
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

  saveFile2.write(curName.upper() + "\t")
  for curVal in curArr:
    value = curVal / float(count)
    saveFile2.write("%0.2f \t" %value)
  saveFile2.write("\n")

  saveFile2.close()

  print("Write report successfully!")

if __name__ == "__main__":
  main(sys.argv[1:])