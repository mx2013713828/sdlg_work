# openvino安装与部署 


## openvino安装

使用pip安装
```bash
pip install openvino-dev[tensorflow2,pytorch,ONNX]==2022.1.0
```
版本可自行选择，但是openvino的高版本对低版本缺乏兼容性，项目与环境版本不同很容易报错。

## YOLOV5-lite openvino部署

### pt模型转化成
```bash
$ python models/export.py --weights v5lite-c.pt --img 640 --batch 1
$ python -m onnxsim v5lite-c.onnx v5lite-c-sim.onnx
```
###	转化 to IR model
```bash
mo --input_model v5lite-c.onnx -s 255 --data_type FP16  --reverse_input_channels --output Conv_462,Conv_478,Conv_494
```

###	Inference
有xml和bin文件后就可以进行推理了。
```bash
python openvino.py -m v5lite-c.xml -i bike.jpg
```

## openvino版本不同造成的问题
2021.3 和 2022.1版本不同，需要改动一些属性和方法。

```python
# out_blob_n, out_blob_c, out_blob_h, out_blob_w = blob.shape
out_blob_n, out_blob_c, out_blob_h, out_blob_w = blob._initial_shape
```
```python
predictions = 1.0 / (1.0 + np.exp(-blob.buffer))
```
```python
# net = IENetwork(model=model_xml, weights=model_bin)
net = ie.read_network(model=model_xml, weights=model_bin)
```
```python
# n, c, h, w = net.inputs[input_blob].shape
n, c, h, w = net.input_info[input_blob].input_data.shape
```
```python
# out_blob.shape = layer_params[0]
out_blob.set_shape(layer_params[0])
```
```python
# output = exec_net.requests[cur_request_id].outputs
output = exec_net.requests[cur_request_id].output_blobs
```

## 1.安装openvino2022.1（安装包已下载）
- 1 sudo chmod 777 l_openvino_toolkit_p_2022.1.0.643_offline.sh
- 2 ./l_openvino_toolkit_p_2022.1.0.643_offline.sh (默认安装位置是/home/用户名/intel/)
- 3 cd /home/tron/intel/openvino_2022.1.0.643/install_dependencies 
- 4 ./install_openvino_dependencies.sh  (不执行该步骤应该也没问题)
- 5 cd /home/tron/intel/openvino_2022.1.0.643/extras/scripts
- 6 ./download_opencv.sh (此步骤安装opencv)
    
## 2. 配置openvino运行环境
- 1 sudo gedit ~/.bashrc 末尾添加 source /home/tron/intel/openvino_2022/setupvars.sh
- 2 source ~/.bashrc
- 3 
```console
  sudo gedit /etc/ld.so.conf
```
  添加如下3条：
  
`/home/myf/intel/openvino_2022/runtime/lib/intel64/
/home/myf/intel/openvino_2022/runtime/3rdparty/tbb/lib/
/home/myf/intel/openvino_2022/extras/opencv/lib/`
- 4 
```console
sudo ldconfig
```


## 3. 错误总结

#### （1）安装方式最好选用离线安装，2022.1以后的是sh安装包，带gui界面，使用方便，而且再安装opencv时候也简单。前面用github源码编译，搞了半天还是不行，而且还要自己安装opencv，配置麻烦。
#### （2）C++代码需要编译，在makefile中指定使用库的路径（推理引擎、opencv、第三方库等）。
#### （3）使用模型优化器MO的时候，使用yolov5-6.1版本的代码，适配C++的runtime代码。
#### （4）计算推理时间用chrono，推理时间一般是包含nms.
#### （5）C++ 设置输入参数方式

```c++
int main(int argc,char ** argv){

    // Step 1. Initialize OpenVINO Runtime core
    ov::Core core;
    // Step 2. Read a model
    string modelname = argv[1];
    // std::shared_ptr<ov::Model> model = core.read_model("../../model/v5lite-c.xml");
    std::shared_ptr<ov::Model> model = core.read_model(modelname);
    // Step 3. Read input image
    string imgname = argv[2] ;
    // ../../imgs/bike.jpg
    cv::Mat img = cv::imread(imgname);
```
