"""
保存一些配置文件相关的类和处理
生成，文件路径和文件名处理等
常量值版本：2/8/22
"""
import os
import json
import time
#import traceback
from enum import Enum


ELEVATOR_ITEM_INDEX = 7


class WorkingMode(Enum):
    Data = "Data"
    Config = "Config"

class FilenameProcess:  # 取文件名等相关信息
    file_dir = ""  # 文件路径
    path = ""  # 目录路径
    file_fullname = ""  # 文件全名
    file_name = ""
    file_ext = ""  # 文件扩展名


    def __init__(self, file_dir, mode: WorkingMode = WorkingMode.Data):
        print(mode)
        if mode == WorkingMode.Data:
            print("data inint")
            self.file_dir = file_dir
            (self.path, self.file_fullname) = os.path.split(self.file_dir)
            (self.file_name, file_ext) = os.path.splitext(self.file_fullname)  # self.file_name:文件名（不含扩展名）
            self.file_ext = file_ext.strip(".")
        elif mode == WorkingMode.Config:
            self.path = file_dir


class ConfigData:
    dict_data = {}

    def __init__(self, directory, name=None, config_mode=False):
        self.config_mode = config_mode
        self.directory = directory  # 配置文件所在文件夹路径
        self.name = name  # 配置名
        self.__verbose = False
        if self.config_mode:
            self.file_dir_object = FilenameProcess(directory, WorkingMode.Config)  # 文件路径实例化方便取信息
        else:
            self.file_dir_object = FilenameProcess(directory, WorkingMode.Data)
        pass

    def set_verbose(self, choice: bool):
        if choice:
            self.__verbose = True
            print("Verbosity enabled in ConfigData object at", self)
            print("ConfigData Object Basic data:\nDirectory:", self.directory)

    def set_config_mode(self, config_mode: bool):
        self.config_mode = config_mode

    def set_basic_info(self, elvt_cnt: int, floor_cnt: int, under_floors: int):
        if not isinstance(elvt_cnt, int) and isinstance(floor_cnt, int) and isinstance(under_floors, int):
            raise TypeError("传入类型错误")
        else:
            self.dict_data["elvt_cnt"] = elvt_cnt
            # print(type(self.elvt_cnt.value()),  self.elvt_cnt.value())
            self.dict_data["floor_cnt"] = floor_cnt
            self.dict_data["under_floors"] = under_floors

            if self.__verbose:
                print("initial config done!", self.dict_data)

            self.dict_data["elevators"] = []
            for index in range(1, elvt_cnt + 1):
                self.dict_data["elevators"].append({"index": index, "floors": None,
                                                    "accepted_priority": None,
                                                    "service_duration": None,
                                                    "capacity": None})
            if self.__verbose:
                print("Elevators generated", self.dict_data["elevators"])

    def set_config_name(self, use_file_name: bool = True, name: str = None):  # 设置配置名
        if use_file_name and isinstance(self.file_dir_object, FilenameProcess):
            self.name = self.file_dir_object.file_name  # 使用文件名
        else:
            if not isinstance(name, str):
                raise TypeError("传入错误类型")
            else:
                self.name = name
        if self.__verbose:
            print("Config name set!", self.name)

    def get_elevator_config(self, index: int):
        for elevator in self.dict_data["elevators"]:
            if elevator["index"] == index:
                return elevator

    def set_elevator_config(self, index: int, floors: tuple = None,
                            accepted_priority: int = None, service_duration: tuple = None,
                            capacity: int = None):
        for elevator in self.dict_data["elevators"]:
            if elevator["index"] == index:
                elevator["floors"] = floors
                elevator["accepted_priority"] = accepted_priority
                elevator["service_duration"] = service_duration
                elevator["capacity"] = capacity
                break
        if self.__verbose:
            print("Elevator", index, "config is set", self.dict_data["elevators"])
        pass

    def generate_data_file(self):  # 从字典生成配置文件
        if self.directory is None:  # 先确定路径
            raise AttributeError("未指定路径，不能生成新数据")
        else:
            filename = time.strftime("Config_at_%y-%m-%d-%H-%M-%S", time.localtime())+'.json'
            self.file_dir_object = FilenameProcess(os.path.join(self.directory, "Configs", filename))
            if self.__verbose:
                print("Attempt to create file at", self.file_dir_object.file_dir)
            with open(self.file_dir_object.file_dir, 'w') as f:
                json.dump(self.dict_data, f)
            return self.file_dir_object.file_dir

        pass

