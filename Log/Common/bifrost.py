from datetime import datetime as dt


class Reporter:
    def __init__(self):
        self.logs = []

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


class Chime:
    def __init__(self):
        self.logs = []

    def _format_timestamp(self, timestamp: int) -> str:
        hours = timestamp // 3600 % 24
        minutes = timestamp // 60 % 60
        seconds = timestamp % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def info(self, timestamp: int, info: str):
        formatted_timestamp = self._format_timestamp(timestamp)
        entry = ["INFO", formatted_timestamp, info]
        self.logs.append(entry)

    def debug(self, timestamp: int, info: str):
        formatted_timestamp = self._format_timestamp(timestamp)
        entry = ["DEBUG", formatted_timestamp, info]
        self.logs.append(entry)

    def warning(self, timestamp: int, info: str):
        formatted_timestamp = self._format_timestamp(timestamp)
        entry = ["WARNING", formatted_timestamp, info]
        self.logs.append(entry)

    def error(self, timestamp: int, info: str):
        formatted_timestamp = self._format_timestamp(timestamp)
        entry = ["ERROR", formatted_timestamp, info]
        self.logs.append(entry)

    def critical(self, timestamp: int, info: str):
        formatted_timestamp = self._format_timestamp(timestamp)
        entry = ["CRITICAL", formatted_timestamp, info]
        self.logs.append(entry)
