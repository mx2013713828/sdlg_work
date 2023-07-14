# 编译hdl_graph_slam 踩坑！！！
## 1）环境
我使用环境为ubuntu20.04 + ros noetic，anaconda3 ，8G内存8700K CPU。

## 2）编译错误
- eigen 目录问题，安装eigen时目录如果是 ` /usr/local/include/eigen3 `，在编译时候会出现错误，找不到eigen3,只需设置一个软链接即可。

设置软链接： `ln -s /usr/local/include/eigen3 /usr/include/eigen3`

- python冲突，`Unable to find either executable ‘empy’ or Python module ‘em’… try`，此错误一般是由于anaconda导致的python环境错误，编译时指定python目录即可。
  
使用以下命令：`catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3`

- 内存问题，`C++: fatal error: Killed signal terminated program cc1plus`，出现此错误，原因是内存不足，在编译的时候前面打开过多的终端和界面，导致内存不足。
