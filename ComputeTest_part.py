# test phan theo the loai cua file da cat
import os, sys, getopt, shutil

def main(argv):
  try:
    opts, args = getopt.getopt(argv,"hi:o:")
  except getopt.GetoptError:
    print 'ComputeTest_part.py -i <inputfolder> -o <outputfolder>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'ComputeTest_part.py -i <inputfolder> -o <outputfolder>'
      sys.exit()
    elif opt in ("-i"):
      InputDir = arg
    elif opt in ("-o"):
      os.system("mkdir " + arg)
      OutputDir = arg

  for file in os.listdir(InputDir):
    print("Test file " + file)
    os.system("./ComputeTest.exe --config ./cfg/targetTest_part.cfg --ndxFilename " + InputDir + "/" + file + " --inputWorldFilename world --outputFilename " + OutputDir + "/" + file.split(".")[0] + ".res");

if __name__ == "__main__":
  main(sys.argv[1:])
