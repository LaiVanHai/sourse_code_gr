import os
# os.system("python feature_calculate.py"); # trich chon dac trung
# os.system("python NormFeat1.py"); # chuan hoa lan 1
# os.system("python EnergyDetector1.py"); # danh dau nhung doan co tieng noi
# os.system("python NormFeat2.py"); # chuan hoa lan 2
# os.system("python namefile.py"); # tao danh sach file wav
# os.system("python DataSplit.py -i all1.lst -o ./lst -p 5 -t 1"); # chia phan de train va test
os.system("python createWorld.py"); # tao file config World.lst va World.weight
os.system("./TrainWorld.exe --config ./cfg/TrainWorldInit.cfg --inputStreamList ./lst/world.lst --weightStreamList ./lst/world.weight --outputWorldFilename world_init --debug false --verbose true"); # tao 2 file
os.system("./TrainWorld.exe --config ./cfg/TrainWorldFinal.cfg --inputStreamList ./lst/world.lst --weightStreamList ./lst/world.weight --outputWorldFilename world --inputWorldFilename world_init --debug false --verbose true");
# tao file world.gmm
os.system("python createNDX.py");
os.system("python createCfg.py"); # tao file config
os.system("python TrainTarget.py"); # train
os.system("python createTest.py"); # tao file test
os.system("python ComputeTest.py"); # test
os.system("python report.py"); # tao file bao cao