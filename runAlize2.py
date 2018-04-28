import os
os.system("python createLst.py"); # tao ra file cho 2 thu muc lst_ch va lst_qh
os.system("python createWorld.py -i ./lst_ch"); # tao file config World.lst va World.weight
os.system("python createWorld.py -i ./lst_qh")
os.system("./TrainWorld.exe --config ./cfg/TrainWorldInit_ch.cfg --inputStreamList ./lst_ch/world.lst --weightStreamList ./lst_ch/world.weight --outputWorldFilename world_init --debug false --verbose true"); # tao 2 file
os.system("./TrainWorld.exe --config ./cfg/TrainWorldInit_qh.cfg --inputStreamList ./lst_qh/world.lst --weightStreamList ./lst_qh/world.weight --outputWorldFilename world_init --debug false --verbose true"); # tao 2 file
os.system("./TrainWorld.exe --config ./cfg/TrainWorldFinal_ch.cfg --inputStreamList ./lst_ch/world.lst --weightStreamList ./lst_ch/world.weight --outputWorldFilename world --inputWorldFilename world_init --debug false --verbose true");
# tao file world.gmm
os.system("./TrainWorld.exe --config ./cfg/TrainWorldFinal_qh.cfg --inputStreamList ./lst_qh/world.lst --weightStreamList ./lst_qh/world.weight --outputWorldFilename world --inputWorldFilename world_init --debug false --verbose true");
# tao file world.gmm
os.system("python createNDX.py -i ./lst_ch -o ./ndx_ch");
os.system("python createNDX.py -i ./lst_qh -o ./ndx_qh");
os.system("python createCfg.py -i ./lst_ch"); # tao file config
os.system("python createCfg.py -i ./lst_qh"); # tao file config
os.system("python TrainTargetCH.py"); # train
os.system("python TrainTargetQH.py"); # train
# os.system("python createTest2.py"); # tao file test
# os.system("python ComputeTest2.py"); # test
# os.system("python report2.py"); # tao file bao cao