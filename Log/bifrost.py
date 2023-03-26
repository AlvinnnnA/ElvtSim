import os.path
from datetime import datetime as dt
import sqlite3
import logging

from Scheduler.Thread import convert_time

REPORTER_DEFAULT_LOG = {
    "mode": "log",
    "path": f"Data/{dt.strftime(dt.now(), '%m-%d-%H-%M')}.log",
    "level": "DEBUG"}
REPORTER_DEFAULT_DB = {
    "mode": "sql",
    "path": f"Data/database.sqlite3"}


class sql_ops:
    def __init__(self, conf, batch_number=-1):
        self.conn = sqlite3.connect(conf["path"])
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS metadata (batch_number integer, timestamp_log text)")
        self.conn.commit()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS sim_log (batch_number integer, timestamp_log text, level_log text, message text)")
        self.conn.commit()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS user_log (batch_number integer, internal_time text, uid integer, event text)")
        self.conn.commit()
        if batch_number<0:
            query_result = self.cursor.execute('SELECT max(batch_number) FROM metadata').fetchone()
            if query_result and query_result[0]:
                self.batch_number = query_result[0] + 1
            else:
                self.batch_number = 1
        else:
            self.batch_number = batch_number
        #print(self.batch_number, str(dt.now()))
        self.cursor.execute("insert into metadata (batch_number, timestamp_log) values (?,?)",
                            (self.batch_number, str(dt.now())))
        self.conn.commit()

    def info(self, info: str):
        self.cursor.execute(
            "insert into sim_log (batch_number, timestamp_log,level_log,message) values (?,?,?,?)",
            (self.batch_number, str(dt.now()), "INFO", info))
        self.conn.commit()

    def debug(self, info: str):
        self.cursor.execute(
            "insert into sim_log (batch_number, timestamp_log,level_log,message) values (?,?,?,?)",
            (self.batch_number, str(dt.now()), "DEBUG", info))
        self.conn.commit()

    def warning(self, info: str):
        self.cursor.execute(
            "insert into sim_log (batch_number, timestamp_log,level_log,message) values (?,?,?,?)",
            (self.batch_number, str(dt.now()), "WARNING", info))
        self.conn.commit()

    def error(self, info: str):
        self.cursor.execute(
            "insert into sim_log (batch_number, timestamp_log,level_log,message) values (?,?,?,?)",
            (self.batch_number, str(dt.now()), "ERROR", info))
        self.conn.commit()

    def critical(self, info: str):
        self.cursor.execute(
            "insert into sim_log (batch_number, timestamp_log,level_log,message) values (?,?,?,?)",
            (self.batch_number, str(dt.now()), "CRITICAL", info))
        self.conn.commit()

    def append(self, info: list):
        self.cursor.execute(
            "insert into user_log (batch_number, internal_time,uid,event) values (?,?,?,?)",
            (self.batch_number, info[2], info[1], info[0]))
        self.conn.commit()




class Reporter:
    def __init__(self, conf=REPORTER_DEFAULT_LOG):
        if conf["mode"] == "log":
            self.conf = conf
            self.logger = logging.getLogger()
            # Set the logging level to INFO
            self.logger.setLevel(conf["level"])
            # Create a file handler and set its logging level to INFO
            self.file_handler = logging.FileHandler(conf["path"])
            self.file_handler.setLevel(conf["level"])
            # Create a formatter and add it to the file handler
            self.formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
            self.file_handler.setFormatter(self.formatter)
            # Add the file handler to the logger
            self.logger.addHandler(self.file_handler)
            self.user_logs = []
        elif conf["mode"] == "sql":
            self.conf = conf
            self.logger = sql_ops(conf)
            self.batch_number = self.logger.batch_number
            self.user_logs = self.logger
        else:
            raise Exception("Invalid mode")

    def sql_re_init(self):
        if self.conf["mode"] == "sql":
            self.logger = sql_ops(self.conf, self.batch_number)
            self.batch_number = self.logger.batch_number
            self.user_logs = self.logger
        else:
            pass

    def info(self, info: str):
        self.logger.info(info)

    def debug(self, info: str):
        self.logger.debug(info)

    def warning(self, info: str):
        self.logger.warning(info)

    def error(self, info: str):
        self.logger.error(info)

    def critical(self, info: str):
        self.logger.critical(info)

    def _format_timestamp(self, timestamp: int) -> str:
        hours = timestamp // 3600 % 24
        minutes = timestamp // 60 % 60
        seconds = timestamp % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def into(self, timestamp: int, uid,floor,elevator):
        formatted_timestamp = self._format_timestamp(timestamp)
        entry = ["INTO", uid,formatted_timestamp,floor,elevator]
        self.user_logs.append(entry)

    def exit(self, timestamp: int, uid,floor,elevator):
        formatted_timestamp = self._format_timestamp(timestamp)
        entry = ["EXIT", uid, formatted_timestamp,floor,elevator]
        # print(entry) if timestamp > convert_time.time_to_num("19:55:00") else None
        self.user_logs.append(entry)

    def call(self, timestamp: int, uid, floor,elevator):
        formatted_timestamp = self._format_timestamp(timestamp)
        entry = ["CALL", uid, formatted_timestamp, floor,elevator]
        # print(entry) if timestamp > convert_time.time_to_num("19:55:00") else None
        self.user_logs.append(entry)

    def user_to_file(self):
        self.info("User logs are being stored in the file")
        if self.conf["mode"] == "log":
            # print(self.user_logs[:3])
            with open(f"user_{dt.strftime(dt.now(), '%m-%d-%H-%M')}.csv", "w") as f:
                for entry in self.user_logs:
                    f.write(",".join(map(str, entry)) + "\n")
        else:
            self.info("User logs are stored in the database")
