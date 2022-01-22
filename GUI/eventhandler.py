# 测试事件处理器
import multiprocessing
import time
from threading import Thread, Timer
from mainwindow import *
HANDLER_DICT = {"Error": Ui_MainWindow.error_handle,
                "Info": Ui_MainWindow.event_handle,
                "Progress": Ui_MainWindow.process_handle,
                "Instruction": None
                }  #instruction_guide}


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


class EventHandler:
    def __init__(self, queue: multiprocessing.Queue):
        self.__active = False  # 控制位，用于控制侦听器是否活跃
        self.__verbose = False
        self.queue = queue  # 事件队列
        self.__listener = Thread(target=self.__listen)
        # 一个小坑：target=func()和target=func不一样，前者直接运行，后者不调用start()不运行
        # self.activate_listener()  # 启动侦听器线程

    def __listen(self):
        if self.__verbose:
            print("handler listening for events\n")  # 运行汇报
        while self.__active:  # 控制位
            time.sleep(0.3)  # 避免cpu占用过高
            while not self.queue.empty():  # 队列非空时不断处理
                gotevent = self.queue.get(block=True)  # 取事件对象
                if not isinstance(gotevent, Event):  # 防止非事件对象进入队列出错
                    self.queue.put(Event("Error", "Type error in error handler, an object "
                                                  "that is not an event was put in event queue",
                                         multiprocessing.current_process().pid))
                    continue
                self.__event_process(gotevent)

    def __event_process(self, gotevent: Event):
        if self.__verbose:
            print("Handler Process", multiprocessing.current_process().pid,
                  "Got Data", gotevent)
            gotevent.print_data()
        if gotevent.eventtype == "Instruction":  # 实现特定事件传入关闭侦听器
            if gotevent.eventinfo == "Stop handler":
                self.__active = False
            else:
                HANDLER_DICT["Instruction"](gotevent)
        else:
            HANDLER_DICT[gotevent.eventtype]()

    def activate_listener(self):  # 启动侦听器
        self.__active = True
        if self.__verbose:
            print("activating listener")
        self.__listener.start()

    def activate_verbose(self):
        self.__verbose = True
        print("Now running in verbose")


def kill_handler(queue: multiprocessing.Queue):
    stop_event = Event("Instruction", "Stop handler", multiprocessing.current_process().pid)
    queue.put(stop_event)


def self_test():
    err = multiprocessing.Queue()

    handler = EventHandler(err)
    handler.activate_verbose()
    handler.activate_listener()
    # handler_instance = multiprocessing.Process(target=EventHandler, args=(err,))
    # handler_instance.start()  # 启动事件处理器

    killer = Timer(5, kill_handler, args=(err,))
    killer.start()


