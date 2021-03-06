import os
print("Running feature_calculate.py.\n")
os.system("python feature_calculate.py"); # trich chon dac trung
os.system("python NormFeat1.py"); # chuan hoa lan 1
os.system("python EnergyDetector1.py"); # danh dau nhung doan co tieng noi
os.system("python NormFeat2.py"); # chuan hoa lan 2
os.system("python namefile.py"); # tao danh sach file wav
# ---------------------------------
# phan theo loai
os.system("python remove_and_create.py");
os.system("python DataSplit1.py -i all1.lst -o ./lst -p 5 -t 0"); # chia phan de train va test
# DataSplit1.py: phan theo loai /
# DataSplit.py: phan theo lan dieu /
os.system("python createWorld.py -i ./lst"); # tao file config World.lst va World.weight
os.system("./TrainWorld.exe --config ./cfg/TrainWorldInit.cfg --inputStreamList ./lst/world.lst --weightStreamList ./lst/world.weight --outputWorldFilename world_init --debug false --verbose true"); # tao 2 file
os.system("./TrainWorld.exe --config ./cfg/TrainWorldFinal.cfg --inputStreamList ./lst/world.lst --weightStreamList ./lst/world.weight --outputWorldFilename world --inputWorldFilename world_init --debug false --verbose true");
# tao file world.gmm
os.system("python createNDX.py -i ./lst -o ./ndx");
os.system("python createCfg.py -i ./lst"); # tao file config
os.system("python TrainTarget.py"); # train
os.system("python createTest.py"); # tao file test
os.system("python ComputeTest.py"); # test
os.system("python report.py -i ./res -o ./rpt"); # tao file bao cao

#=================
# phan theo lan dieu
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

os.system("python createTest3.py -c ./test_ch -q ./test_qh -r ./res -p ./rpt"); # tao file test
# createTest tao file test phan theo loai
# createTest2 tao file test phan theo lan dieu
# createTest3 tao file test phan theo lan dieu dua vao ket qua phan theo loai

os.system("python ComputeTest2.py"); # test
# ComputeTest test theo loai
# ComputeTest2 test theo lan dieu

os.system("python report2.py -c ./res_ch -q ./res_qh -o ./rpt"); # tao file bao cao

os.system("python exportData1.py -i ./rpt -f report.txt")
os.system("python exportData2.py -i ./rpt -f report_ch.txt")
os.system("python exportData2.py -i ./rpt -f report_qh.txt")

# Merger data
# python mergeData.py -i ./mergeData # merge du lieu phan theo lan dieu
# python mergeData2.py -i ./mergeData # merge du lieu phan theo the loai

# python convert2Number.py -n 20 -f ./mergeData/mergeData.txt

