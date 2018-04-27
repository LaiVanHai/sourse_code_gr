import os
for file in os.listdir("./ndx_qh"):
  os.system("./TrainTarget.exe --config ./cfg/qh_target.cfg --targetIdList ./ndx_qh/" + file + " --inputWorldFilename world --debug false --verbose true");