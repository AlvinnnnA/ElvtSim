import logging
import logging.config
import sys
import time
import os
import shutil
import re


def getLogging(confName = "applog"):
    logging.config.fileConfig("logging.conf")
    return logging.getLogger(confName)


rootlogger = logging.getLogger()
logging.warning(("hdd is so seductive"))
logger = logging.getLogger('applog')
logger.warning("supervisor of postgrads, warning")

# Log等级总开关
logger.setLevel(logging.INFO)
# 定义输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d]- %(levelname)s: %(message)s")

#利用sys.stdout将print行导向到你定义的日志文件中
# 备份stdout route
stdout_backup = sys.stdout
# 这个message.log就是我们自行定义的日志文件，日志信息会导入到这个文件里！
log_file = open("message.log", "w")
# redirect print output to log file
sys.stdout = log_file
print("现在所有的信息都会存储在这个文档里")

# 接下来的内容是需要执行的一些命令
...
log_file.close()
# 将输出恢复到初始模式
sys.stdout = stdout_backup
print("完毕")

if __name__ == '__main__':

    # 先实例化再进行调用日志模块
    logger = logging.getLogger('applog')
    for i in range(1):
        logger.info("syn_is_doing_handjob")
        logger.warning("There's whores in the house")