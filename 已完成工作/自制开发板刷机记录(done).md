# <div align='center'>开发板刷机记录</div>
#### <p align = "center">马玉峰📜</p>

## <div align = 'center'>制作系统镜像</div>
### 1.使用DD命令制作镜像
- 在ORIN上，将镜像拷贝到其他硬盘或U盘
```bash
#以下两个任选其一，制作时间约半小时
sudo dd if=/dev/mmcblk0p1 of=/path/to/save/orin_raw.img 
sudo dd if=/dev/mmcblk0p1 |gzip > /path/to/save/orin.img #压缩格式镜像，省空间  
#注意：不能放到系统盘内
```
- #若无额外硬盘，可通过将自己电脑与orin使用ssh连接，将生成的镜像文件直接拷贝到自己电脑中。
```bash
sudo dd if=/dev/mmcbl0p1 |ssh sdlg@192.168.1.102 dd of=/path/to/save/orin_raw.img
#将sdlg@192.168.1.102替换为自己主机IP和名字，地址替换为自己电脑的储存位置
```

### 2.使用制作的镜像进行刷机

- 打开官方的刷机包，替换原镜像
```bash
#确保镜像制作过程无错误且原镜像存储在个人主机中
cd Linux_for_Tegra
sudo rm bootloader/system.img
sudo ln -s /path/to/orin.img bootloader/orin.img
```
- 刷机
```bash
#USB连接ORIN和个人主机，确认orin处于recovery模式，开始刷机
sudo ./flash.sh -r jetson-agx-orin-devkit mmcblk0p1
```



----
## <div align = 'center'>Orin刷机记录</div>
##### <div align = 'center'>2023年09月14日</div>

- Orin接到自制底板，连接主机无反应，lsusb不显示设备。
- 随即将nvidia官方orin soc拆下，换上我们的soc，刷机成功，并成功安装jetpack5.1.2.刷机过程如下：

    - 下载 NVIDIA 官方jetpack 包 [L4T35.3.1](https://developer.nvidia.com/embedded/jetson-linux-r3531),下载其中的drive和system两个压缩文件。
    - 解压系统文件并刷机
        ```bash
        # 解压到Linux_for Tegra
        tar xf Jetson_Linux_R35.3.1_aarch64.tbz2
        sudo tar xpf Tegra_Linux_Sample-Root-Filesystem_R35.3.1_aarch64.tbz2 -C Linux_for_Tegra/rootfs

        cd Linux_for_Tegra
        # 执行刷机前准备
        sudo ./apply_binaries.sh
        sudo ./tools/l4t_flash_prerequisites.sh
        # 确认orin处于recovery模式，开始刷机
        sudo ./flash.sh jetson-agx-orin-devkit internal
        ```
    - 重启设备，进入系统，初始化，安装Jetpack
        ```bash
        sudo apt install nvidia-jetpack
        # 网络很慢，耐心等待
        ```
    - 问题1 ：storage info error。L4T版本过低，更换版本解决。

- 将刷好机的Orin更换到自制底板上，启动失败，无法进入系统，待解决。

    

-----
## <div align = 'center'>Xaiver刷机记录</div>
##### <div align = 'center'>2023年04月</div>

## 使用官方SDK_Manager（失败）
- 下载困难
- 安装慢，制作镜像中间会断开usb连接导致失败
- 使用麻烦，每次需登录NVIDIA
- 使用自制板刷 jetpack45、50都失败，卡在刷SDK。
- 使用图为控制器刷jetpack45，USB无法使用，刷jetpack50，正常使用。

## 制作a04镜像通过脚本刷机 
```bash
sudo ./flash.sh -r -k APP -G a04.img jetson-xavier mmcblk0p1
sudo ./flash.sh -r jetson-xavier mmcblk0p1
## 如果是orin，设备名换成jetson-agx-orin-devkit
```

- 使用a03的包制作镜像+刷机，失败，无法进去系统。
- 使用jetpack45包制作镜像+刷机，失败，无法使用USB。
- 使用jetpack44包制作镜像+刷机，失败，无法使用USB。
- 使用孙军制作的镜像+jetpack44包+a03db，成功。
- 使用孙军制作的镜像+jetpack44包+44中的db，失败，USB无法使用。
- 使用jetpack45包制作镜像+a03db刷机，成功。
- USB可正常使用，以太网无法使用。
