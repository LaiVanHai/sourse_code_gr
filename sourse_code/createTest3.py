# so sanh phan tram nhan dang theo loai
import os, sys, getopt, shutil

def main(argv):
  try:
    opts, args = getopt.getopt(argv,"hc:q:r:p:")
  except getopt.GetoptError:
    print 'createTest3.py -c <outputfolder_ch> -q <outputfolder_qh> -r <resfolder> -p <reportfolder>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'createTest3.py -c <outputfolder_ch> -q <outputfolder_qh> -r <resfolder> -p <reportfolder>'
      sys.exit()
    elif opt in ("-c"):
      os.system("mkdir " + arg)
      OutputlstDir1 = arg + "/"
    elif opt in ("-q"):
      os.system("mkdir " + arg)
      OutputlstDir2 = arg + "/"
    elif opt in ("-r"):
      lstDir = arg
    elif opt in ("-p"):
      rptDir = arg

  curName = ""
  countName = 0

  rptFile = open(rptDir + "/" + "report.txt", "r")
  lineRpt = rptFile.readline()

  for file in os.listdir(lstDir):
    if (file.split("-")[0] != lineRpt.split("\t")[0]): lineRpt = rptFile.readline()
    result = 0
    if (lineRpt.split("_")[0] == "CH"):
      if (float(lineRpt.split("\t")[1]) >= 0.5):
        OutputFolder = OutputlstDir1
        ndxFolder = "./ndx_ch"
        result = 1
      else: result = 0
    elif (lineRpt.split("_")[0] == "QH"):
      if (float(lineRpt.split("\t")[2]) >= 0.5):
        OutputFolder = OutputlstDir2
        ndxFolder = "./ndx_qh"
        result = 1
      else: result = 0

    if (result == 1):
      fileName = file.split(".")[0]
      outputFile = open(OutputFolder + fileName + ".ndx", "w")
      outputFile.write(fileName + " ")
      for file2 in os.listdir(ndxFolder):
        fileName2 = file2.split(".")[0]
        outputFile.write(fileName2 + "_gmm ")
      outputFile.write("\n")
      outputFile.close()

  print("Create all file TEST .NDX successfully!\n")

if __name__ == "__main__":
  main(sys.argv[1:])