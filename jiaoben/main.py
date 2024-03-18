#-*-coding:gb2312-*-

import os
import shutil


def imag_rename(old_path, new_path,start_number = 0):
    filelist = os.listdir(old_path)  # ���ļ��������е��ļ��������ļ��У�
    if os.path.exists(new_path) == False:
        os.mkdir(new_path)
    for file in filelist:  # ���������ļ�
        Olddir = os.path.join(old_path, file)  # ԭ�����ļ�·��
        if os.path.isdir(Olddir):  # ������ļ���������
            continue
        filename = os.path.splitext(file)[0]  # �ļ���
        filetype = os.path.splitext(file)[1]  # �ļ���չ��
        if filetype == '.jpg':
            Newdir = os.path.join(new_path, str(int(filename) + start_number).zfill(6) + filetype)
            # ���ַ�������zfill ��0��ȫ����λ��
            shutil.copyfile(Olddir, Newdir)


if __name__ == "__main__":
    # ���positive image set�ļ����е����������⣬start_number = 0
    old_path = "/home/ywn/yolov5_vedai/NWPU VHR-10 dataset/positive image set/"
    new_path = "/home/ywn/yolov5_vedai/NWPU/images"
    imag_rename(old_path, new_path)
    # ���negative image set�ļ����е����������⣬start_number = 650
    old_path = "/home/ywn/yolov5_vedai/NWPU VHR-10 dataset/negative image set/"
    new_path = "/home/ywn/yolov5_vedai/NWPU/images"
    imag_rename(old_path,new_path,start_number = 650)
    print("done!")

