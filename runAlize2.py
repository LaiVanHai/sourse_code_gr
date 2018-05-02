import os
# os.system("python createLst_ch_qh.py"); # tao ra file cho 2 thu muc lst_ch va lst_qh
# os.system("python createWorld.py -i ./lst_ch_qh"); # tao file config World.lst va World.weight
# os.system("./TrainWorld.exe --config ./cfg/TrainWorldInit_ch_qh.cfg --inputStreamList ./lst_ch_qh/world.lst --weightStreamList ./lst_ch_qh/world.weight --outputWorldFilename world_init --debug false --verbose true"); # tao 2 file
# os.system("./TrainWorld.exe --config ./cfg/TrainWorldFinal_ch_qh.cfg --inputStreamList ./lst_ch_qh/world.lst --weightStreamList ./lst_ch_qh/world.weight --outputWorldFilename world --inputWorldFilename world_init --debug false --verbose true");
# # tao file world.gmm
# os.system("python createNDX.py -i ./lst_ch_qh -o ./ndx_ch_qh");

# os.system("python createCfg.py -i ./lst_ch_qh"); # tao file config

# os.system("python TrainTargetCH_QH.py"); # train

# ===========================

# os.system("python cutWav.py -t 20 -f ./wav/wav20") # cat file wav theo thoi gian
# print("Cut file Wav successfully! ")

os.system("python feature_calculate_CH_QH.py -i ./wav/wavF -o ./prm/prmF"); # trich chon dac trung
print("Run file feature_calculate_CH_QH successfully! ")

os.system("python NormFeat1_CH_QH.py -i ./prm/prmF"); # chuan hoa lan 1
# sua file NormFeat_ch_qh
print("Run file NormFeat1_CH_QH successfully! ")

os.system("python EnergyDetector_CH_QH.py -i ./prm/prmF"); # danh dau nhung doan co tieng noi
# sua file EnergyDetector_ch_qh
print("Run file EnergyDetector_CH_QH successfully! ")

os.system("python NormFeat2_CH_QH.py -i ./prm/prmF"); # chuan hoa lan 2
# sua file NormFeat_energy_ch_qh
print("Run file NormFeat2_CH_QH successfully! ")

os.system("python createTestCH_QH.py -i ./lbl/lblF -o ./test/testF"); # tao file test
os.system("python ComputeTest_CH_QH.py -i ./test/testF -o ./res/resF"); # test
# sua file targetTest_ch_qh
os.system("python report_CH_QH.py -i ./res/resF -o ./rpt/rptF  -n ./ndx_ch_qh"); # tao file bao cao