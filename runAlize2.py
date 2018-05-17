import os
# print("Running feature_calculate.py.\n")
# os.system("python feature_calculate.py"); # trich chon dac trung
# os.system("python NormFeat1.py"); # chuan hoa lan 1
# os.system("python EnergyDetector1.py"); # danh dau nhung doan co tieng noi
# os.system("python NormFeat2.py"); # chuan hoa lan 2
# os.system("python namefile.py"); # tao danh sach file wav
# os.system("python createLst_ch_qh.py -o ./lst_ch_qh); # tao ra file cho 2 thu muc lst_ch va lst_qh
# os.system("python createWorld.py -i ./lst_ch_qh"); # tao file config World.lst va World.weight
# os.system("./TrainWorld.exe --config ./cfg/TrainWorldInit_ch_qh.cfg --inputStreamList ./lst_ch_qh/world.lst --weightStreamList ./lst_ch_qh/world.weight --outputWorldFilename world_init --debug false --verbose true"); # tao 2 file
# os.system("./TrainWorld.exe --config ./cfg/TrainWorldFinal_ch_qh.cfg --inputStreamList ./lst_ch_qh/world.lst --weightStreamList ./lst_ch_qh/world.weight --outputWorldFilename world --inputWorldFilename world_init --debug false --verbose true");
# # tao file world.gmm
os.system("python createNDX.py -i ./lst_ch_qh -o ./ndx_ch_qh");

os.system("python createCfg.py -i ./lst_ch_qh"); # tao file config

os.system("python TrainTargetCH_QH.py"); # train

# ===========================

os.system("python cutWav.py -t 4 -f ./wav/wav4") # cat file wav theo thoi gian
# print("Cut file Wav successfully! ")

os.system("python feature_calculate_CH_QH.py -i ./wav/wav4 -o ./prm/prm4"); # trich chon dac trung
print("Run file feature_calculate_CH_QH successfully! ")

os.system("python NormFeat1_CH_QH.py -i ./prm/prm4"); # chuan hoa lan 1
# sua file NormFeat_ch_qh
print("Run file NormFeat1_CH_QH successfully! ")

os.system("python EnergyDetector_CH_QH.py -i ./prm/prm4"); # danh dau nhung doan co tieng noi
# sua file EnergyDetector_ch_qh
print("Run file EnergyDetector_CH_QH successfully! ")

os.system("python NormFeat2_CH_QH.py -i ./prm/prm4"); # chuan hoa lan 2
# sua file NormFeat_energy_ch_qh
print("Run file NormFeat2_CH_QH successfully! ")

os.system("python createTestCH_QH.py -i ./lbl/lbl4 -o ./test/test4 -n ./ndx_ch_qh"); # tao file test
os.system("python ComputeTest_CH_QH.py -i ./test/test4 -o ./res/res4"); # test
# sua file targetTest_ch_qh
os.system("python report_CH_QH.py -i ./res/res4 -o ./rpt/rpt4  -n ./ndx_ch_qh"); # tao file bao cao