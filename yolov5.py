import os,cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import yaml
import glob
DIR_PATH = "E:/yolov5_vedai"
train_path  = os.path.join(DIR_PATH, "vedai/images/train")
test_path  = os.path.join(DIR_PATH, "vedai/images/test")
annot = os.path.join(DIR_PATH, "vedai/data")

a = os.listdir(train_path)
for item in a:
    if item.endswith(".xml"):
        os.remove(os.path.join(train_path, item))

b = os.listdir(test_path)
for item in b:
    if item.endswith(".xml"):
        os.remove(os.path.join(test_path, item))



config = {'train': 'E:/yolov5_vedai/vedai_data/train/images',
         'val': 'E:/yolov5_vedai/vedai_data/valid/images',
         'nc': 2,
         'names': ['car', 'notcar']}
if not os.path.exists('data.yaml'):
    with open("data.yaml", "w+") as file:
        yaml.dump(config, file, default_flow_style=False)

# python .\build_dataset.py --input_dir e:/yolov5_vedai/vedai/images/train/ --output_dir e:/yolov5_vedai/vedai_data --train E:\yolov5_vedai\vedai\data\train_labels.csv --valid E:\yolov5_vedai\vedai\data\test_labels.csv

TRAIN = True
if TRAIN:
    command = "python .\\yolov5\\train.py --data data.yaml --weights yolov5n.pt --img 640 --epochs 20 --batch-size 32 --name result_dir"
    ret = os.system(command)    
    print(ret)





# def set_res_dir():
#     # Directory to store results
#     res_dir_count = len(glob.glob('runs/train/*'))
#     print(f"Current number of result directories: {res_dir_count}")
#     if TRAIN:
#         RES_DIR = f"results_{res_dir_count+1}"
#         print(RES_DIR)
#     else:
#         RES_DIR = f"results_{res_dir_count}"
#     return RES_DIR

# def set_res_dir():
#     # Directory to store results
#     res_dir_count = len(glob.glob('runs/train/*'))
#     print(f"Current number of result directories: {res_dir_count}")
#     if TRAIN:
#         RES_DIR = f"results_{res_dir_count+1}"
#         print(RES_DIR)
#     else:
#         RES_DIR = f"results_{res_dir_count}"
#     return RES_DIR

