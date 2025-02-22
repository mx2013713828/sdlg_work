# <div align='center'> ⭐Cuda-Centerpoint部署流程⭐ </div>
  
<div align = "center"> <img src="https://pic.imgdb.cn/item/65dc5dfc9f345e8d03446103.png" height=100 width=300> </div>

#### <p align = "center">![Static Badge](https://img.shields.io/badge/mayufeng-blue?style=flat&label=Author)![Static Badge](https://img.shields.io/badge/2024/08/05-blue?style=flat&label=CreateTime)![Static Badge](https://img.shields.io/badge/97357473@qq\.com\-blue?style=flat&label=Email)</p>

---

### 针对使用OpenPCDet和自制数据集训练的Centerpoint 

- get official pth model   

    1. 更改configs nusc_centerpoint_voxelnet_0075voxel_fix_bn_z_custom.py , 参数和openpcdet中保持一致 
    2. 运行export_neck_head.py 获取test32_centerpoint_official.pth

        ```bash

        python centerpoint-export/export_neck_head.py --config configs/myf_kuang/nusc_centerpoint_voxelnet_0075voxel_fix_bn_z_custom.py --checkpoint ../model/pth/changed2official_test32_checkpoint_epoch_20.pth --save-onnx rpn_centerhead_sim_myfkuang.onnx --input_channel 4
        ```

- 运行 export-scn.py 获取scn.onnx

    ```bash
    python centerpoint-export/export-scn.py --ckpt ../model/pth/changed2official_test32_checkpoint_epoch_20.pth --save-onnx scn.nuscenes-test32.onnx --in-channel 4
    ```

- 运行 export_neck_head.py 获取rpn.onnx

    ```bash 
    python centerpoint-export/export_neck_head.py --config configs/myf_kuang/nusc_centerpoint_voxelnet_0075voxel_fix_bn_z_custom.py --checkpoint ../model/pth/changed2official_test32_checkpoint_epoch_20.pth --save-onnx rpn_centerhead_sim_myfkuang.onnx --input_channel 4
    ```

- 运行 build.trt.sh 获取rpn.plan

    ```bash
    bash tool/build.trt.sh
    ```

- 更改 main.cpp 和 centerpoint.cpp 中的 rpn_centerhead_sim.plan、centerpoint.scn.onnx 路径。

- 编译运行

    ```
    $ mkdir -p build && cd build
    $ cmake .. && make -j
    $ ./centerpoint ../data/test/ --verbose
    ```