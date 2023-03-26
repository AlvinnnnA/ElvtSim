"""
这里是一些非常常用的类型定义和方法！
"""
import time
from types import NoneType
from datetime import datetime as dt

from Scheduler.Thread import convert_time


class Event:  # 事件类型定义
    def __init__(self, eventtype: str, eventinfo: str, pid: int = None, info_extra=None):
        if not isinstance(eventtype, str) and isinstance(eventinfo, str) \
                and isinstance(pid, int) and isinstance(info_extra, (NoneType, str)):  # 有问题
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

    def dictize(self):
        event_dict = {}
        event_dict["eventinfo"] = self.eventinfo
        event_dict["eventtype"] = self.eventtype
        event_dict["pid"] = self.pid
        event_dict["time"] = self.time
        event_dict["info_extra"] = self.info_extra
        return event_dict

class DefaultPrint:
    def __init__(self):
        print("Default Print init")
        self.logs = self.bridge()

    class bridge():
        def append(self,*args):
            print(*args)

    def _format_timestamp(self, timestamp) -> str:
        return dt.strftime(timestamp, "%m/%d %H:%M:%S")

    def info(self, info: str):
        formatted_timestamp = self._format_timestamp(dt.now())
        entry = ["INFO", formatted_timestamp, info]
        self.logs.append(entry)

    def debug(self, info: str):
        formatted_timestamp = self._format_timestamp(dt.now())
        entry = ["DEBUG", formatted_timestamp, info]
        self.logs.append(entry)

    def warning(self, info: str):
        formatted_timestamp = self._format_timestamp(dt.now())
        entry = ["WARNING", formatted_timestamp, info]
        self.logs.append(entry)

    def error(self, info: str):
        formatted_timestamp = self._format_timestamp(dt.now())
        entry = ["ERROR", formatted_timestamp, info]
        self.logs.append(entry)

    def critical(self, info: str):
        formatted_timestamp = self._format_timestamp(dt.now())
        entry = ["CRITICAL", formatted_timestamp, info]
        self.logs.append(entry)

    def call(self, clock,uid,floor):
        formatted_timestamp = convert_time.num_to_time(clock)
        entry = ["CALL", formatted_timestamp, uid,floor]
        self.logs.append(entry)

    def into(self,clock, uid):
        formatted_timestamp = convert_time.num_to_time(clock)
        entry = ["INTO", formatted_timestamp, uid]
        self.logs.append(entry)

    def exit(self,clock,uid):
        formatted_timestamp = convert_time.num_to_time(clock)
        entry = ["EXIT", formatted_timestamp, uid]
        self.logs.append(entry)

def make_event_instance(event_dict: dict):
    event = Event(event_dict["eventtype"], event_dict["eventinfo"], event_dict["pid"], event_dict["info_extra"])
    return event

