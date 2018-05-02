from pydub import AudioSegment
import os, sys, getopt, shutil

def main(argv):
  t2 = 0
  try:
    opts, args = getopt.getopt(argv,"ht:f:")
  except getopt.GetoptError:
    print 'cutWav.py -t <inputTime> -f <folderSave>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'cutWav.py -t <inputTime> -f <folderSave>'
      sys.exit()
    elif opt in ("-t"):
      t2 = int(arg) * 1000
      extendName = arg
      os.system("mkdir ./lbl/lbl" + arg)
      os.system("mkdir ./lst/lst" + arg)
    elif opt in ("-f"):
      saveFolder = arg
      os.system("mkdir " + arg);
      print("Create save folfer successfully!")

  for file in os.listdir("./wav"):
    name = file.split(".")[0] + ("_")
    t1 = 0
    newAudio = AudioSegment.from_wav("./wav/" + file)
    newAudio = newAudio[t1:t2]
    newAudio.export(saveFolder + "/"+ name + "_" + extendName + ".wav", format="wav")

  print("Cut file Wav successfully! ")
if __name__ == "__main__":
   main(sys.argv[1:])