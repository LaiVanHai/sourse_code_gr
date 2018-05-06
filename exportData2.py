# export data phan theo lan dieu
import os, sys, getopt, shutil

def main(argv):
  InputDir = ''
  try:
    opts, args = getopt.getopt(argv,"hi:f:")
  except getopt.GetoptError:
    print 'exportData1.py -i <inputfolder> -f <fileName>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'exportData1.py -i <inputfolder> -f <fileName>'
      sys.exit()
    elif opt in ("-i"):
      InputDir = arg
    elif opt in ("-f"):
      FileName = arg


  if (InputDir[len(InputDir) - 1] != "/"): InputDir = InputDir + "/"
  inputFile = open(InputDir + FileName, "r")

  line = inputFile.readline()
  arrType = [] # mang luu danh sach lan dieu
  curLine = line.split("\t")
  lineLen = len(curLine) - 1
  for i in range(1, lineLen):
    arrType.append(curLine[i])

  line = inputFile.readline()
  trueNumF = 0 # so lan dieu nhan dung hoan toan
  trueNum = 0 # so lan dieu nhan dung mot phan
  falseNum = 0 # so lan dieu nhan sai
  sumVal = 0 # luu tong so diem cua ket qua
  sumNum = 0 # so lan dieu
  arrTrue = []
  arrFalse = []

  while (line != ""):
    count = -1
    curLine = line.split("\t")
    lineLen = len(curLine) - 1
    sumNum += 1 # dem so lan dieu dau vao
    for i in range(1, lineLen):
      count += 1
      val = float(curLine[i])
      if (curLine[0] == arrType[count]):
        if (val > 0):
          if (val == 1):
            trueNumF += 1
          else:
            trueNum += 1
            arrTrue .append(curLine[0])
          sumVal += val
        else:
          falseNum += 1
          arrFalse.append(curLine[0])
    line = inputFile.readline()

  inputFile.close()
  savefile = open(InputDir + FileName.split(".")[0] + "_export.txt", "w")
  # In ra file ket qua

  savefile.write("So luong lan dieu: " + str(sumNum) + "\n")
  savefile.write("=======================================\n")
  value = sumVal / sumNum
  savefile.write("==> Ty le nhan dung: %0.2f \n" %value)
  savefile.write("So lan dieu nhan DUNG HOAN TOAN: " + str(trueNumF) + "\n")
  savefile.write("So lan dieu nhan DUNG MOT PHAN: " + str(trueNum) + "\n")
  for i in arrTrue:
    savefile.write(i + "\t")
  savefile.write("\n")
  savefile.write("So lan dieu nhan SAI: " + str(falseNum) + "\n")
  for i in arrFalse:
    savefile.write(i + "\t")
  savefile.write("\n")

  savefile.close()
  print("Export file successfully!!!")
if __name__ == "__main__":
  main(sys.argv[1:])