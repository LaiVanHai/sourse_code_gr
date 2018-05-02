import os
for file in os.listdir("./prm"):
  print("Running EnergyDetector...")
  os.system("./EnergyDetector.exe --config ./cfg/EnergyDetector.cfg --inputFeatureFilename \""+file.split(".")[0] + "\"");