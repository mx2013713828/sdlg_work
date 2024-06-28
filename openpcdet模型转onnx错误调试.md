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

### 错误原因

```python
# simplify_onnx.py 
def simplify_postprocess(onnx_model, FEATURE_SIZE_X, FEATURE_SIZE_Y, NUMBER_OF_CLASSES):
  print("Use onnx_graphsurgeon to adjust postprocessing part in the onnx...")
  graph = gs.import_onnx(onnx_model)

  cls_preds = gs.Variable(name="cls_preds", dtype=np.float32, shape=(1, int(FEATURE_SIZE_Y), int(FEATURE_SIZE_X), 2*NUMBER_OF_CLASSES*NUMBER_OF_CLASSES))
  box_preds = gs.Variable(name="box_preds", dtype=np.float32, shape=(1, int(FEATURE_SIZE_Y), int(FEATURE_SIZE_X), 14*NUMBER_OF_CLASSES))
  dir_cls_preds = gs.Variable(name="dir_cls_preds", dtype=np.float32, shape=(1, int(FEATURE_SIZE_Y), int(FEATURE_SIZE_X), 4*NUMBER_OF_CLASSES))

```

上述代码中的cls_preds、box_preds、dir_cls_preds的形状需和训练时保持一致。
训练时，参数文件中的参考anchor数 * 2 = anchors 
之所以此处使用2 * NUMBER_OF_CLASSES * NUMBER_OF_CLASSES，是因为训练时对于每一类都设置一个anchor。
报错就是因为训练时没有对每一类设置一个参考anchor。
