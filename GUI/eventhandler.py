"""
测试事件处理器
"""
import multiprocessing
import time
import traceback
from threading import Thread, Timer
from PySide6.QtCore import QObject, Signal, QEventLoop, QTimer
from common_objects import *
from GUI.mainwindow import *
from GUI.testmodule import Ui_TestWindow


class EventSignal(QObject):
    event = Signal(dict)
    def poll(self,event):
        event_dict = event.dictize()
        self.event.emit(event_dict)
        loop = QEventLoop()
        QTimer.singleShot(100, loop.quit)
        loop.exec()
        #self.event.connect()


def instruction_process(event: Event):
    if event.eventinfo == "Error":
        pass


class EventHandler:
    def __init__(self, queue: multiprocessing.Queue):
        self.__active = False  # 控制位，用于控制侦听器是否活跃
        self.__verbose = False
        if isinstance(queue, multiprocessing.queues.Queue):
            self.queue = queue  # 事件队列
        else:
            raise TypeError("Bad queue", str(type(queue)), queue)
        self.__listener = Thread(target=self.__listen)
        self.register_dict = {}
        self.HANDLER_DICT = {"Error": None,
                        "Info": Ui_MainWindow.event_handle,
                        "Progress": Ui_MainWindow.process_handle,
                        "Instruction": self.instruction_process
                        }
        self.front_handler = EventSignal()
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

    def register_process(self, register_event):
        self.register_dict[register_event.pid] = register_event.info_extra

    def error_process(self, event):
        event.print_data()

    def instruction_process(self, event):
        if event.eventinfo == "Register":
            self.register_process(event)

    def event_process(self, gotevent: Event):
        if self.__verbose:
            print("Handler Process", multiprocessing.current_process().pid,
                  "Got Data", gotevent)
            gotevent.print_data()
        if gotevent.eventinfo == "Stop handler":
            self.kill_listener()
        if isinstance(self.front_handler, EventSignal):
            self.front_handler.poll(gotevent)
        else:
            print("None activated")
            #self.HANDLER_DICT[gotevent.eventtype](gotevent)


    def activate_listener(self):  # 启动侦听器
        self.__active = True
        if self.__verbose:
            print("activating listener")
        self.__listener.start()

    def kill_listener(self):
        if self.__verbose:
            print("Terminating listener")
        self.__active = False
        if self.__verbose:
            print("Terminated listener")

    def activate_verbose(self):
        self.__verbose = True
        print("Now running in verbose")


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
