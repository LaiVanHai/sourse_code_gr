import os
for file in os.listdir("./ndx"):
  os.system("./TrainTarget.exe --config ./cfg/target.cfg --targetIdList ./ndx/" + file + " --inputWorldFilename world --debug false --verbose true");