# <div align='center'> pth转onnx报错 </div>
  
<div align = "center"> <img src="https://pic.imgdb.cn/item/65dc5dfc9f345e8d03446103.png" height=100 width=300> </div>

#### <p align = "center">![Static Badge](https://img.shields.io/badge/mayufeng-blue?style=flat&label=Author)![Static Badge](https://img.shields.io/badge/2024/05/21-blue?style=flat&label=CreateTime)![Static Badge](https://img.shields.io/badge/97357473@qq\.com\-blue?style=flat&label=Email)</p>

---

### 错误日志

```bash

corrupted double-linked list
[1]    18532 abort (core dumped)  python exporter.py --cfg  --ckpt

```

### 实验过程

- 测试1：训练使用8类，构建数据集使用8类

错误依然存在

- 测试2：训练使用7类，构建数据集使用7类

可以训练且导出onnx模型

- 测试3：使用test20训练模型和test18的参数

可以导出，但是检测无结果

- 测试4：训练使用7类，构建数据集8类

可以导出
