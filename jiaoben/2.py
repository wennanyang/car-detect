#-*-coding:gb2312-*-
import os
import random

trainval_percent = 0.8  # ��ʾѵ��������֤��(������֤��)��ռ��ͼƬ�ı���
train_percent = 0.75  # ѵ������ռ������֤���ı���
xmlfilepath = "/home/ywn/yolov5_vedai/NWPU/Annotations"
txtsavepath = "/home/ywn/yolov5_vedai/NWPU/ImageSets/Main"
total_xml = os.listdir(xmlfilepath)

num = 650  # ��Ŀ���ͼƬ��
list = range(num)
tv = int(num * trainval_percent)  # xml�ļ��еĽ�����֤����
tr = int(tv * train_percent)  # xml�ļ��е�ѵ��������ע�⣬������ǰ�涨�����ѵ����ռ������֤���ı���
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open("/home/ywn/yolov5_vedai/NWPU/ImageSets/Main/trainval.txt", 'w')
ftest = open('/home/ywn/yolov5_vedai/NWPU/ImageSets/Main/test.txt', 'w')
ftrain = open("/home/ywn/yolov5_vedai/NWPU/ImageSets/Main/train.txt", 'w')
fval = open('/home/ywn/yolov5_vedai/NWPU/ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

for i in range(150):
    num = str(651 + i).zfill(6) + '\n'
    ftest.write(num)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()

print("done!")

