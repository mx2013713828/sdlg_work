import os
import random
import shutil

def shuffle_and_copy_files(source_folder, target_folders):
    # 获取源文件夹下所有文件
    all_files = os.listdir(source_folder)
    
    # 将文件列表打乱顺序
    random.shuffle(all_files)

    # 计算每个目标文件夹应该包含的文件数
    files_per_folder = len(all_files) // len(target_folders)
    
    # 将文件复制到目标文件夹
    for i, target_folder in enumerate(target_folders):
        # 创建目标文件夹（如果不存在）
        os.makedirs(target_folder, exist_ok=True)
        
        # 计算当前目标文件夹应该复制的文件范围
        start_index = i * files_per_folder
        end_index = (i + 1) * files_per_folder if i < len(target_folders) - 1 else None
        
        # 复制文件到目标文件夹
        for file_name in all_files[start_index:end_index]:
            source_path = os.path.join(source_folder, file_name)
            target_path = os.path.join(target_folder, file_name)
            shutil.copy(source_path, target_path)

if __name__ == "__main__":
    # 指定源文件夹和目标文件夹列表
    source_folder = "/media/sdlg/DataSet/data/0122sorted/"
    target_folders = [f"/media/sdlg/DataSet/data/0122sorted_split/0122splited_{i}" for i in range(1, 6)]

    # 执行打乱和复制操作
    shuffle_and_copy_files(source_folder, target_folders)
