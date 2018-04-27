import os, sys, getopt, shutil

def main(argv):
  inputfile = ''
  outputfolder = ''
  allpart = 0
  testpart = 0
  try:
    opts, args = getopt.getopt(argv,"hi:o:p:t:")
  except getopt.GetoptError:
    print 'DataSplit.py -i <inputfile> -o <outputfolder> -p <allpart> -t <testpart>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'DataSplit.py -i <inputfile> -o <outputfolder> -p <allpart> -t <testpart>'
      sys.exit()
    elif opt in ("-i"):
      inputfile = arg
    elif opt in ("-o"):
      outputfolder = arg
    elif opt in ("-p"):
      allpart = arg
    elif opt in ("-t"):
      testpart = arg

  lstDir = "./lst"

  if (lstDir[len(lstDir) - 1] != "/"): lstDir = lstDir + "/"
  if (outputfolder[len(outputfolder) - 1] != "/"): outputfolder = outputfolder + "/"

  inputFile = open(lstDir + "all1.lst", "r")

  line = inputFile.readline()
  curList = []
  curName = ""

  while(line != ""):
    if (curName == ""): curName = line.split("-")[0]
    if (curName == line.split("-")[0]):
      curList.append(line)
      line = inputFile.readline()
    else:
      outputFile = open(outputfolder + curName + "train.lst", "w+")
      outputFile2 = open(outputfolder + curName + "test.lst", "w+")
      listLength = len(curList)
      count = listLength / float(allpart)
      i0 = 0
      testStart = count * (float(testpart) - 1)
      testEnd = count * float(testpart) - 1


      while(i0 < listLength):
        if ((i0 >= testStart) and (i0 <= testEnd)):
          outputFile2.write(curList[i0])
        else:
          outputFile.write(curList[i0])
        i0 += 1

      outputFile.close()
      outputFile2.close()
      curList = []
      curName = ""

  outputFile = open(outputfolder + curName + "train.lst", "w+")
  outputFile2 = open(outputfolder + curName + "test.lst", "w+")
  listLength = len(curList)
  count = listLength / float(allpart)
  i0 = 0
  testStart = count * (float(testpart) - 1)
  testEnd = count * float(testpart) - 1

  print testStart
  print testEnd

  while(i0 < listLength):
    if ((i0 >= testStart) and (i0 <= testEnd)):
      outputFile2.write(curList[i0])
    else:
      outputFile.write(curList[i0])
    i0 += 1

  outputFile.close()
  outputFile2.close()

  print("Data split successfully and save to ", outputfolder)

  # print 'Input file is :', inputfile
  # print 'Output file is :', outputfolder
  # print 'All part is :', allpart
  # print 'Test part: ', testpart

if __name__ == "__main__":
   main(sys.argv[1:])