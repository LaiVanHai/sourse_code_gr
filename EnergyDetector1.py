import os
for file in os.listdir("./prm"):
  print("21313212133")
  os.system("./EnergyDetector.exe --config ./cfg/EnergyDetector.cfg --inputFeatureFilename \""+file.split(".")[0] + "\"");