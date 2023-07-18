#coding: utf-8
#This is a script for dataset inspection, including functionalities such as label deduplication, label removal,
#  and reprocessing of problematic images.
# ---mayufneg---2023.07.18---

from json.tool import main
import os,time,argparse
from unicodedata import name
import cv2

#图片重写
def rewrite_images(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            img = cv2.imread(file_path)
            try:
                cv2.imwrite(file_path, img)
            except:
                print("wrong image format:",file_path)

#替换标签
def change_char_at_position(text, position, new_char):
    char_list = list(text)  # 转换为列表
    if 0 <= position < len(char_list):  # 确保位置在有效范围内
        char_list[position] = new_char  # 修改指定位置的字符
    new_text = ''.join(char_list)  # 将列表转换回字符串
    return new_text

def label_check(directory):
    for root, dirs, files in os.walk(directory):
        t = root.split('/')
        print(t)
        if t[-2] == 'labels':
            t[-2] = 'newlabels'
        elif t[-3] == 'labels':
            t[-3] = 'newlabels'
        newroot = '/'.join(t)
        print(newroot)
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            newlabel_file = os.path.join(newroot, file)
            newlabel = []
            with open(file_path, 'r') as f: #处理shadow类
                lines = f.readlines()
                lines = list(set(lines)) #去重
                for l in lines:
                    line = l.rstrip().split() #x,y,w,h
                    x = line[1]
                    y = line[2]
                    w = line[3]
                    h = line[4]
                    label = line[0]
                    # 去除shadow、和xywh∉[0,1]标签
                    if label != '5' and 0 < float(x) < 1 and 0 < float(y) < 1 and 0 < float(w) < 1 and 0 < float(h) < 1:
                        if int(label) > 5:
                            nl = str(int(label) - 1)
                            new_line = change_char_at_position(l, 0, nl)
                            newlabel.append(new_line)
                        else:
                            newlabel.append(l)
            if len(newlabel) > 0:
                with open(newlabel_file, 'w') as fw:
                    fw.writelines(newlabel)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--labelsdir', type=str, default='./labels/train/', help='labels director')
    parser.add_argument('--imagesdir', type=str, default='./images/train/', help='images director')
    opt = parser.parse_args()
    print("..开始执行脚本..")
    print("image check")
    rewrite_images(opt.imagesdir)
    print("label check")
    label_check(opt.labelsdir)
    print("---succeccful---")