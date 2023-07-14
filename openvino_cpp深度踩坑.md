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
