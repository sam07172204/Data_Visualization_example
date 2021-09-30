import pandas as pd
import os
import csv
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import statistics
a = []

savepath = "C:/Users/sam/Desktop/碩論實驗資料備份/論文最終/PC/txt大小_ramdisk/"
savefile = "160kb_erase_disk"
title = "RAM Disk Erase Count(1txt file/160kbytes)"

path = "C:/Users/sam/Desktop/碩論實驗資料備份/論文最終/rpi/iozone_ramdisk/"
file = "sdb.offset_179,0_w_iozone.dat"
block_log_table = pd.read_table(path+file,header=None,encoding='gb2312',
                             delim_whitespace=True,index_col=None)
# images_pixel = pd.read_table('all_geo.txt')
# print(block_log_table[1])

for i in range(len(block_log_table)):
    a.append(block_log_table[1][i])
dict = {}
for key in a:
    dict[key] = dict.get(key, 0) + 1
# print(dict)

myList = dict.items()
myList = sorted(myList)
x, y = zip(*myList)
s=sorted(y)
print(s)
print("mean",statistics.mean(s))
print("sum",sum(s))
# fig1 = plt1.figure(figsize=(6, 5))
# plt.ylim(0, 600)
#
# plt.scatter(x, y,s = 20,color='b', marker='h')
# plt.xlabel('block number', fontsize=16)
# plt.ylabel('Erase count', fontsize=16)
# plt.title(title , fontsize=18)
# plt.savefig(savepath+savefile+".png")
# plt.show()

# plt.title("ramdisk iozone sector number " , fontsize=20)
#
#
# plt1.xlim(-1,50)
# # #print(mmcblk0_write_MB)
# # plt.scatter(number,mmcblk0_write_MB,s = 22,color='b', marker='h', label='ramdisk')
# plt1.xlabel('time(s)', fontsize=20)
# plt1.ylabel('sector  ', fontsize=20)
# # plt.tick_params(axis='x', labelsize=16)
# # plt.tick_params(axis='y', labelsize=16)
#
# plt1.scatter(block_log_table[0],block_log_table[0]+block_log_table[1],s = 5,color='b')
# # plt.plot(block_log_table[0],block_log_table[1]+block_log_table[1])
# plt1.savefig(path+file[:-4]+"_sector.png")
# plt1.show()
