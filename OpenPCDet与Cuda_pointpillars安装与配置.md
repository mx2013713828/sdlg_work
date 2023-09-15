# <div align='center'> 安装openpcdet 与 cuda_pointpillars </div>

#### <p align = "center"> 马玉峰📜 </p>

- 之前装成功过，环境更换后spconv库与pytorch、pcdet版本不匹配，出现各种问题，故重装


## 第一，安装OpenPCDet

- git clone
- 安装pytorch，1.10
- 安装spconv （pip） 
    ```bash
    pip install spconv-cu111
    pip install -r requirements.txt
    python setup.py develop
    ```

## 第二，安装CUDA_POINT_PILLARS

- git clone 
- 使用附带的工具，将模型转化为onnx格式
