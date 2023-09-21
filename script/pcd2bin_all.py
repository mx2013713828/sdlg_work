#!/usr/bin/env python
# coding=utf-8
import numpy as np
import os
import argparse

def parse_config():
    parser = argparse.ArgumentParser(description = "convert pcd to bin,save all col")
    parser.add_argument("--pcd_file_path",help="pcd file dir",type=str,default=None)
    parser.add_argument("--save_bin_path",help="bin save dir",type=str,default=None)

    args = parser.parse_args()
    return args

#read pcd file 
def read_pcd_file(file_path):
    with open(file_path,'r') as file:
        lines = file.readlines()

    data_start_line = 0
    for i,line in enumerate(lines):
        if line.startswith('DATA'):
            data_start_line = i + 1
            break

    point_cloud_data = []
    for line in lines[data_start_line:]:
        values = line.strip().split()
        point_cloud_data.append(values)

    point_cloud_array = np.array(point_cloud_data,dtype=np.float32)

    return point_cloud_array

def save_bin_file(pcd_file_path,save_bin_path):
    if not os.path.exists(save_bin_path):
        os.makedirs(save_bin_path)
        print("save bin directory created")

    for root,_,files in os.walk(pcd_file_path):
        for filename in files:
            
            pcd_file = os.path.join(root,filename)
            point_cloud_array = read_pcd_file(pcd_file)
            bin_file_name = save_bin_path + filename.split('.')[0] + ".bin"
            

            point_cloud_array.tofile(bin_file_name)

def main():
    args = parse_config()
    print("start pcd to bin ### ")
    save_bin_file(args.pcd_file_path, args.save_bin_path)

if __name__ == "__main__":
    main()


