# cat ngan file chia thanh the loai, sau do chia ve tung lan dieu
import os
# print("Running feature_calculate.py.\n")
# os.system("python feature_calculate.py"); # trich chon dac trung
# os.system("python NormFeat1.py"); # chuan hoa lan 1
# os.system("python EnergyDetector1.py"); # danh dau nhung doan co tieng noi
# os.system("python NormFeat2.py"); # chuan hoa lan 2
# os.system("python namefile.py"); # tao danh sach file wav
#---------------------------------
# huan luyen phan theo loai
# os.system("python remove_and_create.py");
# os.system("python createLst_part.py -o ./lst"); # tao ra file train cho thu muc lst
# os.system("python createWorld.py -i ./lst"); # tao file config World.lst va World.weight
# os.system("./TrainWorld.exe --config ./cfg/TrainWorldInit.cfg --inputStreamList ./lst/world.lst --weightStreamList ./lst/world.weight --outputWorldFilename world_init --debug false --verbose true"); # tao 2 file
# os.system("./TrainWorld.exe --config ./cfg/TrainWorldFinal.cfg --inputStreamList ./lst/world.lst --weightStreamList ./lst/world.weight --outputWorldFilename world --inputWorldFilename world_init --debug false --verbose true");
# # tao file world.gmm
# os.system("python createNDX.py -i ./lst -o ./ndx");
# os.system("python createCfg.py -i ./lst"); # tao file config
# os.system("python TrainTarget.py"); # train

# #---------------------------------
# # huan luyen phan theo lan dieu
# os.system("python createLst.py"); # tao ra file cho 2 thu muc lst_ch va lst_qh
# os.system("python createWorld.py -i ./lst_ch"); # tao file config World.lst va World.weight
# os.system("python createWorld.py -i ./lst_qh")
# os.system("./TrainWorld.exe --config ./cfg/TrainWorldInit_ch.cfg --inputStreamList ./lst_ch/world.lst --weightStreamList ./lst_ch/world.weight --outputWorldFilename world_init --debug false --verbose true"); # tao 2 file
# os.system("./TrainWorld.exe --config ./cfg/TrainWorldInit_qh.cfg --inputStreamList ./lst_qh/world.lst --weightStreamList ./lst_qh/world.weight --outputWorldFilename world_init --debug false --verbose true"); # tao 2 file
# os.system("./TrainWorld.exe --config ./cfg/TrainWorldFinal_ch.cfg --inputStreamList ./lst_ch/world.lst --weightStreamList ./lst_ch/world.weight --outputWorldFilename world --inputWorldFilename world_init --debug false --verbose true");
# # tao file world.gmm
# os.system("./TrainWorld.exe --config ./cfg/TrainWorldFinal_qh.cfg --inputStreamList ./lst_qh/world.lst --weightStreamList ./lst_qh/world.weight --outputWorldFilename world --inputWorldFilename world_init --debug false --verbose true");
# # tao file world.gmm
# os.system("python createNDX.py -i ./lst_ch -o ./ndx_ch");
# os.system("python createNDX.py -i ./lst_qh -o ./ndx_qh");
# os.system("python createCfg.py -i ./lst_ch"); # tao file config
# os.system("python createCfg.py -i ./lst_qh"); # tao file config
# os.system("python TrainTargetCH.py"); # train
# os.system("python TrainTargetQH.py"); # train

#---------------------------------
# cat ngan file de tao du lieu test

# os.system("python cutWav.py -t 12 -f ./wav/wav12") # cat file wav theo thoi gian
# print("Cut file Wav successfully! ")

# os.system("python feature_calculate_CH_QH.py -i ./wav/wav12 -o ./prm/prm12"); # trich chon dac trung
# print("Run file feature_calculate_CH_QH successfully! ")

# os.system("python NormFeat1_CH_QH.py -i ./prm/prm12"); # chuan hoa lan 1
# # sua file NormFeat_ch_qh
# print("Run file NormFeat1_CH_QH successfully! ")

# os.system("python EnergyDetector_CH_QH.py -i ./prm/prm12"); # danh dau nhung doan co tieng noi
# # sua file EnergyDetector_ch_qh
# print("Run file EnergyDetector_CH_QH successfully! ")

# os.system("python NormFeat2_CH_QH.py -i ./prm/prm12"); # chuan hoa lan 2
# # sua file NormFeat_energy_ch_qh
# print("Run file NormFeat2_CH_QH successfully! ")

# #---------------------------------
# phan theo the loai
os.system("python getTime.py -c StartTest -o ./rpt/rpt12") # danh thoi gian bat dau
os.system("python createTestCH_QH.py -i ./lbl/lbl12 -o ./test/test12 -n ./ndx"); # tao file test
os.system("python ComputeTest_part.py -i ./test/test12 -o ./res/res12"); # test
# sua file targetTest_part
os.system("python report.py -i ./res/res12 -o ./rpt/rpt12"); # tao file bao cao

# ---------------------------------
# phan theo lan dieu
os.system("python createTest3.py -c ./test_ch/test_ch12 -q ./test_qh/test_qh12 -r ./res/res12 -p ./rpt/rpt12"); # tao file test
os.system("python ComputeTest2_part.py -c ./test_ch/test_ch12 -q ./test_qh/test_qh12 -a ./res_ch/res_ch12 -b res_qh/res_qh12"); # test
# sua file targetTest_ch_part va targetTest_qh_part
os.system("python report2.py -c ./res_ch/res_ch12 -q ./res_qh/res_qh12 -o ./rpt/rpt12"); # tao file bao cao

os.system("python exportData1.py -i ./rpt/rpt12 -f report.txt")
os.system("python exportData2.py -i ./rpt/rpt12 -f report_ch.txt")
os.system("python exportData2.py -i ./rpt/rpt12 -f report_qh.txt")

os.system("python getTime.py -c EndTest -o ./rpt/rpt12") # danh thoi gian ket thuc