#!/usr/bin/env python
# coding=utf-8
import numpy as np
import os
import argparse
import open3d as o3d

def parse_config():
    parser = argparse.ArgumentParser(description = "convert pcd to bin,save all col")
    parser.add_argument("--pcd_file_path",help="pcd file dir",type=str,default=None)
    parser.add_argument("--save_bin_path",help="bin save dir",type=str,default=None)

    args = parser.parse_args()
    return args

def read_pcd_file_bin(file_path):
    point_cloud_data = o3d.io.read_point_cloud(file_path)
    point_cloud_array = np.array(point_cloud_data.points)
    return point_cloud_array

def save_bin_file(pcd_file_path,save_bin_path):
    if not os.path.exists(save_bin_path):
        os.makedirs(save_bin_path)
        print("save bin directory created")

    for root,_,files in os.walk(pcd_file_path):
        for filename in files:          
            pcd_file = os.path.join(root,filename)
            point_cloud_array = read_pcd_file_bin(pcd_file)
            if point_cloud_array.shape[1] == 3:
                save_point = np.insert(point_cloud_array[:,:3],3,0,axis=1).astype(np.float32)
                # save_points = np.insert(pt[:,:3],3,0,axis=1).astype(np.float32)

            bin_file_name = save_bin_path + filename.split('.')[0] + ".bin"
            print(bin_file_name)
            save_point.tofile(bin_file_name)

def main():
    args = parse_config()
    print("start pcd to bin ### ")
    save_bin_file(args.pcd_file_path, args.save_bin_path)

if __name__ == "__main__":
    main()


