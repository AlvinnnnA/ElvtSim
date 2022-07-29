import logging
import time
import os
import shutil
import re
from logging.handlers import RotatingFileHandler
from multiprocessing import Process



class Logger(object):
    # 建立日期类
    # type_name为日志所在文件夹名字， log_content为要保留日志文件夹数量
    def __init__(self, type_name, log_content):
        self.type_name = type_name
        self.log_path, self.path = self.log_start()
        self.date_path = os.path.dirname(self.path)
        self.all_path = os.path.dirname(self.date_path)
        self.log_content = log_content
        # self.del_log()

    # path为存放日志的文件夹目录
    # log_path为日志文件的完整路径

    def log_start(self):
        local_time = time.strftime("%Y_%m_%d", time.localtime())
        complete_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        # path = os.path.join(os.getcwd(), "Worklog", local_time) + "_" + self.type_name + ".log"
        path = os.path.join(os.getcwd(), "Simlog", local_time, self.type_name)
        # 路径为，LOG文件夹，时间，日志文件名
        if not os.path.exists(path):
            os.makedirs(path)
            # 若没有该路径就创建该路径
        log_path = os.path.join(path, "%s_" % self.type_name) + complete_time + ".log"
        # 给创建的日志文件命名（！！！！！！！！！！！！！！！！！！！这里更改导出的日志文件类型！！！！！！！！！）
        file_log = open(log_path, "a")
        print(log_path, path)
        return log_path, path

    # 设置每份日志最大内存为maxBytes=1024 * 10, 超过该内存自动将日志切割到新日志文件中，
    # 设置backupCount=5，若新增的日志数量超过五个，自动将五个中旧的日志删除，保留最新的日志并数量保持为五个

    def log_main(self, sign, information):
        write_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        logger = logging.getLogger('mylogger')
        logger.setLevel(level=logging.DEBUG)
        fmt = '%(asctime)s - %(levelname)s : %(message)s'
        format_str = logging.Formatter(fmt)
        fh = RotatingFileHandler(self.log_path, maxBytes=1024 * 10, backupCount=5, encoding="utf-8")
        fh.namer = lambda x: self.path + r"\%s_%s_" % (self.type_name, write_time) + x.split(".")[-1] + ".log"

        fh.setFormatter(fmt=format_str)
        logger.addHandler(fh)

        if sign == "debug":
            logger.debug(information)
        elif sign == "info":
            logger.info(information)
        elif sign == "warning":
            logger.warning(information)
        elif sign == "error":
            logger.error(information)
        elif sign == "critical":
            logger.critical(information)

        logger.removeHandler(fh)

    # # 删除超过保留数量的日志文件夹，
    # # 例如log_content设置为30，日志文件夹超过30个时就会删除多余的日志文件夹，
    # # 让日志文件夹始终保持30个
    def del_log(self):
        if not os.listdir(self.all_path):
            return
        print(os.listdir(self.all_path))
        date_list = []
        for file_name in os.listdir(self.all_path):
            if re.fullmatch(r"\d{4}_\d{2}_\d{2}", file_name):
                all_name = os.path.join(self.all_path, file_name)
                date_list.append(all_name)
        print(date_list)
        # exit()
        if len(date_list) > self.log_content:
            difference_value = len(date_list) - self.log_content
            date_list.sort()
        # exit()
            for i in range(difference_value):
                shutil.rmtree(date_list[i], ignore_errors=True)
                if os.path.isfile(date_list[i]):
                    os.remove(date_list[i])
                else:
                    pass

    # 编写五种报告类型的函数
    def debug(self, information):
        sign = "debug"
        self.log_main(sign, information)

    def info(self, information):
        sign = "info"
        self.log_main(sign, information)

    def warning(self, information):
        sign = "warning"
        self.log_main(sign, information)

    def error(self, information):
        sign = "error"
        self.log_main(sign, information)

    def critical(self, information):
        sign = "critical"
        self.log_main(sign, information)


def long_time_task(i):
    logger.info('子进程: {} - 任务{}'.format(os.getpid(), i))
    time.sleep(2)
    logger.warning("结果: {}".format(8 ** 20))


if __name__ == '__main__':

    # 先实例化再进行调用日志模块
    logger = Logger("sim_log1", 2)
    for i in range(1):
        logger.info("当前母进程:".format(os.getpid()))
        start = time.time()
        p1 = Process(target=long_time_task, args=(1,))
        p2 = Process(target=long_time_task, args=(2,))
        logger.info('等待所有子进程完成。')
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        end = time.time()
        logger.warning("总共用时{}秒".format((end - start)))