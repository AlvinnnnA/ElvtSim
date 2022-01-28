# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Slot, QObject)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform, QScreen, QGuiApplication)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QTableView, QToolButton, QWidget)
import sys
from GUI.sim_conf import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow, rate):
        self.rate = rate
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(int(800/self.rate), int(600/self.rate))
        #sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        #MainWindow.setSizePolicy(sizePolicy)
        self.actionGlobal_config = QAction(MainWindow)
        self.actionGlobal_config.setObjectName(u"actionGlobal_config")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 411, 401))
        self.configs = QHBoxLayout(self.layoutWidget)
        self.configs.setObjectName(u"configs")
        self.configs.setContentsMargins(0, 0, 0, 0)
        self.sim_conf_cont = QGroupBox(self.layoutWidget)
        self.sim_conf_cont.setObjectName(u"sim_conf_cont")
        self.sim_config_view = QTableView(self.sim_conf_cont)
        self.sim_config_view.setObjectName(u"sim_config_view")
        self.sim_config_view.setGeometry(QRect(10, 20, 171, 331))
        self.sim_config_view.setShowGrid(True)
        self.sim_config_view.setSortingEnabled(True)
        self.layoutWidget1 = QWidget(self.sim_conf_cont)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 360, 81, 24))
        self.sim_conf_toolstools = QHBoxLayout(self.layoutWidget1)
        self.sim_conf_toolstools.setObjectName(u"sim_conf_toolstools")
        self.sim_conf_toolstools.setContentsMargins(0, 0, 0, 0)
        self.sim_add = QToolButton(self.layoutWidget1)
        self.sim_add.setObjectName(u"sim_add")

        self.sim_conf_toolstools.addWidget(self.sim_add)

        self.sim_edit = QToolButton(self.layoutWidget1)
        self.sim_edit.setObjectName(u"sim_edit")

        self.sim_conf_toolstools.addWidget(self.sim_edit)

        self.sim_refresh = QToolButton(self.layoutWidget1)
        self.sim_refresh.setObjectName(u"sim_refresh")

        self.sim_conf_toolstools.addWidget(self.sim_refresh)


        self.configs.addWidget(self.sim_conf_cont)

        self.user_info_cont = QGroupBox(self.layoutWidget)
        self.user_info_cont.setObjectName(u"user_info_cont")
        self.user_info_view = QTableView(self.user_info_cont)
        self.user_info_view.setObjectName(u"user_info_view")
        self.user_info_view.setGeometry(QRect(10, 20, 171, 331))
        self.user_info_view.setShowGrid(True)
        self.user_info_view.setSortingEnabled(True)
        self.layoutWidget2 = QWidget(self.user_info_cont)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 360, 81, 24))
        self.user_conf_tools = QHBoxLayout(self.layoutWidget2)
        self.user_conf_tools.setObjectName(u"user_conf_tools")
        self.user_conf_tools.setContentsMargins(0, 0, 0, 0)
        self.usr_add = QToolButton(self.layoutWidget2)
        self.usr_add.setObjectName(u"usr_add")

        self.user_conf_tools.addWidget(self.usr_add)

        self.usr_edit = QToolButton(self.layoutWidget2)
        self.usr_edit.setObjectName(u"usr_edit")

        self.user_conf_tools.addWidget(self.usr_edit)

        self.usr_refresh = QToolButton(self.layoutWidget2)
        self.usr_refresh.setObjectName(u"usr_refresh")

        self.user_conf_tools.addWidget(self.usr_refresh)


        self.configs.addWidget(self.user_info_cont)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(620, 530, 158, 26))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.exit = QPushButton(self.widget)
        self.exit.setObjectName(u"exit")

        self.horizontalLayout.addWidget(self.exit)

        self.start_sim = QPushButton(self.widget)
        self.start_sim.setObjectName(u"start_sim")

        self.horizontalLayout.addWidget(self.start_sim)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.setttings = QMenu(self.menubar)
        self.setttings.setObjectName(u"setttings")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.setttings.menuAction())
        self.setttings.addAction(self.actionGlobal_config)
        self.setttings.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.exit.clicked.connect(MainWindow.close)
        self.sim_refresh.pressed.connect(self.sim_config_view.reset)
        self.usr_refresh.pressed.connect(self.user_info_view.reset)
        self.actionExit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u914d\u7f6e", None))
        self.actionGlobal_config.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5c40\u914d\u7f6e", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.sim_conf_cont.setTitle(QCoreApplication.translate("MainWindow", u"\u4eff\u771f\u914d\u7f6e\u6570\u636e", None))
        self.sim_add.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.sim_add.clicked.connect(self.conf_wizard)
        self.sim_edit.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.sim_refresh.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.user_info_cont.setTitle(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u4fe1\u606f", None))
        self.usr_add.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.usr_edit.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.usr_refresh.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.start_sim.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4eff\u771f", None))
        self.setttings.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
    # retranslateUi

    @Slot()
    def error_handle(self):
        pass

    @Slot()
    def event_handle(self):
        pass

    @Slot()
    def process_handle(self):
        pass

    @Slot()
    def conf_wizard(self):
        wizard = ConfigWizard(self.rate)
        wizard.exec_()
        #return app.exec_()


