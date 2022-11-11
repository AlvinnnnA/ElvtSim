"""
这里是图形化测试工具！！
"""
import platform

from PySide6.QtCore import *
from PySide6.QtGui import (QAction, QTextCursor)
from PySide6.QtWidgets import *

from common_objects import *
from wheels import *
from GUI.sim_conf import *

import multiprocessing
import eventhandler
import sys
import traceback
import warnings
from threading import Thread


warnings.filterwarnings("ignore", category=DeprecationWarning)


class EmittingStr(QObject):
    textWritten = Signal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))
        loop = QEventLoop()
        QTimer.singleShot(100, loop.quit)
        loop.exec()


class Ui_TestWindow(object):
    def setupUi(self, TestWindow, rate):
        if not TestWindow.objectName():
            TestWindow.setObjectName(u"TestWindow")
        self.rate = rate
        TestWindow.resize(int(800/self.rate), int(600/self.rate))
        self.actionExit = QAction(TestWindow)
        self.actionExit.setObjectName(u"actionExit")

        self.centralwidget = QWidget(TestWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(440, 510, 291, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 460, 321, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 20, 681, 241))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_8.addWidget(self.label)

        self.pushButton_27 = QPushButton(self.layoutWidget)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.horizontalLayout_8.addWidget(self.pushButton_27)

        self.pushButton_28 = QPushButton(self.layoutWidget)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.horizontalLayout_8.addWidget(self.pushButton_28)

        self.pushButton_29 = QPushButton(self.layoutWidget)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.horizontalLayout_8.addWidget(self.pushButton_29)

        self.pushButton_30 = QPushButton(self.layoutWidget)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.horizontalLayout_8.addWidget(self.pushButton_30)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_9.addWidget(self.label_2)

        self.pushButton_31 = QPushButton(self.layoutWidget)
        self.pushButton_31.setObjectName(u"pushButton_31")

        self.horizontalLayout_9.addWidget(self.pushButton_31)

        self.pushButton_32 = QPushButton(self.layoutWidget)
        self.pushButton_32.setObjectName(u"pushButton_32")

        self.horizontalLayout_9.addWidget(self.pushButton_32)

        self.pushButton_33 = QPushButton(self.layoutWidget)
        self.pushButton_33.setObjectName(u"pushButton_33")

        self.horizontalLayout_9.addWidget(self.pushButton_33)

        self.pushButton_34 = QPushButton(self.layoutWidget)
        self.pushButton_34.setObjectName(u"pushButton_34")

        self.horizontalLayout_9.addWidget(self.pushButton_34)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.pushButton_11 = QPushButton(self.layoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_4.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_4.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.layoutWidget)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_4.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.layoutWidget)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_4.addWidget(self.pushButton_14)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.log_output = QTextEdit(self.centralwidget)
        self.log_output.setObjectName(u"textEdit")
        self.log_output.setGeometry(QRect(50, 270, 681, 181))
        TestWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TestWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuTest_tool = QMenu(self.menubar)
        self.menuTest_tool.setObjectName(u"menuTest_tool")
        TestWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TestWindow)
        self.statusbar.setObjectName(u"statusbar")
        TestWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTest_tool.menuAction())
        self.menuTest_tool.addAction(self.actionExit)

        self.retranslateUi(TestWindow)

        QMetaObject.connectSlotsByName(TestWindow)
        self.prompter = ElvtTeamEventPrompt()
    # setupUi

    def retranslateUi(self, TestWindow):
        TestWindow.setWindowTitle(QCoreApplication.translate("TestWindow", u"ElvtTeam test tool", None))
        self.actionExit.setText(QCoreApplication.translate("TestWindow", u"Exit", None))
        self.actionExit.triggered.connect(TestWindow.close)

        self.pushButton_2.setText(QCoreApplication.translate("TestWindow", u"Exit", None))
        self.pushButton_2.clicked.connect(TestWindow.close)
        self.pushButton.setText(QCoreApplication.translate("TestWindow", u"Reserved", None))
        self.pushButton.clicked.connect(TestWindow.close)

        self.checkBox.setText(QCoreApplication.translate("TestWindow", u"Config checker A", None))
        self.checkBox_2.setText(QCoreApplication.translate("TestWindow", u"Config checker B", None))

        self.label.setText(QCoreApplication.translate("TestWindow", u"Supporting modules", None))
        self.pushButton_27.setText(QCoreApplication.translate("TestWindow", u"Event handler", None))
        self.pushButton_27.clicked.connect(self.eventhandler_self_test)
        self.pushButton_28.setText(QCoreApplication.translate("TestWindow", u"Config generator", None))
        self.pushButton_28.clicked.connect(self.configgen_self_test)
        self.pushButton_29.setText(QCoreApplication.translate("TestWindow", u"Userinfo generator", None))
        self.pushButton_30.setText(QCoreApplication.translate("TestWindow", u"System log", None))

        self.label_2.setText(QCoreApplication.translate("TestWindow", u"Simulation\nmodule", None))
        self.pushButton_31.setText(QCoreApplication.translate("TestWindow", u"Config reader", None))
        self.pushButton_32.setText(QCoreApplication.translate("TestWindow", u"User reader", None))
        self.pushButton_33.setText(QCoreApplication.translate("TestWindow", u"User dispatcher", None))
        self.pushButton_34.setText(QCoreApplication.translate("TestWindow", u"Simulation Core", None))
        self.pushButton_34.clicked.connect(self.sim_core_test)

        self.label_3.setText(QCoreApplication.translate("TestWindow", u"GUI", None))
        self.pushButton_11.setText(QCoreApplication.translate("TestWindow", u"Error prompt", None))
        self.pushButton_11.clicked.connect(self.error_prompt_test)
        self.pushButton_12.setText(QCoreApplication.translate("TestWindow", u"Info dialog", None))
        self.pushButton_12.clicked.connect(self.info_diag_test)
        self.pushButton_13.setText(QCoreApplication.translate("TestWindow", u"Event error", None))
        self.pushButton_13.clicked.connect(self.handler_error_prompt)
        self.pushButton_14.setText(QCoreApplication.translate("TestWindow", u"Reserved", None))
        self.menuTest_tool.setTitle(QCoreApplication.translate("TestWindow", u"Test tool", None))
        sys.stdout = EmittingStr()
        self.log_output.connect(sys.stdout, SIGNAL("textWritten(QString)"), self.output_written)
        sys.stderr = EmittingStr()
        self.log_output.connect(sys.stderr, SIGNAL("textWritten(QString)"), self.output_written)

    @Slot()
    def output_written(self, text: str):
        # self.textEdit.clear()
        cursor = self.log_output.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.log_output.setTextCursor(cursor)
        self.log_output.ensureCursorVisible()

    @Slot()
    def eventhandler_self_test(self):
        eventhandler.self_test()

    @Slot()
    def configgen_self_test(self):
        wizard = ConfigWizard(self.rate)
        wizard.exec_()

    @Slot()
    def error_prompt_test(self):
        try:
            a = 1
            a.append("a")
        except AttributeError:
            error_event = Event("Error", traceback.format_exc(), multiprocessing.current_process().pid)
            self.prompter.event_prompt(error_event)

    @Slot()
    def info_diag_test(self):
        info = Event("Info", "This is a self test message!", multiprocessing.current_process().pid)
        self.prompter.event_prompt(info)

    @Slot()
    def handler_error_prompt(self):
        queue = multiprocessing.Queue()
        handler = eventhandler.EventHandler(queue)
        handler.activate_verbose()
        handler.use_front_handler()
        signal = handler.front_handler
        signal.event.connect(self.prompter.event_prompt)
        handler.activate_listener()

        eventhandler.suicide(queue)

        eventhandler.kill_handler(queue)

    def sim_core_test(self):
        # TODO 核心程序测试
        pass


class TestTool(QMainWindow):
    def __init__(self, rate):
        super().__init__()
        self.ui = Ui_TestWindow()
        self.ui.setupUi(self, rate)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = app.screens()[0]
    dpi = screen.devicePixelRatio() - 0.35
    if platform.system() == "Darwin":
        dpi = 1
    window = TestTool(dpi)
    window.show()
    sys.exit(app.exec())





