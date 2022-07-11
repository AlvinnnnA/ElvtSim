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
from Log.Common import bifrost


ELEVATOR_ITEM_INDEX = 7


class WorkingMode(Enum):  # 运行模式枚举类
    Data = "Data"
    Config = "Config"

class FilenameProcess:  # 取文件名等相关信息
    file_dir = ""  # 文件路径
    path = ""  # 目录路径
    file_fullname = ""  # 文件全名
    file_name = ""
    file_ext = ""  # 文件扩展名


    def __init__(self, file_dir, mode: WorkingMode = WorkingMode.Data, verbose=False):
        if verbose:
            print("filename object set mode", mode)
        if mode == WorkingMode.Data:  # 数据模式
            if verbose:
                print("filename data init")
            self.file_dir = file_dir
            (self.path, self.file_fullname) = os.path.split(self.file_dir)
            (self.file_name, file_ext) = os.path.splitext(self.file_fullname)  # self.file_name:文件名（不含扩展名）
            self.file_ext = file_ext.strip(".")
        elif mode == WorkingMode.Config:
            if verbose:
                print("filename config init")
            self.path = file_dir


class ConfigData:
    dict_data = {}

    def __init__(self, directory, name=None, config_mode=False, verbose=False):
        self.config_mode = config_mode
        self.directory = directory  # 配置文件所在文件夹路径
        self.name = name  # 配置名
        self.__verbose = verbose
        if self.config_mode:
            self.file_dir_object = FilenameProcess(directory, WorkingMode.Config, self.__verbose)
            # 文件路径实例化方便取信息
        else:
            self.file_dir_object = FilenameProcess(directory, WorkingMode.Data, self.__verbose)
        if self.__verbose:
            print("Verbosity enabled in ConfigData object at", self)
            print("ConfigData Object Basic data:\nDirectory:", self.directory)
        pass

    def set_verbose(self, choice: bool):
        self.__verbose = choice  # 罗嗦模式

    def set_basic_info(self, elvt_cnt: int, floor_cnt: int, under_floors: int):
        # 基础信息设置
        if not isinstance(elvt_cnt, int) and isinstance(floor_cnt, int) and isinstance(under_floors, int):
            raise TypeError("Basic info arguments' type does not match expected")
        else:
            self.dict_data["elvt_cnt"] = elvt_cnt  # 填入配置
            # print(type(self.elvt_cnt.value()),  self.elvt_cnt.value())
            self.dict_data["floor_cnt"] = floor_cnt
            self.dict_data["under_floors"] = under_floors

            if self.__verbose:
                print("initial config done!", self.dict_data)

            self.dict_data["elevators"] = []
            for index in range(1, elvt_cnt + 1):  # 生成电梯对象
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

    def get_elevator_config(self, index: int):  # 获取索引为index的电梯对象
        if self.dict_data["elevators"][index-1]["index"] == index:
            return self.dict_data["elevators"][index-1]
        else:
            raise ValueError("Requested elevator not found")

    def set_elevator_config(self, index: int, floors: tuple = None,
                            accepted_priority: int = None, service_duration: tuple = None,
                            capacity: int = None):  # 设置电梯配置
        elevator = self.get_elevator_config(index)
        if elevator["index"] == index:
            elevator["floors"] = floors
            elevator["accepted_priority"] = accepted_priority
            elevator["service_duration"] = service_duration
            elevator["capacity"] = capacity
            if self.__verbose:
                print("Elevator", index, "config is set", elevator)

        pass

    def generate_data_file(self):  # 从字典生成配置文件
        if self.directory is None:  # 先确定路径
            raise AttributeError("未指定路径，不能生成新数据")
        else:
            filename = time.strftime("Config at %y-%m-%d-%H-%M-%S", time.localtime())+'.json'
            self.file_dir_object = FilenameProcess(os.path.join(self.directory, "Configs", filename))
            bifrost.Reporter.debug("Attempt to create file at", self.file_dir_object.file_dir)
            with open(self.file_dir_object.file_dir, 'w') as f:
                json.dump(self.dict_data, f, indent=4, separators=(',', ':'))
            return self.file_dir_object.file_dir

    def get_file_name(self):
        return self.file_dir_object.file_fullname
        pass

class UIConfig:
    def __init__(self, conf_dict):
        if not isinstance(conf_dict, dict):
            raise TypeError("Bad type in", str(conf_dict), "type is", type(conf_dict))
        pass