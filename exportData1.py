# export data phan theo loai
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
  arrType = []
  curLine = line.split("\t")
  lineLen = len(curLine) - 1
  for i in range(1, lineLen):
    arrType.append(curLine[i])

  line = inputFile.readline()
  trueNumF_ch = 0 # so lan dieu nhan dung hoan toan
  trueNum_ch = 0 # so lan dieu nhan dung mot phan
  falseNum_ch = 0 # so lan dieu nhan sai
  sumVal_ch = 0 # luu tong so diem cua ket qua
  trueNumF_qh = 0 # so lan dieu nhan dung hoan toan
  trueNum_qh = 0 # so lan dieu nhan dung mot phan
  falseNum_qh = 0 # so lan dieu nhan sai
  sumVal_qh = 0 # luu tong so diem cua ket qua
  chNum = 0 # so lan dieu cheo
  qhNum = 0 # so lan dieu quan ho
  arrTrue_ch = []
  arrFalse_ch = []
  arrTrue_qh = []
  arrFalse_qh = []

  while (line != ""):
    curLine = line.split("\t")
    if (curLine[0].split("_")[0] == "CH"):
      chNum += 1
      val = float(curLine[1])
      if (val == 1):
        trueNumF_ch += 1
      elif (val == 0):
        falseNum_ch += 1
        arrFalse_ch.append(curLine[0])
      elif (val > 0):
        trueNum_ch +=1
        arrTrue_ch.append(curLine[0])
      sumVal_ch += val
    else:
      qhNum += 1
      val = float(curLine[2])
      if (val == 1):
        trueNumF_qh += 1
      elif (val == 0):
        falseNum_qh += 1
        arrFalse_qh.append(curLine[0])
      elif (val > 0):
        trueNum_qh +=1
        arrTrue_qh.append(curLine[0])
      sumVal_qh += val

    line = inputFile.readline()

  inputFile.close()
  savefile = open(InputDir + FileName.split(".")[0] + "_export.txt", "w")
  # In ra file ket qua

  savefile.write("So luong lan dieu cheo: " + str(chNum) + "\n")
  savefile.write("=======================================\n")
  value = sumVal_ch / chNum
  savefile.write("==> Ty le nhan dung: %0.2f \n" %value)
  savefile.write("So lan dieu nhan DUNG HOAN TOAN: " + str(trueNumF_ch) + "\n")
  savefile.write("So lan dieu nhan DUNG MOT PHAN: " + str(trueNum_ch) + "\n")
  for i in arrTrue_ch:
    savefile.write(i + "\t")
  savefile.write("\n")
  savefile.write("So lan dieu nhan SAI: " + str(falseNum_ch) + "\n")
  for i in arrFalse_ch:
    savefile.write(i + "\t")
  savefile.write("\n")

  savefile.write("So luong lan dieu dan ca: " + str(qhNum) + "\n")
  savefile.write("=======================================\n")
  value = sumVal_qh / qhNum
  savefile.write("==> Ty le nhan dung: %0.2f \n" %value)
  savefile.write("So lan dieu nhan DUNG HOAN TOAN: " + str(trueNumF_qh) + "\n")
  savefile.write("So lan dieu nhan DUNG MOT PHAN: " + str(trueNum_qh) + "\n")
  for i in arrTrue_qh:
    savefile.write(i + "\t")
  savefile.write("\n")
  savefile.write("So lan dieu nhan SAI: " + str(falseNum_qh) + "\n")
  for i in arrFalse_qh:
    savefile.write(i + "\t")
  savefile.write("\n")

  savefile.close()
  print("Export file successfully!!!")
if __name__ == "__main__":
  main(sys.argv[1:])