# 此脚本用来处理录制的pcd数据包。
# 1、去除pcd中的nan值。2、每隔x帧抽取1帧数据，将所有pcd包合并shuffle。3、分割数据包为N个包。
# 输入：包含pcd1、pcd2...的文件夹路径。输出：分割后的N个文件夹。
#------input_folder
#------------pcd1
#------------pcd2
#------------pcd3
#
#------output_folder
#------------processed_pcd1
#------------processed_pcd2
#------------processed_pcd3
#example: python script/preprocess_pcd_dataset.py --input_folder /media/sdlg/DataSet/myf_kuang/raw_lidar/ --output_folder /media/sdlg/DataSet/myf_kuang/test --num_dirs 5

import json,os
from tqdm import tqdm
import datetime
import numpy as np
import open3d as o3d
import argparse,random
def parse_config():
    parser = argparse.ArgumentParser(description = "convert pcd to bin,save all col")
    parser.add_argument("--input_folder",help="pcd file dir",type=str,default=None)
    parser.add_argument("--output_folder",help="pcd save dir",type=str,default=None)
    parser.add_argument("--num_dirs",help="num of dirs",type=int,default=5)

    args = parser.parse_args() 
    return args

def read_pcd_file(pcd_file):
    pt = np.array(o3d.io.read_point_cloud(pcd_file,remove_nan_points=True).points,dtype=np.float32)
    return pt

def split_list(lst, n):
    # 计算每个子列表的平均长度
    avg_length = len(lst) // n
    remainder = len(lst) % n

    result = []
    start = 0
    for i in range(n):
        length = avg_length + (1 if i < remainder else 0)
        result.append(lst[start:start + length])
        start += length

    return result

def get_subdirectories(folder_path):
    subdirectories = []
    for filename in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, filename)):
            subdirectories.append(filename)
    return subdirectories
def get_processed_pcd_file(input_folder):
    dirs = get_subdirectories(input_folder)
    allpcds = []
    for dir in dirs:
        subdirs = []
        for root,_,files in os.walk(os.path.join(input_folder,dir)):
            for file in files:
                if file.endswith(".pcd"):
                    subdirs.append(os.path.join(root,file)) 
        # 每隔几张筛选一张
        allpcds.extend(subdirs[::1])

    random.shuffle(allpcds)
    return allpcds

def write_pcd_file(pt,output_folder,file_name):
    # 创建 PointCloud 对象
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(pt)

    # 保存为 PCD 文件
    o3d.io.write_point_cloud(os.path.join(output_folder,file_name), pcd)


def main():
    args = parse_config()
    input_folder = args.input_folder
    output_folder = args.output_folder

    allpcds = get_processed_pcd_file(input_folder)

    sublists = split_list(allpcds,args.num_dirs) 
    folder_name = input_folder.split('/')[-1]
    for i,sublist in enumerate(sublists):
        print("start write sublist %d"%i)
        directory_path = os.path.join(output_folder, folder_name+"_processed_pcd_%d"%i)

        if not os.path.exists(directory_path):
        # 如果不存在，则创建目录
            os.makedirs(directory_path)
            print("create directory %s"%directory_path)
        print("sublist %d has %d pcd files"% (i, len(sublist)))
        # 获取当前日期
        current_date = datetime.date.today()

        for j, pcd_file in tqdm(enumerate(sublist), desc="Processing", unit="item"):
            pt = read_pcd_file(pcd_file)
            write_pcd_file(pt,directory_path, "%s_processed_pcd%d_%d.pcd"%(str(folder_name), i, j))
        print("end write sublist %d"%i)
    print("end write all pcd files")

#    for index, item in tqdm(enumerate(my_list), desc="Processing", unit="item"):

if __name__ == "__main__":
    main()
