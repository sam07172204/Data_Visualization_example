import pandas as pd
import os
import csv
import matplotlib.pyplot as plt

savepath = "C:/Users/sam/Desktop/碩論實驗資料備份/論文最終/PC/merge/"
savefile = "iozone"

title = "TPS RAM Disk vs Disk (Iozone)"
# title = "TPS RAM Disk vs Disk (1txt file/160kbytes)"

diskpath = "C:/Users/sam/Desktop/碩論實驗資料備份/論文最終/PC/txt大小_disk/"
diskfile = "disk_160kb.txt"

rampath = "C:/Users/sam/Desktop/碩論實驗資料備份/論文最終/PC/txt大小_ramdisk/"
ramfile = "ramdisk_160kb.txt"

disk_log_table = pd.read_table(diskpath+diskfile)
disk_time = []
disk_number = []
disk_mmcblk0_write_MB = []
ram_disk_log_table = pd.read_table(rampath+ramfile)
ram_time = []
ram_number = []
ram_mmcblk0_write_MB = []
disk_log_table.to_csv('disk_log_csv.csv',index=False)
disk_log = pd.read_csv('disk_log_csv.csv',header=None)
ram_disk_log_table.to_csv('ram_disk_log_csv.csv',index=False)
ramdisk_log = pd.read_csv('ram_disk_log_csv.csv',header=None)

# disk-------------------------------------------------------
for i in range(len(disk_log)):
    #time
    if i % 10 == 0:
        disk_time.append(disk_log.iloc[i][0])
    #disk_mmcblk0_write_MB
    if i % 10 == 6:
        mmcblk0_spilt = disk_log.iloc[i][0].split(' ')
        for i in range(mmcblk0_spilt.count('')):
            mmcblk0_spilt.remove('')

        disk_mmcblk0_write_MB.append(mmcblk0_spilt[1])

disk_mmcblk0_write_MB = [i for i in disk_mmcblk0_write_MB if i]
disk_mmcblk0_write_MB = list(map(float, disk_mmcblk0_write_MB))

for i in range(len(disk_mmcblk0_write_MB)):
    disk_number.append(i)


# ramdisk-------------------------------------------------------
for i in range(len(ramdisk_log)):
    #time
    if i % 10 == 0:
        ram_time.append(i)
        # print(ramdisk_log.iloc[i][0])
    #mmcblk0_write_MB
    if i % 10 == 6:
        mmcblk0_spilt = ramdisk_log.iloc[i][0].split(' ')
        for i in range(mmcblk0_spilt.count('')):
            mmcblk0_spilt.remove('')
        ram_mmcblk0_write_MB.append(mmcblk0_spilt[1])

ram_mmcblk0_write_MB = [i for i in ram_mmcblk0_write_MB if i]
# if mmcblk0_write_MB!="0.00":
    # print(mmcblk0_write_MB)
ram_mmcblk0_write_MB = list(map(float, ram_mmcblk0_write_MB))
for i in range(len(ram_mmcblk0_write_MB)):
    ram_number.append(i)

values = [50,100,150,200,250]

print("disk:",sum(disk_mmcblk0_write_MB))
print("ramdiskM",sum(ram_mmcblk0_write_MB))
# plt-------------------------------------------------------


# fig = plt.figure(figsize=(12, 6))
# plt.title(title , fontsize=24)
# plt.axis([0, len(ram_number),-5,max(disk_mmcblk0_write_MB)+100 ])
# plt.scatter(disk_number,disk_mmcblk0_write_MB,s = 22,color='r',marker='x', label='disk')
# plt.scatter(ram_number,ram_mmcblk0_write_MB,s = 22,color='b', marker='h', label='ramdisk',alpha=0.9)
# plt.xlabel('time(s)', fontsize=20)
# plt.ylabel('tps(I/O per second)', fontsize=20)
# plt.tick_params(axis='x', labelsize=16)
# plt.tick_params(axis='y', labelsize=16)
# plt.legend( loc='upper right', fontsize=20)
# plt.yticks(values)
# plt.savefig(savepath+savefile+".png")
# plt.show()

# bins_list=[0.00,0.02,0.04,0.06,0.08,0.10,0.12,0.14,0.16,0.18,0.20]    #分布區域 (組距)
# # bins_list=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0]    #分布區域 (組距)
# # bins_list=[0.00,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09]    #分布區域 (組距)
bins_list=[0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0]    #分布區域 (組距)
# print(disk_mmcblk0_write_MB)
# n, bins, patches=plt.hist(disk_mmcblk0_write_MB, bins=bins_list, color='r')           #繪製直方圖
# print(n)                                                                          #輸出次數分配
# print(bins)                                                                     #輸出分布區間
# for p in patches:                                                            #輸出 Patch 物件內容
#     print(p)
# plt.title("disk_write_count", fontsize=24)                                         #設定圖形標題
# plt.ylabel('count', fontsize=20)                                                        #設定 Y 軸標籤
# plt.xlabel('write(MB/s)', fontsize=20)                                                     #設定 X 軸標籤
# plt.tick_params(axis='x', labelsize=16)
# plt.tick_params(axis='y', labelsize=16)
# plt.show()
