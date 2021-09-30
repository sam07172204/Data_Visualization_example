import os
import matplotlib.pyplot as plt
import numpy as np

ppp = ['PC', 'Nano Pi', 'Raspberry Pi', 'NUC980']
# ----------------TPS------------------------
# disk_postmark = [30057, 32364, 31025, 31161]
# ramdisk_postmark = [233, 88, 104, 88]
#
# disk_iozone = [1483, 4540, 3149, 4621]
# ramdisk_iozone = [243, 54, 124, 54]
# -----------------ERASE-----------------------
disk_postmark = [29943, 32332, 30981, 0]
ramdisk_postmark = [193, 37, 83, 0]

disk_iozone = [924, 4539, 3323, 0]
ramdisk_iozone = [191, 54, 107, 0]
# ----------------------------------------
bar_width = 0.2
x = np.arange(len(ppp))

fig = plt.figure(figsize=(12, 6))

# plt.title("PostMark(TPS)")
plt.title("Iozone+PostMark(Erase Count)")
plt.xlabel("Platform")
plt.ylabel("Frequency")

plt.bar(x , disk_postmark ,width=0.2,  color='w',label="Disk PostMark",align='center',hatch="\\\\\\\\\\", tick_label=ppp )
plt.bar(x  , ramdisk_postmark , width=0.2,  color='grey',label="RAM Disk PostMark", align="center",hatch="////////")

plt.bar(x+0.22  ,disk_iozone ,width=0.2,  color='w',label="Disk Iozone",align='center',hatch="||||||")
plt.bar(x+0.22  , ramdisk_iozone , width=0.2,  color='grey',label="RAM Disk Iozone", align="center" ,hatch="xxxx")

# plt.bar(x+0.44  ,disk_postmark ,width=0.2,  color='w',label="disk_160kb",align='center',hatch="*")
# plt.bar(x+0.44  , ramdisk_postmark , width=0.2,  color='black',label="ramdisk_160kb", align="center")
#
# plt.bar(x+0.66  ,disk_iozone ,width=0.2,  color='w',label="disk_160kb",align='center',hatch="o")
# plt.bar(x+0.66  , ramdisk_iozone , width=0.2,  color='black',label="ramdisk_160kb", align="center")
# 添加数据标签

plt.annotate('c',xy=(1,1),xytext=(-0.04, 44),fontsize=20)
for x,y in enumerate(disk_postmark):
    plt.text(x, y+200, y,ha='center',fontsize=16)
    # plt.text(x, "disk", y,ha='center',fontsize=16)
for x,y in enumerate(ramdisk_postmark):
    plt.text(x, y+200, y,ha='center',fontsize=16)
for x,y in enumerate(disk_iozone):
    plt.text(x+0.22, y+200, y,ha='center',fontsize=16)
for x,y in enumerate(ramdisk_iozone):
    plt.text(x+0.22, y+200, y,ha='center',fontsize=16)
# for a, b in zip(ppp, ramdisk_20b):
#     plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)

# 添加图例
#
values=[0,10000,20000,30000,40000]
plt.yticks(values)
plt.legend(loc='upper right', fontsize=8)
# fig = plt.figure(figsize=(12, 6))
plt.savefig("C:/Users/許富淞/Desktop/論文最終/post+iozone_ec.png")
plt.show()
