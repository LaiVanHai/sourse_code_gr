import os, sys, getopt, shutil

def main(argv):
  lstDir = ''
  try:
    opts, args = getopt.getopt(argv,"hi:")
  except getopt.GetoptError:
    print 'createWorld.py -i <inputfolder>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'createWorld.py -i <inputfolder>'
      sys.exit()
    elif opt in ("-i"):
      lstDir = arg

  outputFile = open(lstDir + "/World.lst", "w")
  countLine = 0

  for file in os.listdir(lstDir):
    fileName = file.split(".")[0]
    nameLength = len(fileName)
    startName = nameLength - 5
    if (fileName[startName:nameLength] == "train"):
      cur_str = "D:\Alize\ " + lstDir.split("/")[1] + "\ " + file
      str_arr = cur_str.split(" ")
      outputFile.write(str_arr[0] + str_arr[1] + str_arr[2])
      outputFile.write("\n")
      countLine += 1

  outputFile.close()

  outputFile2 = open(lstDir + "/World.weight", "w")
  weight = 1 / float(countLine)
  while(countLine != 0):
    outputFile2.write(str(weight))
    outputFile2.write("\n")
    countLine -= 1

  outputFile2.close()

  print("Create file World.lst and World.weitght successfully")

if __name__ == "__main__":
  main(sys.argv[1:])