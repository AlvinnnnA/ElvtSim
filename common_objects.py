"""
这里是一些非常常用的类型定义和方法！
"""
import time

class Event:  # 事件类型定义
    def __init__(self, eventtype: str, eventinfo: str, pid: int, info_extra = None):
        if not isinstance(eventtype, str) and isinttance(eventinfo, str) \
                and isinstance(pid, int) and isinstance(info_extra, (NoneType, str)):
            raise TypeError("事件初始化出现错误：传入参数类型错误")
        self.eventinfo = eventinfo
        self.eventtype = eventtype
        self.pid = pid
        self.time = time.time()
        self.info_extra = info_extra

    def print_data(self):  # 输出事件信息的方法
        print("Event type is", self.eventtype)
        print("Event info is", self.eventinfo)
        print("Event is from process", self.pid)
        print("created at", self.time, "\n")
        if not self.info_extra is None:
            print("Extra info is", self.info_extra)

