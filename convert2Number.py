import os, sys, getopt, shutil

def main(argv):
  inputFileName = ''
  numberFile = 0
  fileArr = [] # mang luu danh sach file
  try:
    opts, args = getopt.getopt(argv,"hn:f:")
  except getopt.GetoptError:
    print 'convert2Number.py -n <file_number> -f <input_file>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'convert2Number.py -n <file_number> -f <input_file>'
      sys.exit()
    elif opt in ("-n"):
      numberFile = arg
    elif opt in ("-f"):
      inputFileName = arg


  inputFile = open(inputFileName, "r")
  saveFile = open("." + inputFileName.split(".")[1] + "_convert2Number.txt", "w")

  line = inputFile.readline()

  arrType = [] # mang luu lan dieu
  sumVal = 0
  curLine = line.split("\t")
  lineLen = len(curLine) - 1
  for i in range(1, lineLen):
    arrType.append(curLine[i])

  saveFile.write(line)

  line = inputFile.readline()
  count = 1

  while(line != ""):
    curLine = line.split("\t")
    sumFile = 0 # luu tong so file dua vao test

    saveFile.write(curLine[0] + "\t")
    sub_lineLen = len(curLine) - 1
    for i in range(1, sub_lineLen):
      value = float(curLine[i]) * float(numberFile)
      saveFile.write("%d \t" %int(value))
      sumFile += int(value)
    saveFile.write(str(sumFile))
    saveFile.write("\n")

    line = inputFile.readline()
    count += 1 # bien duyet ten cac lan dieu

  saveFile.close()
  print("Convert to number successfully save to " + "." + inputFileName.split(".")[1] + "_convert2Number.txt", "w")
if __name__ == "__main__":
  main(sys.argv[1:])