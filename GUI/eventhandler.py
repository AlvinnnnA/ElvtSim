# 测试事件处理器
import multiprocessing
import time
from threading import Thread


class Event:  # 事件类型定义
    def __init__(self, eventtype, eventinfo, pid):
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
    def __init__(self, queue):
        print("handler Process", multiprocessing.current_process().pid,
              "is running\n")  # 运行汇报
        self.__active = False  # 控制位，用于控制侦听器是否活跃
        self.queue = queue  # 事件队列
        self.__listener = Thread(target=self.__listen)
        # 一个小坑：target=func()和target=func不一样，前者直接运行，后者不调用start()不运行
        print("activating listener")  # 运行汇报
        self.activate_listener()  # 启动侦听器线程

    def __listen(self):
        print("handler listening for events\n")  # 运行汇报
        while self.__active:  # 控制位
            time.sleep(0.3)  # 避免cpu占用过高
            while not self.queue.empty():  # 队列非空时不断处理
                print("new event found")
                gotevent = self.queue.get(block=True)  # 取事件对象
                if not isinstance(gotevent, Event):  # 防止非事件对象进入队列出错
                    print("Queue error")
                    continue
                self.__event_process(gotevent)

    def __event_process(self, gotevent):
        print("Handler Process", multiprocessing.current_process().pid,
              "Got Data", gotevent)
        gotevent.print_data()
        if gotevent.eventtype == "Instruction":  # 实现特定事件传入关闭侦听器
            if gotevent.eventinfo == "Stop handler":
                self.__active = False
                print("Instruction to stop is received, aborting event processor")

    def activate_listener(self):  # 启动侦听器
        self.__active = True
        self.__listener.start()
        # self.__listener = Thread(target=self.__listen)

class WorkManager:
    def __init__(self, eventqueue, run_config):
        self.eventqueue = eventqueue
        print("Manager Process", multiprocessing.current_process().pid,
              "is running at\n", time.time())
        currentevent = Event("General", "manager running",
                             multiprocessing.current_process().pid)  # 报告自身启动
        self.eventqueue.put(currentevent)
        self.initiate(run_config)  # 根据配置数据启动工作进程

    def initiate(self, process_arguments):  # 根据传入配置数据启动工作进程
        process_list = []
        for process in range(0, len(process_arguments)):
            process_list.append(multiprocessing.Process(target=WorkingProcess,
                                                        args=(process_arguments[process],
                                                              self.eventqueue)))  # 配置进程
        for process in range(0, len(process_arguments)):
            process_list[process].start()  # 启动进程

class WorkingProcess:
    def __init__(self, workerdata, eventqueue):
        print("Created worker process", workerdata[0],"with process ID", multiprocessing.current_process().pid, "\n")
        self.eventqueue = eventqueue
        currentevent = Event("General", "worker running", multiprocessing.current_process().pid)
        self.eventqueue.put(currentevent)
        time.sleep(3)
        self.error()  # 自杀

    def poll_error(self, info):  # 错误上报
        currentevent = Event("Error", info, multiprocessing.current_process().pid)
        self.eventqueue.put(currentevent)

    def error(self):
        a = 1
        try:
            a.append("str")
        except Exception as Argument:  # 错误捕获和处理
            self.poll_error(Argument)


if __name__ == '__main__':
    err = multiprocessing.Queue()
    config = [(1, "a"), (2, "b")]
    print("main process running",multiprocessing.current_process().pid, "\n")

    # handler = eventHandler(err)
    handler_instance = multiprocessing.Process(target=EventHandler, args=(err,))
    handler_instance.start()  # 启动事件处理器

    mgr_process = multiprocessing.Process(target=WorkManager, args=(err, config))
    mgr_process.start()  # 启动工作管理器
    time.sleep(5)
    stop_event = Event("Instruction", "Stop handler", multiprocessing.current_process().pid)
    err.put(stop_event)  # 关闭事件处理器
