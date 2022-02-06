"""
    @Slot()
    def event_prompt(self,Event):
        err_prompt = ElvtTeamEventPrompt()

        if event.eventtype == "Error":
            err_prompt.setText("发生了错误！")
            err_prompt.setIcon(err_prompt.Icon.Critical)
            err_prompt.setWindowTitle("错误")
            err_prompt.setDetailedText("Error occurred at process " +
                                       str(event.pid) +
                                       "\nError info is as belows\n" +
                                       event.eventinfo)

        elif event.eventtype == "Info":
            err_prompt.setText("提示")
            err_prompt.setIcon(err_prompt.Icon.Information)
            err_prompt.setWindowTitle("信息")
            err_prompt.setDetailedText("Info raised at process " +
                                       str(event.pid) +
                                       "\nInfo reads as belows\n" +
                                       event.eventinfo)

        err_prompt.setStandardButtons(QMessageBox.Ok)
        err_prompt.exec()
"""
from PySide6.QtWidgets import QMessageBox, QTextEdit
from PySide6.QtCore import Slot, Signal, QObject, QEventLoop
from common_objects import *


class EmittingStr(QObject):
    textWritten = Signal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))
        loop = QEventLoop()
        QTimer.singleShot(100, loop.quit)
        loop.exec()


class ElvtTeamEventPrompt(QMessageBox):  # 错误和信息提示

    # This is a much better way to extend __init__
    def __init__(self, *args, **kwargs):
        super(ElvtTeamEventPrompt, self).__init__(*args, **kwargs)
        # Anything else you want goes below

    # We only need to extend resizeEvent, not every event.
    def resizeEvent(self, event):

        result = super(ElvtTeamEventPrompt, self).resizeEvent(event)

        details_box = self.findChild(QTextEdit)
        # 'is not' is better style than '!=' for None
        if details_box is not None:
            details_box.setFixedSize(details_box.sizeHint())

        return result

    @Slot()
    def event_prompt(self, event_dict):
        # 实现传入字典和事件自动判断处理
        if isinstance(event_dict, dict):
            event = make_event_instance(event_dict)
        elif isinstance(event_dict, Event):
            event = event_dict
        else:
            raise TypeError("传入了错误的对象类型")

        if event.eventtype == "Error":
            self.setText("发生了错误！")
            self.setIcon(self.Icon.Critical)
            self.setWindowTitle("错误")
            self.setDetailedText("Error occurred at process " +
                                       str(event.pid) +
                                       "\nError info is as belows\n" +
                                       event.eventinfo)

        elif event.eventtype == "Info":
            self.setText("提示")
            self.setIcon(self.Icon.Information)
            self.setWindowTitle("信息")
            self.setDetailedText("Info raised at process " +
                                       str(event.pid) +
                                       "\nInfo reads as belows\n" +
                                       event.eventinfo)

        self.setStandardButtons(QMessageBox.Ok)
        self.exec()
