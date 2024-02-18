# 点云标注工具调查研究
#### <p align = "center">马玉峰📜</p>

## 目录

- [开源工具](#div-aligncenter开源工具div)
    - [labelcloud](#div-alignleft-labelcloud-div)
- [国内商业软件](#div-aligncenter-国内商业软件-div)
    - [曼浮](#曼浮)
    - [倍赛](#倍赛)

- [国外商业软件](#div-aligncenter国外商业软件div)
    - [supervisely](#supervisely)
## <div align='center'> 开源工具 </div>

### <div align='left'> labelcloud </div>

[labelcloud](https://github.com/ch-sa/labelCloud.git)类似于labelimg，是最早一批的开源点云标注工具。

![labelcloud](./images/labelcloud01.gif)

优点：

- 安装方便
- 本机操作
- 导出格式齐全

缺点：

- 操作不方便（缩放慢、选择难）
- 不清晰（点云显示分辨率低，无法精确分割）
- 单框标注约3~5分钟
### PCAT

[PCAT](https://github.com/Qjizhi/point_cloud_ros_annotation_tool) 是个人开发的项目，基于ROS，可以同时显示图片与点云，方便标注。

![pcat](./images/pcat01.png)

优点：

- 本机安装
- 同时显示图片，辅助标注

缺点：

- 安装复杂，需先安装ros、python和相关依赖
- 操作繁琐，标注一个框约需3~5分钟
- 导出格式单一


## <div align='center'> 国内商业软件 </div>

### 曼浮

[曼浮](mindflow.com.cn/)是国内的标注厂家，目前价格和服务方式未知，已留联系方式。

### 倍赛

[倍赛](https://www.basicfinder.com/tools)是国内的标注厂家，目前价格和服务方式未知。


## <div align='center'>国外商业软件</div>

### supervisely

[supervisely](https://supervisely.com/)是国外的一款在线数据管理平台，包含数据采集、标注、训练的全流程。

![supervisely](./images/supervisely.png)

优点：
- 三维视图标注，标注结果清晰可见
- 操作简单、人性化（标注单框约1~2分钟）
- 导出格式齐全
- 不需安装配置，直接使用

缺点：
- 需翻墙使用，网页加载速度不稳定
- 在线标注，数据需上传至网站
- 正式版付费使用
