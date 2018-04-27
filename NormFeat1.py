import os
for file in os.listdir("./prm"):
  os.system("./NormFeat.exe --config ./cfg/NormFeat_energy.cfg --inputFeatureFilename \""+file.split(".")[0] + "\"");