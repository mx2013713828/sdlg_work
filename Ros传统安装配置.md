# <div align='center'>ROS学习笔记（一）</div>
#### <p align = "center">马玉峰📜</p>
## 1）安装配置

按这个教程安装配置，目前没啥问题，网络慢就换源。

[ROS1 - ubuntu20.04 安装教程](http://wiki.ros.org/cn/noetic/Installation/Ubuntu)

## 2）常用命令
[ROS1 - 常用命令教程](https://www.cnblogs.com/shandianchengzi/p/15232145.html)

    roscore #开启ROS core
    rosrun turtlesim #列出所有可用的turtlesim命令
    rosrun turtlesim turtlesim-node #启动小海龟节点（小海龟仿真器）。
    rosrun turtlesim turtle_teleop_key #启动小海龟的控制节点

ros中的节点是主要操作单位，与Class相似。每个节点有不同的功能，在ROS中称之为service。

    rosnode list、info、ping...... 

    rosservice lise、call、args、info、type......

    rostopic #所谓话题，如/pose（位姿） /cmd_vel（移动）,通过对话题发送消息rostopic pub，进行移动、改变位姿、颜色等等操作。

## 3）注意事项
- 在catkin_make 时候，如果系统是用python3，直接make会出错,使用下面的命令。
- catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
- 重点：ros工作空间，在每次打开终端后都需要先将catkin工作空间添加到ROS环境中，命令如下，后面就可以使用roscd beginner_tutorials 、rospack depends beginner_tutorials等命令了。
```bash
$ . ~/catkin_ws/devel/setup.bash
```
## 4)
- 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  ##github身份验证码
- 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
- ## ROS中通信有Topic和Service两种方式。


  