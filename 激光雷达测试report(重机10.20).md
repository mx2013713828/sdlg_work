# <div align="center">⭐激光雷达测试</div>
#### <p align = "center">马玉峰、徐坤📜</p>
----
## 测试前言

#### 测试人员：

- 马玉峰
- 徐坤

#### 测试场景

- 重机宿舍前停车场

#### 测试时间

- 2023.9.23 ~~ 2023.10.12

## 测试过程


### 录制数据

采用手持方式，举高约1.5米作用，在重机宿舍前停车场绕1米半径内录制点云数据包，格式为 ROGBAG.

### 运行点云检测算法

将rosbag转为pcd格式数据，使用基于华为once数据集训练的pointpillar_300模型测试目标检测效果。

## 测试效果

### 禾赛xt16
![xt16a](./images/lidar_test/hs16_detect1.png)
![xt16b](./images/lidar_test/hs16_detect2.png)
![xt16c](./images/lidar_test/hs16_detect3.png)
![xt16d](./images/lidar_test/hs16_detect4.png)

### 禾赛xt32
![xt32a](./images/lidar_test/hs32_detect1.png)
![xt32b](./images/lidar_test/hs32_detect2.png)
![xt32c](./images/lidar_test/hs32_detect3.png)
![xt32d](./images/lidar_test/hs32_detect4.png)
![xt32e](./images/lidar_test/hs32_detect5.png)

### 速腾32线

![rs32a](./images/lidar_test/rs32_detect1.png)
![rs32b](./images/lidar_test/rs32_detect2.png)
![rs32c](./images/lidar_test/rs32_detect3.png)
![rs32d](./images/lidar_test/rs32_detect4.png)

### 速腾M1

![m1a](./images/lidar_test/m1_detect1.png)
![m1b](./images/lidar_test/m1_detect2.png)
![m1c](./images/lidar_test/m1_detect3.png)
![m1d](./images/lidar_test/m1_detect4.png)
![m1e](./images/lidar_test/m1_detect5.png)

## 测试总结

- xt16线雷达线束稀疏，10米外基本检测不到。
- xt32、HS32 效果差不多，满足需求。
- M1检测距离远、精度高，满足需求。