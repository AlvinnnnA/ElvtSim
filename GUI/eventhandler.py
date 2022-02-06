"""
事件处理器
"""
import multiprocessing
import time
import traceback
from threading import Thread, Timer
from PySide6.QtCore import QObject, Signal, QEventLoop, QTimer
from common_objects import *
from GUI.mainwindow import *
from GUI.testmodule import Ui_TestWindow


class EventSignal(QObject):  # Qt信号，发送事件到前端生成提示框
    event = Signal(dict)
    def poll(self,event):
        event_dict = event.dictize()
        self.event.emit(event_dict)
        #loop = QEventLoop()
        #QTimer.singleShot(100, loop.quit)
        #loop.exec()
        #self.event.connect()


def instruction_process(event: Event):
    if event.eventinfo == "Error":
        pass


class EventHandler:
    def __init__(self, queue: multiprocessing.Queue):
        self.__active = False  # 控制位，用于控制侦听器是否活跃
        self.__verbose = False
        self.__use_front_handler = False
        if isinstance(queue, multiprocessing.queues.Queue):  # 判断传入队列对象是否类型正确
            self.queue = queue  # 事件队列
        else:
            raise TypeError("Bad queue", str(type(queue)), queue)
        self.__listener = Thread(target=self.__listen)
        self.register_dict = {}  # 进程注册字典
        self.HANDLER_DICT = {"Error": None,
                        "Info": Ui_MainWindow.event_handle,
                        "Progress": Ui_MainWindow.process_handle,
                        "Instruction": self.instruction_process
                        }  # 处理对应事件方法
        self.front_handler = None  # 前端信号发送器
        # 一个小坑：target=func()和target=func不一样，前者直接运行，后者不调用start()不运行
        # self.activate_listener()  # 启动侦听器线程

    def __listen(self):
        if self.__verbose:
            print("handler listening for events\n")  # 运行汇报
        while self.__active:  # 控制位
            while not self.queue.empty():  # 队列非空时不断处理
                gotevent = self.queue.get(block=True)  # 取事件对象
                if not isinstance(gotevent, Event):  # 防止非事件对象进入队列出错
                    self.queue.put(Event("Error", "Type error in error handler, an object "
                                                  "that is not an event was put in event queue",
                                         multiprocessing.current_process().pid))
                    continue
                self.event_process(gotevent)
            if self.queue.empty():
                time.sleep(0.3)  # 避免cpu占用过高

    def register_process(self, register_event):  # 进程注册方法
        self.register_dict[register_event.pid] = register_event.info_extra

    def error_process(self, event):  # 没用
        event.print_data()

    def instruction_process(self, event):  # 处理Instruction类事件
        if event.eventinfo == "Register":
            self.register_process(event)

    def event_process(self, gotevent: Event):  #总事件处理器
        if self.__verbose:  # 啰嗦模式
            print("Handler Process", multiprocessing.current_process().pid,
                  "Got Data", gotevent)
            gotevent.print_data()
        if gotevent.eventinfo == "Stop handler":  # 处理器自杀
            self.kill_listener()
        if self.__use_front_handler:  # 前端信号发送器
            self.front_handler.poll(gotevent)
        else:
            print("No reporting mechanism activated")
            #self.HANDLER_DICT[gotevent.eventtype](gotevent)


    def activate_listener(self):  # 启动侦听器
        self.__active = True
        if self.__verbose:
            print("activating listener")
        self.__listener.start()

    def kill_listener(self):  # 关闭侦听器
        if self.__verbose:
            print("Terminating listener")
        self.__active = False
        if self.__verbose:
            print("Terminated listener")

    def activate_verbose(self):  # 启动啰嗦模式
        self.__verbose = True
        print("Now running in verbose")

    def use_front_handler(self):  # 启动前端报送
        self.__use_front_handler = True
        self.front_handler = EventSignal()


def kill_handler(queue: multiprocessing.Queue):
    stop_event = Event("Instruction", "Stop handler", multiprocessing.current_process().pid)
    queue.put(stop_event)


def suicide(err: multiprocessing.Queue):
    a = 1
    try:
        a.append("a")
    except AttributeError:
        error_event = Event("Error", traceback.format_exc(), multiprocessing.current_process().pid)
        err.put(error_event)


def self_test():
    print("Event handler self test")
    err = multiprocessing.Queue()

    handler = EventHandler(err)
    handler.activate_verbose()
    handler.activate_listener()

    suicide(err)

    # handler_instance = multiprocessing.Process(target=EventHandler, args=(err,))
    # handler_instance.start()  # 启动事件处理器

    killer = Timer(5, kill_handler, args=(err,))
    killer.start()
