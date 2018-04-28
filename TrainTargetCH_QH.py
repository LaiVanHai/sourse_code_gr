import os
for file in os.listdir("./ndx_ch_qh"):
  os.system("./TrainTarget.exe --config ./cfg/ch_qh_target.cfg --targetIdList ./ndx_ch_qh/" + file + " --inputWorldFilename world --debug false --verbose true");