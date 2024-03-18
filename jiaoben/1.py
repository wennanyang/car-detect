#-*-coding:gb2312-*-
from lxml.etree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import xml.dom.minidom
import os
import sys
from PIL import Image


# ����NWPU VHR-10���ݼ��е�txt��ע��Ϣת���� xml�ļ�
# �˴���pathӦ�ô������NWPU VHR-10���ݼ��ļ��������ground truth�ļ��е�Ŀ¼
# �� path = "/home/ywn/yolov5_vedai/NWPU VHR-10 dataset/ground truth"
def deal(path):
    files = os.listdir(path)  # files��ȡ���б�עtxt�ļ����ļ���
    # �˴����������������·��  ����VOC���ݼ��ĸ�ʽ��xml�ļ�Ӧ����������ݼ��ļ������Annotations�ļ�������
    outpath = "/home/ywn/yolov5_vedai/NWPU/Annotations/"
    # �������ļ��в����ڣ��ʹ�����
    if os.path.exists(outpath) == False:
        os.mkdir(outpath)
    # �������е�txt��ע�ļ���һ��650��txt�ļ�
    for file in files:

        filename = os.path.splitext(file)[0]  # ��ȡground truth�ļ����б�עtxt�ļ����ļ�������������ļ���Ϊ001.txt����ôfilename = '001'
        sufix = os.path.splitext(file)[1]  # ��ȡ��עtxt�ļ��ĺ�׺�� �ж��Ƿ�Ϊtxt
        if sufix == '.txt':  # ��עtxt�ļ���ÿһ�д���һ��Ŀ�꣬(x1,y1)��(x2,y2)��class_number����ʾ
            xmins = []
            ymins = []
            xmaxs = []
            ymaxs = []
            names = []

            # num,xmins,ymins,xmaxs,ymaxs,names=readtxt(path + '/' + file)    # ����readtxt�ļ���ȡ��Ϣ��ת��readtxt����
            path_txt = path + '/' + file  # ��ȡtxt��ע�ļ���·����Ϣ
            # ��txt��ע�ļ�
            with open(path_txt, 'r') as f:
                contents = f.read()  # ��txt�ļ�����Ϣ���ж�ȡ��contents�б���
                objects = contents.split('\n')  # �Ի��л���ÿһ��Ŀ��ı�ע��Ϣ����Ϊÿһ��Ŀ��ı�ע��Ϣ��txt�ļ���Ϊһ��
                for i in range(objects.count('')):
                    objects.remove('')  # ��objects�еĿո��Ƴ�
                num = len(objects)  # ��ȡһ����ע�ļ���Ŀ�������objects��һ��Ԫ�ش������Ϣ����һ�����Ŀ��

                # ���� objects�б���ȡÿһ�����Ŀ�����ά��Ϣ
                for objecto in objects:
                    xmin = objecto.split(',')[0]  # xmin = '(563'
                    xmin = xmin.split('(')[1]  # xmin = '563' ���ܴ��ڿո�
                    xmin = xmin.strip()  # strip����ȥ���ַ�����ͷ��β�Ŀո��

                    ymin = objecto.split(',')[1]  # ymin = '478)'
                    ymin = ymin.split(')')[0]  # ymin = '478'  ���ܴ��ڿո�
                    ymin = ymin.strip()  # strip����ȥ���ַ�����ͷ��β�Ŀո��

                    xmax = objecto.split(',')[2]  # xmaxͬ��
                    xmax = xmax.split('(')[1]
                    xmax = xmax.strip()

                    ymax = objecto.split(',')[3]  # ymaxͬ��
                    ymax = ymax.split(')')[0]
                    ymax = ymax.strip()

                    name = objecto.split(',')[4]  # ���� ͬ��
                    name = name.strip()

                    if name == "1 " or name == "1":  # ��������Ϣת����label�ַ�����Ϣ
                        name = 'airplane'
                    elif name == "2 " or name == "2":
                        name = 'ship'
                    elif name == "3 " or name == "3":
                        name = 'storage tank'
                    elif name == "4 " or name == "4":
                        name = 'baseball diamond'
                    elif name == "5 " or name == "5":
                        name = 'tennis court'
                    elif name == "6 " or name == "6":
                        name = 'basketball court'
                    elif name == "7 " or name == "7":
                        name = 'ground track field'
                    elif name == "8 " or name == "8":
                        name = 'harbor'
                    elif name == "9 " or name == "9":
                        name = 'bridge'
                    elif name == "10 " or name == "10":
                        name = 'vehicle'
                    else:
                        print(path)
                    # print(xmin,ymin,xmax,ymax,name)
                    xmins.append(xmin)
                    ymins.append(ymin)
                    xmaxs.append(xmax)
                    ymaxs.append(ymax)
                    names.append(name)

            filename_fill = str(int(filename)).zfill(6)  # ��xml���ļ������Ϊ6λ��������1.xml�͸�Ϊ000001.xml
            filename_jpg = filename_fill + ".jpg"  # ����xml�д洢���ļ���Ϊ000001.jpg�����Ի��ö����е�NWPU���ݼ��е�ͼƬ����������
            print(filename_fill)

            dealpath = outpath + filename_fill + ".xml"

            # ע�⣬����������ת��֮��ͼƬ�������E:/Remote Sensing/Data Set/VOCdevkit2007/VOC2007/JPEGImages/��
            imagepath = "/home/ywn/yolov5_vedai/NWPU/images/" + filename_fill + ".jpg"
            with open(dealpath, 'w') as f:
                img = Image.open(imagepath)  # ����ͼƬ�ĵ�ַ��ͼƬ����ȡͼƬ�Ŀ� �� ��
                width = img.size[0]
                height = img.size[1]
                # ��ͼƬ�Ŀ�͸��Լ�������VOC���ݼ����Ӧ����Ϣ
                writexml(dealpath, filename_jpg, num, xmins, ymins, xmaxs, ymaxs, names, height, width)

    #  ͬʱҲ�ø�negative image set�ļ�����������и�����ͼƬ����xml��ע
    negative_path = "/home/ywn/yolov5_vedai/NWPU VHR-10 dataset/negative image set/"
    negative_images = os.listdir(negative_path)
    for file in negative_images:
        filename = file.split('.')[0]  # ��ȡ�ļ�������������׺��
        filename_fill = str(int(filename) + 650).zfill(6)  # ��xml���ļ������Ϊ6λ����ͬʱ����650������1.xml�͸�Ϊ00001.xml
        filename_jpg = filename_fill + '.jpg'  # �����һ��������001.jpg��filename_jpg Ϊ000651.jpg
        ## ������Ϊ6λ��
        print(filename_fill)
        ## ���ɲ���Ŀ���xml�ļ�
        dealpath = outpath + filename_fill + ".xml"
        # ע�⣬����������ת��֮��ͼƬ�������E:/Remote Sensing/Data Set/VOCdevkit2007/VOC2007/JPEGImages/��
        imagepath = "/home/ywn/yolov5_vedai/NWPU/images/" + filename_fill + ".jpg"
        with open(dealpath, 'w') as f:
            img = Image.open(imagepath)
            width = img.size[0]
            height = img.size[1]
            # ����ߺͿյ�Ŀ���ע��Ϣд��xml��ע
            writexml(dealpath, filename_jpg, num=0, xmins=[], ymins=[], xmaxs=[], ymaxs=[], names=[], width=width,
                     height=height)


# NWPU���ݼ��б�ע����ά��Ϣ (x1,y1) denotes the top-left coordinate of the bounding box,
#  (x2,y2) denotes the right-bottom coordinate of the bounding box
# ���� xmin = x1  ymin = y1,  xmax = x2, ymax = y2  ͬʱҪע������������������ͼƬ���Ͻ�Ϊ����ԭ������
# VOC���ݼ����ڰ�Χ���ע�ĸ�ʽ��bounding-box���������½Ǻ����Ͻ�xy����

# ����txt��ȡ�ı�ע��Ϣд�뵽xml�ļ���
def writexml(path, filename, num, xmins, ymins, xmaxs, ymaxs, names, height, width):  # Nwpu-vhr-10 < 1000*600
    node_root = Element('annotation')

    node_folder = SubElement(node_root, 'folder')
    node_folder.text = "VOC2007"

    node_filename = SubElement(node_root, 'filename')
    node_filename.text = "%s" % filename

    node_size = SubElement(node_root, "size")
    node_width = SubElement(node_size, 'width')
    node_width.text = '%s' % width

    node_height = SubElement(node_size, 'height')
    node_height.text = '%s' % height

    node_depth = SubElement(node_size, 'depth')
    node_depth.text = '3'
    for i in range(num):
        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')
        node_name.text = '%s' % names[i]
        node_name = SubElement(node_object, 'pose')
        node_name.text = '%s' % "unspecified"
        node_name = SubElement(node_object, 'truncated')
        node_name.text = '%s' % "0"
        node_difficult = SubElement(node_object, 'difficult')
        node_difficult.text = '0'
        node_bndbox = SubElement(node_object, 'bndbox')
        node_xmin = SubElement(node_bndbox, 'xmin')
        node_xmin.text = '%s' % xmins[i]
        node_ymin = SubElement(node_bndbox, 'ymin')
        node_ymin.text = '%s' % ymins[i]
        node_xmax = SubElement(node_bndbox, 'xmax')
        node_xmax.text = '%s' % xmaxs[i]
        node_ymax = SubElement(node_bndbox, 'ymax')
        node_ymax.text = '%s' % ymaxs[i]

    xml = tostring(node_root, pretty_print=True)
    dom = parseString(xml)
    with open(path, 'wb') as f:
        f.write(xml)
    return


if __name__ == "__main__":
    # pathָ�����Ǳ�עtxt�ļ����ڵ�·��
    path = "/home/ywn/yolov5_vedai/NWPU VHR-10 dataset/ground truth"
    deal(path)
    print("done!")

