import os
import sys


def func():
    print(os.getcwd())  # 获取执行脚本的目录
    print(sys.argv[0].split('/')[-1].split('.')[0])  # 执行脚本的绝对路径名
    print(__file__)  # 被执行代码所在文件的绝对路径名

