import os, sys, getopt, shutil

def main(argv):
  try:
    opts, args = getopt.getopt(argv,"hi:o:")
  except getopt.GetoptError:
    print 'feature_caculate_CH_QH.py -i <inputfolder> -o <outputfolder> -n <ndxFolder>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'feature_caculate_CH_QH.py -i <inputfolder> -o <outputfolder> -n <ndxFolder>'
      sys.exit()
    elif opt in ("-i"):
      InputDir = arg
    elif opt in ("-o"):
      os.system("mkdir " + arg)
      OutputDir = arg

  for file in os.listdir(InputDir):
    os.system("./sfbcep.exe -F PCM16 -f 16000 -p 19 -e -D -A \"" + InputDir + "/" + file + "\" \"" + OutputDir + "/" + file.split(".") [0] + ".prm\"");

if __name__ == "__main__":
  main(sys.argv[1:])