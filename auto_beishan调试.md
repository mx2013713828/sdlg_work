# <div align="center">⭐AUTO_BEISHAN 代码运行退出错误整理</div>
### <p align = "center">马玉峰📜</p>
----

- [后雷达断开导致程序退出（未解决）](#后雷达断开导致程序退出未解决)
- [融合部分报错(未复现)](#融合部分报错)
- [opencv-dnn导致冲突(未解决)](#opencv-dnn-错误)
- [yolov8dnn导致冲突（已解决）](#yolov8dnn--点云推理-报错六小时以上会出现)
- [禾赛sdk-多个主机IP相同导致退出](#禾赛sdk-多个主机间ip冲突影响雷达数据传输)
- [禾赛sdk错误(已解决)](#禾赛sdk错误)
- [yolov5lite与点云冲突(已解决)](#运行图像推理yolov5lite-与-点云推理-报错)
- [多线程显存分配导致冲突(已解决)](#显存冲突)
- [yolov3DNN与点云冲突(未解决)](#运行点云与yolov3_dnn-推理报错)
- [单独运行yolov5lite导致退出(已解决)](#单独运行图像推理yolov5lite-报错)

----

## 后雷达断开导致程序退出（未解决）
```bash
(gdb) bt
#0  0x0000aaaaaab59e94 in __gnu_cxx::new_allocator<PointXYZIRT>::construct<PointXYZIRT, PointXYZIRT&>(PointXYZIRT*, PointXYZIRT&)
    (this=0xffff28000b98, __p=0xfffe6e37e000) at /usr/include/c++/9/ext/new_allocator.h:146
#1  0x0000aaaaaab54b90 in std::allocator_traits<Eigen::aligned_allocator<PointXYZIRT> >::_S_construct<PointXYZIRT, PointXYZIRT&>(Eigen::aligned_allocator<PointXYZIRT>&, PointXYZIRT*, PointXYZIRT&) (__a=..., __p=0xfffe6e37e000) at /usr/include/c++/9/bits/alloc_traits.h:244
#2  0x0000aaaaaab4e978 in std::allocator_traits<Eigen::aligned_allocator<PointXYZIRT> >::construct<PointXYZIRT, PointXYZIRT&>(Eigen::aligned_allocator<PointXYZIRT>&, PointXYZIRT*, PointXYZIRT&) (__a=..., __p=0xfffe6e37e000) at /usr/include/c++/9/bits/alloc_traits.h:350
#3  0x0000aaaaaab45bf4 in std::__uninitialized_copy_a<PointXYZIRT*, PointXYZIRT*, Eigen::aligned_allocator<PointXYZIRT> >(PointXYZIRT*, PointXYZIRT*, PointXYZIRT*, Eigen::aligned_allocator<PointXYZIRT>&) (__first=0xffff4faf2000, __last=0xffff7afb5010, __result=0xfffe6707b010, __alloc=...)
    at /usr/include/c++/9/bits/stl_uninitialized.h:293
#4  0x0000aaaaaac94730 in std::vector<PointXYZIRT, Eigen::aligned_allocator<PointXYZIRT> >::_M_allocate_and_copy<PointXYZIRT*>(unsigned long, PointXYZIRT*, PointXYZIRT*) (this=0xffff28000b98, __n=17646080, __first=0xffff487ef010, __last=0xffff7afb5010)
    at /usr/include/c++/9/bits/stl_vector.h:1511
#5  0x0000aaaaaac8e824 in std::vector<PointXYZIRT, Eigen::aligned_allocator<PointXYZIRT> >::_M_assign_aux<PointXYZIRT*>(PointXYZIRT*, PointXYZIRT*, std::forward_iterator_tag) (this=0xffff28000b98, __first=0xffff487ef010, __last=0xffff7afb5010) at /usr/include/c++/9/bits/vector.tcc:309
#6  0x0000aaaaaac88f9c in std::vector<PointXYZIRT, Eigen::aligned_allocator<PointXYZIRT> >::_M_assign_dispatch<PointXYZIRT*>(PointXYZIRT*, PointXYZIRT*, std::__false_type) (this=0xffff28000b98, __first=0xffff487ef010, __last=0xffff7afb5010) at /usr/include/c++/9/bits/stl_vector.h:1625
#7  0x0000aaaaaac844cc in std::vector<PointXYZIRT, Eigen::aligned_allocator<PointXYZIRT> >::assign<PointXYZIRT*, void>(PointXYZIRT*, PointXYZIRT*) (this=0xffff28000b98, __first=0xffff487ef010, __last=0xffff7afb5010) at /usr/include/c++/9/bits/stl_vector.h:766
#8  0x0000aaaaaac76fc8 in perception::lidars::Lidars::lidar_callback_b(hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&) (frame=...)
    at sources/lidars/perception.cpp:138
#9  0x0000aaaaaac8897c in std::_Function_handler<void (hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&), void (*)(hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&)>::_M_invoke(std::_Any_data const&, hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&) (__functor=..., __args#0=...)
    at /usr/include/c++/9/bits/std_function.h:300
#10 0x0000aaaaaac8e3cc in std::function<void (hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&)>::operator()(hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&) const (this=0xaaaaba0489a8, __args#0=...) at /usr/include/c++/9/bits/std_function.h:688
#11 0x0000aaaaaac88c8c in hesai::lidar::Hesailidar<PointXYZIRT>::run() (this=0xaaaaba048980) at sources/lidars/hesai/hesai.h:115
#12 0x0000aaaaaacc1624 in boost::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >::operator()(hesai::lidar::Hesailidar<PointXYZIRT>*) const (this=0xaaaaba046148, p=0xaaaaba048980) at /usr/include/boost/bind/mem_fn_template.hpp:49
#13 0x0000aaaaaacc067c in boost::_bi::list1<boost::_bi::value<hesai::lidar::Hesailidar<PointXYZIRT>*> >::operator()<boost::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >, boost::_bi::list0>(boost::_bi::type<void>, boost::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >&, boost::_bi::list0&, int) (this=0xaaaaba046158, f=..., a=...) at /usr/include/boost/bind/bind.hpp:259
#14 0x0000aaaaaacbdda4 in boost::_bi::bind_t<void, boost::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >, boost::_bi::list1<boost::_bi::value<hesai::lidar::Hesailidar<PointXYZIRT>*> > >::operator()() (this=0xaaaaba046148) at /usr/include/boost/bind/bind.hpp:1294
#15 0x0000aaaaaacbb064 in boost::detail::thread_data<boost::_bi::bind_t<void, boost::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >, boo--Type <RET> for more, q to quit, c to continue without paging--
st::_bi::list1<boost::_bi::value<hesai::lidar::Hesailidar<PointXYZIRT>*> > > >::run() (this=0xaaaaba046000)
    at /usr/include/boost/thread/detail/thread.hpp:120
#16 0x0000fffff5cdc624 in  () at /lib/aarch64-linux-gnu/libboost_thread.so.1.71.0
#17 0x0000fffff7e93624 in start_thread (arg=0xfffff5cdc598) at pthread_create.c:477
#18 0x0000ffffe707449c in thread_start () at ../sysdeps/unix/sysv/linux/aarch64/clone.S:78
```

## 融合部分报错

```bash
(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x0000ffffe67e3aac in __GI_abort () at abort.c:79
#2  0x0000ffffe6830f40 in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0xffffe68f2518 "%s\n")
    at ../sysdeps/posix/libc_fatal.c:155
#3  0x0000ffffe6838344 in malloc_printerr (str=str@entry=0xffffe68ee4b0 "malloc(): invalid size (unsorted)") at malloc.c:5347
#4  0x0000ffffe683aedc in _int_malloc (av=av@entry=0xfffecc000020, bytes=bytes@entry=3072000) at malloc.c:3736
#5  0x0000ffffe683c574 in __GI___libc_malloc (bytes=3072000) at malloc.c:3066
#6  0x0000aaaaaab2ad20 in Eigen::internal::aligned_malloc(unsigned long) (size=3072000) at /usr/include/eigen3/Eigen/src/Core/util/Memory.h:159
#7  0x0000aaaaaab69180 in Eigen::aligned_allocator<PointXYZIRT>::allocate(unsigned long, void const*) (this=0xfffedefefb78, num=64000)
    at /usr/include/eigen3/Eigen/src/Core/util/Memory.h:758
#8  0x0000aaaaaab6237c in std::allocator_traits<Eigen::aligned_allocator<PointXYZIRT> >::allocate(Eigen::aligned_allocator<PointXYZIRT>&, unsigned long) (__a=..., __n=64000) at /usr/include/c++/9/bits/alloc_traits.h:305
#9  0x0000aaaaaab5a6ec in std::_Vector_base<PointXYZIRT, Eigen::aligned_allocator<PointXYZIRT> >::_M_allocate(unsigned long)
    (this=0xfffedefefb78, __n=64000) at /usr/include/c++/9/bits/stl_vector.h:343
#10 0x0000aaaaaacf38b8 in std::vector<PointXYZIRT, Eigen::aligned_allocator<PointXYZIRT> >::reserve(unsigned long)
    (this=0xfffedefefb78, __n=64000) at /usr/include/c++/9/bits/vector.tcc:78
--Type <RET> for more, q to quit, c to continue without paging--
#11 0x0000aaaaaae6223c in pcl::transformPointCloud<PointXYZIRT, float>(pcl::PointCloud<PointXYZIRT> const&, pcl::PointCloud<PointXYZIRT>&, Eigen::Transform<float, 3, 2, 0> const&, bool) (cloud_in=..., cloud_out=..., transform=..., copy_all_fields=true)
    at /usr/local/include/pcl-1.8/pcl/common/impl/transforms.hpp:53
#12 0x0000aaaaaae61b24 in pcl::transformPointCloud<PointXYZIRT, float>(pcl::PointCloud<PointXYZIRT> const&, pcl::PointCloud<PointXYZIRT>&, Eigen::Matrix<float, 4, 4, 0, 4, 4> const&, bool) (cloud_in=..., cloud_out=..., transform=..., copy_all_fields=true)
    at /usr/local/include/pcl-1.8/pcl/common/transforms.h:225
#13 0x0000aaaaaae61228 in pcl::transformPointCloud<PointXYZIRT>(pcl::PointCloud<PointXYZIRT> const&, pcl::PointCloud<PointXYZIRT>&, Eigen::Matrix<float, 4, 4, 0, 4, 4> const&, bool) (cloud_in=..., cloud_out=..., transform=..., copy_all_fields=true)
    at /usr/local/include/pcl-1.8/pcl/common/transforms.h:234
#14 0x0000aaaaaae5ecbc in transformPointCloud_pose(boost::shared_ptr<pcl::PointCloud<PointXYZIRT> > const&, Pose) (inputCloud=..., pose=...)
    at sources/lidars/jetpack50/../lidar_utility.h:34
#15 0x0000aaaaaae5eda0 in mergePointClouds(boost::shared_ptr<pcl::PointCloud<PointXYZIRT> > const&, boost::shared_ptr<pcl::PointCloud<PointXYZIRT> > const&, boost::shared_ptr<pcl::PointCloud<PointXYZIRT> > const&, Pose, Pose, Pose)
    (mainCloud=..., leftCloud=..., rightCloud=..., pose_left=..., pose_right=..., pose_car=...)
    at sources/lidars/jetpack50/../lidar_utility.h:44
#16 0x0000aaaaaae60614 in CudaPointpillars::task() (this=0xfffffff9f818) at sources/lidars/jetpack50/cuda_pointpillars.cpp:144
--Type <RET> for more, q to quit, c to continue without paging--
#17 0x0000aaaaaae6460c in std::__invoke_impl<void, void (CudaPointpillars::*&)(), CudaPointpillars*&>(std::__invoke_memfun_deref, void (CudaPointpillars::*&)(), CudaPointpillars*&)
    (__f=@0xaaaaaca72408: (void (CudaPointpillars::*)(class CudaPointpillars * const)) 0xaaaaaae60538 <CudaPointpillars::task()>, __t=@0xaaaaaca72418: 0xfffffff9f818) at /usr/include/c++/9/bits/invoke.h:73
#18 0x0000aaaaaae64540 in std::__invoke<void (CudaPointpillars::*&)(), CudaPointpillars*&>(void (CudaPointpillars::*&)(), CudaPointpillars*&)
    (__fn=@0xaaaaaca72408: (void (CudaPointpillars::*)(class CudaPointpillars * const)) 0xaaaaaae60538 <CudaPointpillars::task()>)
    at /usr/include/c++/9/bits/invoke.h:95
#19 0x0000aaaaaae64498 in std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()>::__call<void, , 0ul>(std::tuple<>&&, std::_Index_tuple<0ul>) (this=0xaaaaaca72408, __args=...) at /usr/include/c++/9/functional:400
#20 0x0000aaaaaae64414 in std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()>::operator()<, void>() (this=0xaaaaaca72408)
    at /usr/include/c++/9/functional:484
#21 0x0000aaaaaae643b0 in std::__invoke_impl<void, std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()>>(std::__invoke_other, std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()>&&) (__f=...) at /usr/include/c++/9/bits/invoke.h:60
#22 0x0000aaaaaae64354 in std::__invoke<std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()>>(std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()>&&) (__fn=...) at /usr/include/c++/9/bits/invoke.h:95
#23 0x0000aaaaaae642f0 in std::thread::_Invoker<std::tuple<std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()> > >::_M_invoke<0ul>(std::--Type <RET> for more, q to quit, c to continue without paging--
_Index_tuple<0ul>) (this=0xaaaaaca72408) at /usr/include/c++/9/thread:244
#24 0x0000aaaaaae642c8 in std::thread::_Invoker<std::tuple<std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()> > >::operator()()
    (this=0xaaaaaca72408) at /usr/include/c++/9/thread:251
#25 0x0000aaaaaae642a8 in std::thread::_State_impl<std::thread::_Invoker<std::tuple<std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()> > > >::_M_run() (this=0xaaaaaca72400) at /usr/include/c++/9/thread:195
#26 0x0000ffffe6ad1f9c in  () at /lib/aarch64-linux-gnu/libstdc++.so.6
#27 0x0000fffff7e93624 in start_thread (arg=0xffffe6ad1f80) at pthread_create.c:477
#28 0x0000ffffe689449c in thread_start () at ../sysdeps/unix/sysv/linux/aarch64/clone.S:78

```

## 禾赛SDK错误

```bash
(gdb) bt
#0  0x0000aaaaaac096b0 in __gnu_cxx::new_allocator<PointXYZIRT>::construct<PointXYZIRT, PointXYZIRT&>(PointXYZIRT*, PointXYZIRT&) (this=0xffff4c000b98, __p=0xfff6b4b27000) at /usr/include/c++/9/ext/new_allocator.h:146
#1  0x0000aaaaaac04ce0 in std::allocator_traits<Eigen::aligned_allocator<PointXYZIRT> >::_S_construct<PointXYZIRT, PointXYZIRT&>(Eigen::aligned_allocator<PointXYZIRT>&, PointXYZIRT*, PointXYZIRT&) (__a=..., __p=0xfff6b4b27000)
    at /usr/include/c++/9/bits/alloc_traits.h:244
#2  0x0000aaaaaabff354 in std::allocator_traits<Eigen::aligned_allocator<PointXYZIRT> >::construct<PointXYZIRT, PointXYZIRT&>(Eigen::aligned_allocator<PointXYZIRT>&, PointXYZIRT*, PointXYZIRT&) (__a=..., __p=0xfff6b4b27000)
    at /usr/include/c++/9/bits/alloc_traits.h:350
#3  0x0000aaaaaabf7ecc in std::__uninitialized_copy_a<PointXYZIRT*, PointXYZIRT*, Eigen::aligned_allocator<PointXYZIRT> >(PointXYZIRT*, PointXYZIRT*, PointXYZIRT*, Eigen::aligned_allocator<PointXYZIRT>&)
    (__first=0xffff6c078000, __last=0x100036ac69010, __result=0xfff6aecee010, __alloc=...)
    at /usr/include/c++/9/bits/stl_uninitialized.h:293
#4  0x0000aaaaaabf7d88 in std::vector<PointXYZIRT, Eigen::aligned_allocator<PointXYZIRT> >::_M_allocate_and_copy<PointXYZIRT*>(unsigned long, PointXYZIRT*, PointXYZIRT*)
--Type <RET> for more, q to quit, c to continue without paging--
    (this=0xffff4c000b98, __n=359534080, __first=0xffff6623f010, __last=0x100036ac69010)
    at /usr/include/c++/9/bits/stl_vector.h:1511
#5  0x0000aaaaaabf090c in std::vector<PointXYZIRT, Eigen::aligned_allocator<PointXYZIRT> >::_M_assign_aux<PointXYZIRT*>(PointXYZIRT*, PointXYZIRT*, std::forward_iterator_tag)
    (this=0xffff4c000b98, __first=0xffff6623f010, __last=0x100036ac69010)
    at /usr/include/c++/9/bits/vector.tcc:309
#6  0x0000aaaaaabe8990 in std::vector<PointXYZIRT, Eigen::aligned_allocator<PointXYZIRT> >::_M_assign_dispatch<PointXYZIRT*>(PointXYZIRT*, PointXYZIRT*, std::__false_type)
    (this=0xffff4c000b98, __first=0xffff6623f010, __last=0x100036ac69010)
    at /usr/include/c++/9/bits/stl_vector.h:1625
#7  0x0000aaaaaabe091c in std::vector<PointXYZIRT, Eigen::aligned_allocator<PointXYZIRT> >::assign<PointXYZIRT*, void>(PointXYZIRT*, PointXYZIRT*) (this=0xffff4c000b98, __first=0xffff6623f010, __last=0x100036ac69010)
    at /usr/include/c++/9/bits/stl_vector.h:766

#8  0x0000aaaaaabd1170 in perception::lidars::Lidars::lidar_callback_l(hesai::lidar::LidarDecodedFrame<PointXYZIRT--Type <RET> for more, q to quit, c to continue without paging--
> const&) (frame=...) at sources/lidars/perception.cpp:145
#9  0x0000aaaaaabe8154 in std::_Function_handler<void (hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&), void (*)(hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&)>::_M_invoke(std::_Any_data const&, hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&) (__functor=..., __args#0=...) at /usr/include/c++/9/bits/std_function.h:300
#10 0x0000aaaaaabeffcc in std::function<void (hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&)>::operator()(hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&) const (this=0xaaaaab9313d0, __args#0=...)
    at /usr/include/c++/9/bits/std_function.h:688
#11 0x0000aaaaaabe8464 in hesai::lidar::Hesailidar<PointXYZIRT>::run() (this=0xaaaaab9313a8)
    at sources/lidars/hesai/hesai.h:115
#12 0x0000aaaaaac2acb8 in boost::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >::operator()(hesai::lidar::Hesailidar<PointXYZIRT>*) const (this=0xaaaaab932398, p=0xaaaaab9313a8)
    at /usr/local/include/boost/bind/mem_fn_template.hpp:49
#13 0x0000aaaaaac29b60 in boost::_bi::list1<boost::_bi::value<hesai::lidar::Hesailidar<PointXYZIRT>*> >::operator()<boost::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >, boost::_bi::list0>(boost::_bi::type<void>, boost--Type <RET> for more, q to quit, c to continue without paging--
::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >&, boost::_bi::list0&, int)
    (this=0xaaaaab9323a8, f=..., a=...) at /usr/local/include/boost/bind/bind.hpp:259
#14 0x0000aaaaaac26014 in boost::_bi::bind_t<void, boost::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >, boost::_bi::list1<boost::_bi::value<hesai::lidar::Hesailidar<PointXYZIRT>*> > >::operator()()
    (this=0xaaaaab932398) at /usr/local/include/boost/bind/bind.hpp:1294


#15 0x0000aaaaaac22348 in boost::detail::thread_data<boost::_bi::bind_t<void, boost::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >, boost::_bi::list1<boost::_bi::value<hesai::lidar::Hesailidar<PointXYZIRT>*> > > >::run() (this=0xaaaaab932250) at /usr/local/include/boost/thread/detail/thread.hpp:120
#16 0x0000fffff5f49a6c in thread_proxy () at /usr/local/lib/libboost_thread.so.1.71.0
#17 0x0000fffff7ead624 in start_thread (arg=0xfffff5f499e0 <thread_proxy>) at pthread_create.c:477
#18 0x0000ffffd7daf49c in thread_start () at ../sysdeps/unix/sysv/linux/aarch64/clone.S:78
```

## OPENCV DNN 错误

```bash
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x0000ffffd7cfeaac in __GI_abort () at abort.c:79
#2  0x0000ffffd7fc18bc in __gnu_cxx::__verbose_terminate_handler() ()
    at /lib/aarch64-linux-gnu/libstdc++.so.6
#3  0x0000ffffd7fbf20c in  () at /lib/aarch64-linux-gnu/libstdc++.so.6
#4  0x0000ffffd7fbf270 in  () at /lib/aarch64-linux-gnu/libstdc++.so.6
#5  0x0000ffffd7fbf564 in  () at /lib/aarch64-linux-gnu/libstdc++.so.6
#6  0x0000fffff64a682c in cv::dnn::GenericCUDABackendWrapper<float, 6>::copyToHost() ()
    at /usr/local/include/opencv_4.7.0/lib/libopencv_dnn.so.407
#7  0x0000fffff64c33e4 in cv::dnn::dnn4_v20221220::Net::Impl::forwardLayer(cv::dnn::dnn4_v20221220::detail::LayerData&) () at /usr/local/include/opencv_4.7.0/lib/libopencv_dnn.so.407
#8  0x0000fffff64c00d0 in cv::dnn::dnn4_v20221220::Net::Impl::forwardToLayer(cv::dnn::dnn4_v20221220::detail::LayerData&, bool) () at /usr/local/include/opencv_4.7.0/lib/libopencv_dnn.so.407
--Type <RET> for more, q to quit, c to continue without paging--
#9  0x0000fffff64dbea8 in cv::dnn::dnn4_v20221220::Net::Impl::forward(cv::_OutputArray const&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) ()
    at /usr/local/include/opencv_4.7.0/lib/libopencv_dnn.so.407
#10 0x0000fffff64bbcd0 in cv::dnn::dnn4_v20221220::Net::forward(cv::_OutputArray const&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) ()
    at /usr/local/include/opencv_4.7.0/lib/libopencv_dnn.so.407
#11 0x0000aaaaaab3e6b8 in Dnn::inferring() (this=0xfffffffd4758) at sources/cameras/dnn.cpp:302
#12 0x0000aaaaaab44910 in task_dnn_inference(void*) (arg=0xfffffffd4758) at sources/cameras/dnn.cpp:1115
#13 0x0000fffff7ead624 in start_thread (arg=0xaaaaaab448e4 <task_dnn_inference(void*)>)
    at pthread_create.c:477
#14 0x0000ffffd7daf49c in thread_start () at ../sysdeps/unix/sysv/linux/aarch64/clone.S:78
(gdb) 
```

## 禾赛sdk 多个主机间IP冲突影响雷达数据传输

```bash
(gdb) bt
#0  0x0000aaaaaabf6ebc in __gnu_cxx::new_allocator<PointXYZIRT>::construct<PointXYZIRT, PointXYZIRT&>(PointXYZIRT*, PointXYZIRT&) (this=0xffff2c000b98, __p=0xfffdff6e7ff0)
    at /usr/include/c++/9/ext/new_allocator.h:146
#1  0x0000aaaaaabf0b14 in std::allocator_traits<Eigen::aligned_allocator<PointXYZIRT> >::_S_construct<PointXYZIRT, PointXYZIRT&>(Eigen::aligned_allocator<PointXYZIRT>&, PointXYZIRT*, PointXYZIRT&)
    (__a=..., __p=0xfffdff6e7ff0) at /usr/include/c++/9/bits/alloc_traits.h:244
#2  0x0000aaaaaabea804 in std::allocator_traits<Eigen::aligned_allocator<PointXYZIRT> >::construct<PointXYZIRT, PointXYZIRT&>(Eigen::aligned_allocator<PointXYZIRT>&, PointXYZIRT*, PointXYZIRT&)
    (__a=..., __p=0xfffdff6e7ff0) at /usr/include/c++/9/bits/alloc_traits.h:350
#3  0x0000aaaaaabe3f90 in std::__uninitialized_copy_a<PointXYZIRT*, PointXYZIRT*, Eigen::aligned_allocator<PointXYZIRT> >(PointXYZIRT*, PointXYZIRT*, PointXYZIRT*, Eigen::aligned_allocator<PointXYZIRT>&) (__first=0xffff4c8cdff0, __last=0xffff67a13010, __result=0xfffdf9059010, __alloc=...)
    at /usr/include/c++/9/bits/stl_uninitialized.h:293
#4  0x0000aaaaaabec930 in std::vector<PointXYZIRT, Eigen::aligned_allocator<PointXYZIRT> >::_M_allocate_and_copy<PointXYZIRT*>(unsigned long, PointXYZIRT*, PointXYZIRT*)
    (this=0xffff2c000b98, __n=11705344, __first=0xffff4623f010, __last=0xffff67a13010)
    at /usr/include/c++/9/bits/stl_vector.h:1511
#5  0x0000aaaaaabe5d30 in std::vector<PointXYZIRT, Eigen::aligned_allocator<PointXYZIRT> >::_M_assign_aux<PointXYZIRT*>(PointXYZIRT*, PointXYZIRT*, std::forward_iterator_tag)
    (this=0xffff2c000b98, __first=0xffff4623f010, __last=0xffff67a13010)
    at /usr/include/c++/9/bits/vector.tcc:309
#6  0x0000aaaaaabdddbc in std::vector<PointXYZIRT, Eigen::aligned_allocator<PointXYZIRT> >::_M_assign_dispatch<PointXYZIRT*>(PointXYZIRT*, PointXYZIRT*, std::__false_type)
    (this=0xffff2c000b98, __first=0xffff4623f010, __last=0xffff67a13010)
    at /usr/include/c++/9/bits/stl_vector.h:1625
#7  0x0000aaaaaabd76a0 in std::vector<PointXYZIRT, Eigen::aligned_allocator<PointXYZIRT> >::assign<PointXYZIRT*, void>(PointXYZIRT*, PointXYZIRT*)
    (this=0xffff2c000b98, __first=0xffff4623f010, __last=0xffff67a13010)
--Type <RET> for more, q to quit, c to continue without paging--
    at /usr/include/c++/9/bits/stl_vector.h:766
#8  0x0000aaaaaabc9228 in perception::lidars::Lidars::lidar_callback_r(hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&) (frame=...) at sources/lidars/perception.cpp:166
#9  0x0000aaaaaabdd6e8 in std::_Function_handler<void (hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&), void (*)(hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&)>::_M_invoke(std::_Any_data const&, hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&) (__functor=..., __args#0=...)
    at /usr/include/c++/9/bits/std_function.h:300
#10 0x0000aaaaaabe58e8 in std::function<void (hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&)>::operator()(hesai::lidar::LidarDecodedFrame<PointXYZIRT> const&) const
    (this=0xaaaaab910fe8, __args#0=...) at /usr/include/c++/9/bits/std_function.h:688
#11 0x0000aaaaaabdd9f8 in hesai::lidar::Hesailidar<PointXYZIRT>::run() (this=0xaaaaab910fc0)
    at sources/lidars/hesai/hesai.h:115
#12 0x0000aaaaaac1ce90 in boost::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >::operator()(hesai::lidar::Hesailidar<PointXYZIRT>*) const (this=0xaaaaaba1d758, p=0xaaaaab910fc0)
    at /usr/local/include/boost/bind/mem_fn_template.hpp:49
#13 0x0000aaaaaac1be28 in boost::_bi::list1<boost::_bi::value<hesai::lidar::Hesailidar<PointXYZIRT>*> >::operator()<boost::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >, boost::_bi::list0>(boost::_bi::type<void>, boost::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >&, boost::_bi::list0&, int) (this=0xaaaaaba1d768, f=..., a=...) at /usr/local/include/boost/bind/bind.hpp:259
#14 0x0000aaaaaac1949c in boost::_bi::bind_t<void, boost::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >, boost::_bi::list1<boost::_bi::value<hesai::lidar::Hesailidar<PointXYZIRT>*> > >::operator()() (this=0xaaaaaba1d758) at /usr/local/include/boost/bind/bind.hpp:1294
#15 0x0000aaaaaac1686c in boost::detail::thread_data<boost::_bi::bind_t<void, boost::_mfi::mf0<void, hesai::lidar::Hesailidar<PointXYZIRT> >, boost::_bi::list1<boost::_bi::value<hesai::lidar::Hesailidar<PointXYZIRT>*> > > >::run() (this=0xaaaaaba1d610)
    at /usr/local/include/boost/thread/detail/thread.hpp:120
#16 0x0000fffff5f49a6c in thread_proxy () at /usr/local/lib/libboost_thread.so.1.71.0
#17 0x0000fffff7ead624 in start_thread (arg=0xfffff5f499e0 <thread_proxy>) at pthread_create.c:477
--Type <RET> for more, q to quit, c to continue without paging--
#18 0x0000ffffd7daf49c in thread_start () at ../sysdeps/unix/sysv/linux/aarch64/clone.S:78
```

## 显存冲突

```bash
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x0000ffffd7a45aac in __GI_abort () at abort.c:79
#2  0x0000ffffd7a92f40 in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0xffffd7b54518 "%s\n")
at ../sysdeps/posix/libc_fatal.c:155
#3  0x0000ffffd7a9a344 in malloc_printerr (str=str@entry=0xffffd7b504b0 "malloc(): invalid size (unsorted)")
    at malloc.c:5347
#4  0x0000ffffd7a9cedc in _int_malloc (av=av@entry=0xfffec0000020, bytes=bytes@entry=3600) at malloc.c:3736
#5  0x0000ffffd7a9e574 in __GI___libc_malloc (bytes=3600) at malloc.c:3066
#6  0x0000ffffd7d06b4c in operator new(unsigned long) () at /lib/aarch64-linux-gnu/libstdc++.so.6
#7  0x0000aaaaaae57234 in __gnu_cxx::new_allocator<Bndbox>::allocate(unsigned long, void const*)
    (this=0xfffeca52fe50, __n=100) at /usr/include/c++/9/ext/new_allocator.h:114
#8  0x0000aaaaaae56da8 in std::allocator_traits<std::allocator<Bndbox> >::allocate(std::allocator<Bndbox>&, unsigned long) (__a=..., __n=100) at /usr/include/c++/9/bits/alloc_traits.h:443
#9  0x0000aaaaaae5653c in std::_Vector_base<Bndbox, std::allocator<Bndbox> >::_M_allocate(unsigned long)
    (this=0xfffeca52fe50, __n=100) at /usr/include/c++/9/bits/stl_vector.h:343
#10 0x0000aaaaaae55ca8 in std::vector<Bndbox, std::allocator<Bndbox> >::reserve(unsigned long)
    (this=0xfffeca52fe50, __n=100) at /usr/include/c++/9/bits/vector.tcc:78
#11 0x0000aaaaaae548a8 in CudaPointpillars::infer(float*, int, std::vector<Bndbox, std::allocator<Bndbox> >&, int&) (this=0xfffffffd3738, cloud=0xfffec0000b60, size=128000, boxes=std::vector of length 0, capacity 0, elapsed=@0xfffeca52feac: 22) at sources/lidars/jetpack50/cuda_pointpillars.cpp:98
#12 0x0000aaaaaae5503c in CudaPointpillars::task_cudaPointpillars() (this=0xfffffffd3738)
    at sources/lidars/jetpack50/cuda_pointpillars.cpp:167
#13 0x0000aaaaaae580c8 in std::__invoke_impl<void, void (CudaPointpillars::*&)(), CudaPointpillars*&>(std::__invoke_memfun_deref, void (CudaPointpillars::*&)(), CudaPointpillars*&)
    (__f=@0xaaaaab9ebe58: (void (CudaPointpillars::*)(class CudaPointpillars * const)) 0xaaaaaae54df8 <CudaPointpillars::task_cudaPointpillars()>, __t=@0xaaaaab9ebe68: 0xfffffffd3738) at /usr/include/c++/9/bits/invoke.h:73
--Type <RET> for more, q to quit, c to continue without paging--
#14 0x0000aaaaaae57fd8 in std::__invoke<void (CudaPointpillars::*&)(), CudaPointpillars*&>(void (CudaPointpillars::*&)(), CudaPointpillars*&)
    (__fn=@0xaaaaab9ebe58: (void (CudaPointpillars::*)(class CudaPointpillars * const)) 0xaaaaaae54df8 <CudaPointpillars::task_cudaPointpillars()>) at /usr/include/c++/9/bits/invoke.h:95
#15 0x0000aaaaaae57f1c in std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()>::__call<void, , 0ul>(std::tuple<>&&, std::_Index_tuple<0ul>) (this=0xaaaaab9ebe58, __args=...) at /usr/include/c++/9/functional:400
#16 0x0000aaaaaae57e98 in std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()>::operator()<, void>()
    (this=0xaaaaab9ebe58) at /usr/include/c++/9/functional:484
#17 0x0000aaaaaae57e34 in std::__invoke_impl<void, std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()>>(std::__invoke_other, std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()>&&) (__f=...)
    at /usr/include/c++/9/bits/invoke.h:60
#18 0x0000aaaaaae57db8 in std::__invoke<std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()>>(std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()>&&) (__fn=...) at /usr/include/c++/9/bits/invoke.h:95
#19 0x0000aaaaaae57d40 in std::thread::_Invoker<std::tuple<std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()> > >::_M_invoke<0ul>(std::_Index_tuple<0ul>) (this=0xaaaaab9ebe58) at /usr/include/c++/9/thread:244
#20 0x0000aaaaaae57cf8 in std::thread::_Invoker<std::tuple<std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()> > >::operator()() (this=0xaaaaab9ebe58) at /usr/include/c++/9/thread:251
#21 0x0000aaaaaae57cc4 in std::thread::_State_impl<std::thread::_Invoker<std::tuple<std::_Bind<void (CudaPointpillars::*(CudaPointpillars*))()> > > >::_M_run() (this=0xaaaaab9ebe50) at /usr/include/c++/9/thread:195
#22 0x0000ffffd7d33f9c in  () at /lib/aarch64-linux-gnu/libstdc++.so.6
#23 0x0000fffff7ead624 in start_thread (arg=0xffffd7d33f80) at pthread_create.c:477
#24 0x0000ffffd7af649c in thread_start () at ../sysdeps/unix/sysv/linux/aarch64/clone.S:78
```

## 运行点云与yolov3_dnn 推理报错
```bash
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x0000ffffd8443aac in __GI_abort () at abort.c:79
#2  0x0000ffffd8490f40 in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0xffffd8552518 "%s\n")
    at ../sysdeps/posix/libc_fatal.c:155
#3  0x0000ffffd8498344 in malloc_printerr (str=str@entry=0xffffd854e4b0 "malloc(): invalid size (unsorted)")
    at malloc.c:5347
#4  0x0000ffffd849aedc in _int_malloc (av=av@entry=0xfffeb0000020, bytes=bytes@entry=3600) at malloc.c:3736
#5  0x0000ffffd849c574 in __GI___libc_malloc (bytes=3600) at malloc.c:3066
#6  0x0000ffffd8704b4c in operator new(unsigned long) () at /lib/aarch64-linux-gnu/libstdc++.so.6
#7  0x0000aaaaaac2c090 in __gnu_cxx::new_allocator<Bndbox>::allocate(unsigned long, void const*)
--Type <RET> for more, q to quit, c to continue without paging--
    (this=0xffff213f0e60, __n=100) at /usr/include/c++/9/ext/new_allocator.h:114
#8  0x0000aaaaaac2bc44 in std::allocator_traits<std::allocator<Bndbox> >::allocate(std::allocator<Bndbox>&, unsigned long) (__a=..., __n=100) at /usr/include/c++/9/bits/alloc_traits.h:443
#9  0x0000aaaaaac2b444 in std::_Vector_base<Bndbox, std::allocator<Bndbox> >::_M_allocate(unsigned long)
    (this=0xffff213f0e60, __n=100) at /usr/include/c++/9/bits/stl_vector.h:343
#10 0x0000aaaaaac2acb0 in std::vector<Bndbox, std::allocator<Bndbox> >::reserve(unsigned long)
    (this=0xffff213f0e60, __n=100) at /usr/include/c++/9/bits/vector.tcc:78
#11 0x0000aaaaaac29bac in CudaPointpillars::infer(float*, int, std::vector<Bndbox, std::allocator<Bndbox> >&, int&)
    (this=0xfffffffd3f38, cloud=0xfffeb0000b60, size=78750, boxes=std::vector of length 0, capacity 0, elapsed=@0xfff--Type <RET> for more, q to quit, c to continue without paging--
f213f0eb0: 18) at sources/lidars/jetpack50/cuda_pointpillars.cpp:98
#12 0x0000aaaaaac2a340 in CudaPointpillars::task_cudaPointpillars() (this=0xfffffffd3f38)
    at sources/lidars/jetpack50/cuda_pointpillars.cpp:164
```


## yolov8dnn + 点云推理 报错，六小时以上会出现

```bash
Thread 3 "sdlg" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0xffffa6252900 (LWP 33634)]
PointPillar::doinfer (this=0xffffa6251e60, points_data=0x242e2b000, points_size=125635, 
    nms_pred=std::vector of length 0, capacity 100) at sources/cudaPointpillars/common/pointpillar.cpp:322
322       float obj_count = bndbox_output_[0];
(gdb) bt
#0  PointPillar::doinfer(void*, unsigned int, std::vector<Bndbox, std::allocator<Bndbox> >&)
    (this=0xffffa6251e60, points_data=0x242e2b000, points_size=125635, nms_pred=std::vector of length 0, capacity 100) at sources/cudaPointpillars/common/pointpillar.cpp:322
#1  0x0000aaaaaaadee88 in task_cudaPointpillars(void*) (arg=0xffffffffe4f8)
    at sources/cudaPointpillars/cudaPointpillars.cpp:234
#2  0x0000fffff7ed9624 in start_thread (arg=0xaaaaaaade5a0 <task_cudaPointpillars(void*)>)
--Type <RET> for more, q to quit, c to continue without paging--
    -----
## yolov8dnn 报错
    __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
50      ../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x0000ffffd7c3faac in __GI_abort () at abort.c:79
#2  0x0000ffffd7f028bc in __gnu_cxx::__verbose_terminate_handler() ()
    at /lib/aarch64-linux-gnu/libstdc++.so.6
#3  0x0000ffffd7f0020c in  () at /lib/aarch64-linux-gnu/libstdc++.so.6
#4  0x0000ffffd7f00270 in  () at /lib/aarch64-linux-gnu/libstdc++.so.6
#5  0x0000ffffd7f00564 in  () at /lib/aarch64-linux-gnu/libstdc++.so.6
#6  0x0000fffff63e782c in cv::dnn::GenericCUDABackendWrapper<float, 6>::copyToHost() ()
--Type <RET> for more, q to quit, c to continue without paging--
    at /usr/local/include/opencv_4.7.0/lib/libopencv_dnn.so.407
#7  0x0000fffff64043e4 in cv::dnn::dnn4_v20221220::Net::Impl::forwardLayer(cv::dnn::dnn4_v20221220::detail::LayerData&) ()
    at /usr/local/include/opencv_4.7.0/lib/libopencv_dnn.so.407
#8  0x0000fffff64010d0 in cv::dnn::dnn4_v20221220::Net::Impl::forwardToLayer(cv::dnn::dnn4_v20221220::detail::LayerData&, bool) ()
    at /usr/local/include/opencv_4.7.0/lib/libopencv_dnn.so.407
#9  0x0000fffff641cea8 in cv::dnn::dnn4_v20221220::Net::Impl::forward(cv::_OutputArray cons--Type <RET> for more, q to quit, c to continue without paging--
t&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) () at /usr/local/include/opencv_4.7.0/lib/libopencv_dnn.so.407
#10 0x0000fffff63fccd0 in cv::dnn::dnn4_v20221220::Net::forward(cv::_OutputArray const&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) () at /usr/local/include/opencv_4.7.0/lib/libopencv_dnn.so.407
#11 0x0000aaaaaab3fa50 in Dnn::inferring() (this=0xfffffffd4738)
--Type <RET> for more, q to quit, c to continue without paging--
    at sources/cameras/dnn.cpp:289
#12 0x0000aaaaaab45c80 in task_dnn_inference(void*) (arg=0xfffffffd4738)
    at sources/cameras/dnn.cpp:1076
#13 0x0000fffff7ead624 in start_thread (arg=0xaaaaaab45c58 <task_dnn_inference(void*)>)
    at pthread_create.c:477
#14 0x0000ffffd7cf049c in thread_start () at ../sysdeps/unix/sysv/linux/aarch64/clone.S:78

--Type <RET> for more, q to quit, c to continue without paging--
```


## 运行图像推理yolov5lite 与 点云推理 报错
```bash
Thread 26 "sdlg" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0xffff0fff2900 (LWP 677587)]
0x0000fffeec000370 in ?? ()
(gdb) bt
#0  0x0000fffeec000370 in  ()
#1  0x0000fffffffd3870 in  ()
#2  0xaab82c7000000000 in  ()
(gdb) 
#0  0x0000fffeec000370 in  ()
#1  0x0000fffffffd3870 in  ()
#2  0xaab82c7000000000 in  ()
(gdb) bt
#0  0x0000fffeec000370 in  ()
#1  0x0000fffffffd3870 in  ()
#2  0xaab82c7000000000 in  ()
(gdb) 
```

## 单独运行图像推理yolov5lite 报错
```bash
[Switching to Thread 0xffff77c24900 (LWP 9461)]
__GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
50      ../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x0000ffffd7c3faac in __GI_abort () at abort.c:79
#2  0x0000ffffd7f028bc in __gnu_cxx::__verbose_terminate_handler() () at /lib/aarch64-linux-gnu/libstdc++.so.6
#3  0x0000ffffd7f0020c in  () at /lib/aarch64-linux-gnu/libstdc++.so.6
#4  0x0000ffffd7f00270 in  () at /lib/aarch64-linux-gnu/libstdc++.so.6
#5  0x0000ffffd7f00564 in  () at /lib/aarch64-linux-gnu/libstdc++.so.6
#6  0x0000ffffd7f2b958 in std::__throw_out_of_range_fmt(char const*, ...) ()
    at /lib/aarch64-linux-gnu/libstdc++.so.6
#7  0x0000aaaaaab636f8 in std::vector<target_t, std::allocator<target_t> >::_M_range_check(unsigned long) const
    (this=0xaaaaab013b28 <Sharedata::obs_dnns_filter>, __n=8) at /usr/include/c++/9/bits/stl_vector.h:1070
#8  0x0000aaaaaab61b58 in std::vector<target_t, std::allocator<target_t> >::at(unsigned long)
    (this=0xaaaaab013b28 <Sharedata::obs_dnns_filter>, __n=8) at /usr/include/c++/9/bits/stl_vector.h:1091
--Type <RET> for more, q to quit, c to continue without paging--
#9  0x0000aaaaaac331b8 in visualizer::Visualizer::draw_3d_views() ()
    at sources/visualization/visualization.cpp:926
#10 0x0000aaaaaac2f534 in visualizer::Visualizer::task(void*) (arg=0xaaaaab934a90)
    at sources/visualization/visualization.cpp:358
#11 0x0000fffff7ead624 in start_thread (arg=0xaaaaaac2d480 <visualizer::Visualizer::task(void*)>)
    at pthread_create.c:477
#12 0x0000ffffd7cf049c in thread_start () at ../sysdeps/unix/sysv/linux/aarch64/clone.S:78
```