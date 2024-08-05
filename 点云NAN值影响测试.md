# <div align='center'> ⭐点云NAN值影响测试⭐ </div>

<div align = "center"> <img src="https://pic.imgdb.cn/item/65dc5dfc9f345e8d03446103.png" height=100 width=300> </div>

#### <p align = "center">![Static Badge](https://img.shields.io/badge/mayufeng-blue?style=flat&label=Author)![Static Badge](https://img.shields.io/badge/2024/07/30-blue?style=flat&label=CreateTime)![Static Badge](https://img.shields.io/badge/97357473@qq\.com\-blue?style=flat&label=Email)</p>

---

## Table of Contents

- [Pth模型测试](#pth模型测试)
- [Onnx模型测试](#onnx模型推理)


## pth模型测试

#### 含NAN值

points number :(191646, 5)
[0.9474 ]
!['pth'](./images/test_pcdnan/pth.png)

points number :(191646, 5)
[0.9599, 0.2307]
!['pth1'](./images/test_pcdnan/pth1.png)

points number :(191646, 5)
[0.9540 ]
!['pth2'](./images/test_pcdnan/pth2.png)

#### 去除NAN值

points number :(141392, 5)
[0.9474 ]
!['pth_nonan'](./images/test_pcdnan/pth_nonan.png)

points number :(142259, 5)
[0.9599, 0.2307]
!['pth_nonan1'](./images/test_pcdnan/pth_nonan1.png)

points number :(142283, 5)
[0.9540 ]
!['pth_nonan2'](./images/test_pcdnan/pth_nonan2.png)


## onnx模型推理

#### 含NAN值

points num: 191646
[0.94728 ] 
!['onnx_nan'](./images/test_pcdnan/onnx.png)

points num: 191646
[0.959781, 0.223741 ]
!['onnx_nan1'](./images/test_pcdnan/onnx1.png)

points num: 191646
[0.953865 ]
!['onnx_nan2'](./images/test_pcdnan/onnx2.png)


#### 去除NAN值


points num: 141392
[0.94728 ]
!['onnx_nonan'](./images/test_pcdnan/onnx_nonan.png)

points num: 142259
[0.959779 ,0.22388 ]
!['onnx_nonan1'](./images/test_pcdnan/onnx_nonan1.png)

points num: 142283
[0.953866 ]
!['onnx_nonan2'](./images/test_pcdnan/onnx_nonan2.png)
