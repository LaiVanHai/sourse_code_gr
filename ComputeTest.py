import os
for file in os.listdir("./test"):
  print("Test file " + file)
  os.system("./ComputeTest.exe --config ./cfg/targetTest.cfg --ndxFilename ./test/" + file + " --inputWorldFilename world --outputFilename ./res/" + file.split(".")[0] + ".res");