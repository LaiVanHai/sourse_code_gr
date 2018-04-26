import os
for file in os.listdir("./ndx"):
  print "./TrainTarget.exe --config ./cfg/target.cfg --targetIdList ./ndx/" + file + " --inputWorldFilename world --debug false --verbose true"
  os.system("./TrainTarget.exe --config ./cfg/target.cfg --targetIdList ./ndx/" + file + " --inputWorldFilename world --debug false --verbose true");