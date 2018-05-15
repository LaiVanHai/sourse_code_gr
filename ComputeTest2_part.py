import os, sys, getopt, shutil

def main(argv):
  try:
    opts, args = getopt.getopt(argv,"hc:q:a:b:")
  except getopt.GetoptError:
    print 'ComputeTest2_part.py -i <input_CH> -q <input_QH> -a <output_CH> -b <output_QH>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'ComputeTest2_part.py -i <input_CH> -q <input_QH> -a <output_CH> -b <output_QH>'
      sys.exit()
    elif opt in ("-c"):
      testCh = arg
    elif opt in ("-q"):
      testQh = arg
    elif opt in ("-a"):
      os.system("mkdir " + arg)
      resCh = arg + "/"
    elif opt in ("-b"):
      os.system("mkdir " + arg)
      resQh = arg + "/"

  for file in os.listdir(testCh):
    print("Test file " + file)
    os.system("./ComputeTest.exe --config ./cfg/targetTest_ch_part.cfg --ndxFilename " + testCh + "/" + file + " --inputWorldFilename world --outputFilename " + resCh + file.split(".")[0] + ".res");

  for file in os.listdir(testQh):
    print("Test file " + file)
    os.system("./ComputeTest.exe --config ./cfg/targetTest_qh_part.cfg --ndxFilename " + testQh + "/" + file + " --inputWorldFilename world --outputFilename " + resQh + file.split(".")[0] + ".res");

if __name__ == "__main__":
  main(sys.argv[1:])