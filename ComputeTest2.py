import os
for file in os.listdir("./test_ch"):
  print("Test file " + file)
  os.system("./ComputeTest.exe --config ./cfg/targetTest_ch.cfg --ndxFilename ./test_ch/" + file + " --inputWorldFilename world --outputFilename ./res_ch/" + file.split(".")[0] + ".res");

for file in os.listdir("./test_qh"):
  print("Test file " + file)
  os.system("./ComputeTest.exe --config ./cfg/targetTest_qh.cfg --ndxFilename ./test_qh/" + file + " --inputWorldFilename world --outputFilename ./res_qh/" + file.split(".")[0] + ".res");