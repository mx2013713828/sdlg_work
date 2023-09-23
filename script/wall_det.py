#!/usr/bin/env python
# coding=utf-8
# 挡墙检测算法
# 点云按角度分组，角度θ上的点存在高度差，连续最大子串和 > height的认为是在障碍物上的点。其余的则认为是地面。通过控制height参数，来区分普通障碍物与挡墙。
# 待优化：多个角度上的线合并成一组，提高检测鲁棒性。增加检测逻辑，存在高度差之外，还需判断相邻点的水平距离。
import open3d as o3d
import numpy as np
import math
from collections import defaultdict
import argparse

def parse_config():
    parser = argparse.ArgumentParser(description= "dosmt")
    parser.add_argument("--file_path",help="pcd or bin file_path",default='/home/sdlg/mayufeng/SdlgProject/PointCloutProject/walldet/data/hesaipcd/PointCloudFrame10.pcd')
    parser.add_argument("--angular_res",help="angular_resolution",default=0.18)
    parser.add_argument("--height",help="max sum height_diff",default=0.3)
    parser.add_argument("--delta_h",help="min delta height_diff",default=0.03)
    args = parser.parse_args()
    return args
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

def read_bin_file(file_path):
    points = np.fromfile(file_path, dtype=np.float32).reshape(-1,4)
    return points

def showpcd(point_cloud_array,ext1=None,ext2=None):
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.get_render_option().point_size = 2.0
    vis.get_render_option().background_color = np.array([0.7, 0.7, 0.7])
    pts = o3d.geometry.PointCloud()

    pts.points = o3d.utility.Vector3dVector(point_cloud_array[:,:3])
    vis.add_geometry(pts)
    pts.paint_uniform_color([1,1,0])

    if type(ext1) == np.ndarray:
        
        pts_ext1 = o3d.geometry.PointCloud()
        pts_ext1.points = o3d.utility.Vector3dVector(ext1[:,:3])
        pts_ext1.paint_uniform_color([1,0,0])
        vis.add_geometry(pts_ext1)
    vis.run()
    vis.destroy_window()    

    
# 求连续非零子串的最大和。
def max_diff_sum(nums):
    if not nums:
        return 0
    max_sum = current_sum = 0
    for num in nums:
        if num >= -0.02:
            current_sum = current_sum + num
            max_sum = max(current_sum,max_sum)
        else:
            current_sum = 0
            
    return max_sum

# 求两个点云的XOY水平距离
def distance_xoy(point1,point2):
    return (((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5)

def wall_seg(sample_data,angular_res=0.18, height=0.3, delta_h=0.03):
    horizontal_angles = dict()
    for i,point in enumerate(sample_data):
        horizontal_angle = np.arctan2(point[1],point[0])
        horizontal_angle = np.degrees(horizontal_angle)
        horizontal_angles[i] = round(horizontal_angle, 2)

    angular_resolution = angular_res #参数 水平角分辨率
    angle_to_points = defaultdict(list) #存储格式 (key=角度分组，value=点云序号)

    for point_index,angle in horizontal_angles.items():
        group_index = int(angle / angular_resolution)
        angle_to_points[group_index].append(point_index)        
# 创建一个字典来存储每个分组中相邻点云的高度差
    group_points =list()
    p_wall = list()
    p_boundary = list()
    
    # 遍历每个分组
    for group_index, point_indices in angle_to_points.items():
        # 遍历每个分组中的点云,对每个角度分组中的点云进行处理，筛选疑似打在墙上的点
        group_diffs = dict()
        #解决两端问题
        for i,index in enumerate(point_indices[:-1]):
            # 计算相邻点的高度差（假设Z坐标表示高度）,最下方的线束，将其delta_h设为0
            height_diff = sample_data[point_indices[i]][2] - sample_data[point_indices[i+1]][2]
    #         height_differences[group_index].append(height_diff)
            group_diffs[index] = height_diff
        group_diffs[point_indices[-1]] = 0
        # 处理点集

        #判断连续点的最大高度差，超过阈值的采取，否则抛弃。
        #优化方案：将遮挡物按高度不同划分组，点云使用不同颜色。
        if max_diff_sum(group_diffs.values()) < height:  # 参数，最大连续子串和，可以近似理解为要检测的墙的最低高度。
            #从这里的点集中选取点
            continue

        for point_indices, height_diff in group_diffs.items():

            if height_diff > delta_h : #此处为参数 delta_h
    #             if distance_xoy(sample_data[i],sample_data[i+1]) < 0.5:
    #                 p_wall.append(sample_data[point_indices])
    
                p_wall.append(sample_data[point_indices])

    p_wall = np.array(p_wall) 
    
    return p_wall,p_boundary
    
def main():
    print("start process")

    args = parse_config()
    sample_data = read_pcd_file(args.file_path)
    
    p_wall,_ = wall_seg(sample_data,args.angular_res,args.height, args.delta_h)
    showpcd(p_wall)

    print("end process")


if __name__=='__main__':
    main()
