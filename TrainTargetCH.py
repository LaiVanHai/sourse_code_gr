import os
for file in os.listdir("./ndx_ch"):
  os.system("./TrainTarget.exe --config ./cfg/ch_target.cfg --targetIdList ./ndx_ch/" + file + " --inputWorldFilename world --debug false --verbose true");