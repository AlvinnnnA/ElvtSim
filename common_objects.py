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

    def dictize(self):
        event_dict = {}
        event_dict["eventinfo"] = self.eventinfo
        event_dict["eventtype"] = self.eventtype
        event_dict["pid"] = self.pid
        event_dict["time"] = self.time
        event_dict["info_extra"] = self.info_extra
        return event_dict


def make_event_instance(event_dict: dict):
    event = Event(event_dict["eventtype"], event_dict["eventinfo"], event_dict["pid"], event_dict["info_extra"])
    return event

