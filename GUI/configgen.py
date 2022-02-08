"""
保存一些配置文件相关的类和处理
生成，文件路径和文件名处理等
常量值版本：2/8/22
"""
import os
import json

ELEVATOR_ITEM_INDEX = 7


class FilenameProcess:  # 取文件名等相关信息
    file_dir = ""  # 文件路径
    path = ""  # 目录路径
    file_fullname = ""  # 文件全名
    file_name = ""
    file_ext = ""  # 文件扩展名

    def __init__(self, dir):
        self.file_dir = dir
        (self.path, self.file_fullname) = os.path.split(self.file_dir)
        (self.file_name, file_ext) = os.path.splitext(self.file_fullname)  # self.file_name:文件名（不含扩展名）
        self.file_ext = file_ext.strip(".")


class ConfigData:
    def __init__(self, directory, name=None):
        self.directory = directory  # 配置文件所在文件夹路径
        self.name = name  # 配置名
        if directory is not None:
            self.file_dir_object = FilenameProcess(directory)  # 文件路径实例化方便取信息

    def generate_data_from_dict(self, data_dict: dict):  # 从字典生成配置文件
        if self.directory is not None:  # 先确定路径
            raise AttributeError("未指定路径，不能生成新数据")
        pass

    def set_config_name(self, use_file_name=True, name=None):  # 设置配置名
        if use_file_name and isinstance(self.file_dir_object, FilenameProcess):
            self.name = self.file_dir_object.file_name  # 使用文件名
        else:
            if not isinstance(name, str):
                raise TypeError("传入错误类型")
            else:
                self.name = name
