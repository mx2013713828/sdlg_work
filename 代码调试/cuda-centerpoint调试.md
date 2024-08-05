
# <div align='center'> ⭐Cuda-Centerpoint调试⭐ </div>
  
<div align = "center"> <img src="https://pic.imgdb.cn/item/65dc5dfc9f345e8d03446103.png" height=100 width=300> </div>

#### <p align = "center">![Static Badge](https://img.shields.io/badge/mayufeng-blue?style=flat&label=Author)![Static Badge](https://img.shields.io/badge/2024/07/02-blue?style=flat&label=CreateTime)![Static Badge](https://img.shields.io/badge/97357473@qq\.com\-blue?style=flat&label=Email)</p>

---

## Table of Contents

- [ChangeLog](#changelog)
- [Install](#install)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## 使用代码库提供的模型和参数跑通代码

1. 下载模型和参数
2. 代码调试
    - 报错编译报错,spconv库依赖libprotoc库特定版本,已解决
    - 模型参数加载报错,模型参数加载失败,模型定义时模型名字与提供模型定义名不一致，已解决
3. 运行成功,官方代码和模型已调试成功.

## 转化openpcdet(once)版本CenterPoint模型

1. 下载openpcdet(once)版本CenterPoint模型

2. 转化3D卷积层 export scn

    1. 问题1:模型层名字和官方版本不一致，如何转化？
        - 将openpcdet版本pth中的模型名字修改为和官方版本一致
        - 将openpcdet版本pth模型中的参数值复制到官方版本pth模型中
    2. 问题2:模型头部，nuscences是6个头，自制数据集头数不一致如何操作？

    3. 转换官方模型成功。

3. 转化瓶颈层和检测头 export head

    1. 转换官方模型成功
    2. 问题3:官方模型使用nuscense，点云为N * 5,(x, y, z, intensity, ring index)
        - 自制数据集只有x,y,z三维,可能需要额外添加一个维度,或者模型转化时强制使用4个维度.
        - 必须：模型和输入输入维度匹配，输入维度和VFE函数参数匹配。注意！！！
    3. 问题4:neck.deblocks.0.0.weight 尺寸不匹配
        - Openpcdet 版本为torch.Size([128, 256, 1, 1])
        - 官方版本为torch.Size([256, 128, 1, 1])
        - 已解决。
    4. Openpcdet 版本Centerpoint结构错误
    Openpcdet中的base_bev_backbone.py BaseBEVBackbone结构有错误，导致产生两个上采样层(转置卷积)（Centerpoint中是一个下采样层，另一个下采样使用卷积层代替）
        - 已解决

