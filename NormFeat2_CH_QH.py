import os, sys, getopt, shutil

def main(argv):
  try:
    opts, args = getopt.getopt(argv,"hi:")
  except getopt.GetoptError:
    print 'EnergyDetector_CH_QH.py -i <inputfolder> -o <outputfolder> -n <ndxFolder>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'EnergyDetector_CH_QH.py -i <inputfolder> -o <outputfolder> -n <ndxFolder>'
      sys.exit()
    elif opt in ("-i"):
      InputDir = arg

  for file in os.listdir(InputDir):
    os.system("./NormFeat.exe  --config ./cfg/NormFeat_ch_qh.cfg --inputFeatureFilename \""+file.split(".")[0] + "\"");

if __name__ == "__main__":
  main(sys.argv[1:])