# <div align='center'> 安装openpcdet 与 cuda_pointpillars </div>

#### <p align = "center"> 马玉峰📜 </p>

- 之前装成功过，环境更换后spconv库与pytorch、pcdet版本不匹配，出现各种问题，故重装


## 第一，安装OpenPCDet

- git clone OpenPCDet （可根据需求选择不同的分支版本,我使用版本基于commit 633db6bea843f8422382fc0ce5fd519fd264184d）
- 安装pytorch，1.10
    ```bash
    # 请自行按网速和源选择合适的安装方式，以下为官网安装。
    pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 -f https://download.pytorch.org/whl/cu111/torch_stable.html
    ```
- 安装spconv （pip） 
    ```bash
    pip install spconv-cu111 #这会安装spconv2
    pip install -r requirements.txt
    python setup.py develop
    ```

## 第二，安装CUDA_POINTPILLARS

- git clone 即可  
- 使用附带的工具，将模型转化为onnx格式，注意使用时params文件也需要一并复制。
- 运行需满足 cuda、tensorrt的版本要求。
