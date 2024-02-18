#!/bin/bash
#!/bin/bash

#抽取文件，每十个抽取一个
source_folder="./20231226pcd/pcd_people"
saving_folder="../myf_kuang/people1"
count=0
nums=0
# 确保目标文件夹存在
mkdir -p "$saving_folder"

# 遍历源文件夹中的文件
for file in "$source_folder"/*; do
  if [ -f "$file" ]; then
    ((count++))
    if ((count % 5 == 0)); then
      # 复制每隔10个文件到目标文件夹
      cp "$file" "$saving_folder";
      ((nums++))
    fi
  fi
done

echo "已复制 $nums 个文件到 $saving_folder 文件夹。"

