import os, sys, getopt, shutil

def main(argv):
  try:
    opts, args = getopt.getopt(argv,"hi:")
  except getopt.GetoptError:
    print 'NormFeat1_CH_QH.py -i <inputfolder>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'NormFeat1_CH_QH.py -i <inputfolder>'
      sys.exit()
    elif opt in ("-i"):
      InputDir = arg

  for file in os.listdir(InputDir):
    os.system("./NormFeat.exe --config ./cfg/NormFeat_energy_ch_qh.cfg --inputFeatureFilename \""+file.split(".")[0] + "\"");

if __name__ == "__main__":
  main(sys.argv[1:])