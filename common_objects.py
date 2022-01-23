"""
这里是一些非常常用的类型定义和方法！
"""
import time

class Event:  # 事件类型定义
    def __init__(self, eventtype: str, eventinfo: str, pid: int):
        self.eventinfo = eventinfo
        self.eventtype = eventtype
        self.pid = pid
        self.time = time.time()

    def print_data(self):  # 输出事件信息的方法
        print("Event type is", self.eventtype)
        print("Event info is", self.eventinfo)
        print("Event is from process", self.pid)
        print("created at", self.time, "\n")
