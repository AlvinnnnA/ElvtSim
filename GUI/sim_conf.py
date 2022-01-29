# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_conf.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QProgressBar, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget, QWizard, QWizardPage)

class Ui_NewSimConf(object):
    def setupUi(self, NewSimConf, rate):
        if not NewSimConf.objectName():
            NewSimConf.setObjectName(u"NewSimConf")
        NewSimConf.setWindowModality(Qt.ApplicationModal)
        NewSimConf.resize(423/rate, 326/rate)
        NewSimConf.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        NewSimConf.setSizeGripEnabled(False)
        NewSimConf.setModal(True)
        NewSimConf.setWizardStyle(QWizard.ModernStyle)
        self.wizardPage1 = QWizardPage()
        self.wizardPage1.setObjectName(u"wizardPage1")
        self.start_box = QGroupBox(self.wizardPage1)
        self.start_box.setObjectName(u"start_box")
        self.start_box.setGeometry(QRect(10, 10, 381, 201))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_box.sizePolicy().hasHeightForWidth())
        self.start_box.setSizePolicy(sizePolicy)
        self.layoutWidget = QWidget(self.start_box)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 64, 155))
        self.basic_info = QVBoxLayout(self.layoutWidget)
        self.basic_info.setObjectName(u"basic_info")
        self.basic_info.setContentsMargins(0, 0, 0, 0)
        self.label_elvt_cnt = QLabel(self.layoutWidget)
        self.label_elvt_cnt.setObjectName(u"label_elvt_cnt")

        self.basic_info.addWidget(self.label_elvt_cnt)

        self.elvt_cnt = QSpinBox(self.layoutWidget)
        self.elvt_cnt.setObjectName(u"elvt_cnt")

        self.basic_info.addWidget(self.elvt_cnt)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.basic_info.addItem(self.verticalSpacer)

        self.label_floor_cnt = QLabel(self.layoutWidget)
        self.label_floor_cnt.setObjectName(u"label_floor_cnt")

        self.basic_info.addWidget(self.label_floor_cnt)

        self.floor_cnt = QSpinBox(self.layoutWidget)
        self.floor_cnt.setObjectName(u"floor_cnt")

        self.basic_info.addWidget(self.floor_cnt)

        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.basic_info.addItem(self.verticalSpacer_2)

        self.label_under_floors = QLabel(self.layoutWidget)
        self.label_under_floors.setObjectName(u"label_under_floors")

        self.basic_info.addWidget(self.label_under_floors)

        self.under_floors = QSpinBox(self.layoutWidget)
        self.under_floors.setObjectName(u"under_floors")

        self.basic_info.addWidget(self.under_floors)

        NewSimConf.setPage(1, self.wizardPage1)
        self.wizardPage2 = QWizardPage()
        self.wizardPage2.setObjectName(u"wizardPage2")
        self.start_box_2 = QGroupBox(self.wizardPage2)
        self.start_box_2.setObjectName(u"start_box_2")
        self.start_box_2.setGeometry(QRect(0, 0, 401, 211))
        self.comboBox = QComboBox(self.start_box_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(150, 20, 91, 22))
        self.progressBar = QProgressBar(self.start_box_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 180, 381, 20))
        self.progressBar.setValue(0)
        self.label = QLabel(self.start_box_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 131, 16))
        self.elvt_box = QGroupBox(self.start_box_2)
        self.elvt_box.setObjectName(u"elvt_box")
        self.elvt_box.setGeometry(QRect(10, 40, 381, 131))
        NewSimConf.setPage(2, self.wizardPage2)

        self.retranslateUi(NewSimConf)
        self.comboBox.currentTextChanged.connect(self.progressBar.reset)

        QMetaObject.connectSlotsByName(NewSimConf)
    # setupUi

    def retranslateUi(self, NewSimConf):
        NewSimConf.setWindowTitle(QCoreApplication.translate("NewSimConf", u"\u521b\u5efa\u4eff\u771f\u914d\u7f6e", None))
        self.wizardPage1.setTitle(QCoreApplication.translate("NewSimConf", u"\u7b2c\u4e00\u6b65\uff1a\u786e\u5b9a\u4e00\u4e9b\u57fa\u672c\u4fe1\u606f", None))
        self.wizardPage1.setSubTitle(QCoreApplication.translate("NewSimConf", u"\u8bf7\u5148\u8f93\u5165\u4e00\u4e9b\u57fa\u672c\u7684\u914d\u7f6e\u8981\u6c42", None))
        self.start_box.setTitle(QCoreApplication.translate("NewSimConf", u"\u57fa\u672c\u4fe1\u606f", None))
        self.label_elvt_cnt.setText(QCoreApplication.translate("NewSimConf", u"\u7535\u68af\u53f0\u6570", None))
        self.elvt_cnt.setSuffix("")
        self.label_floor_cnt.setText(QCoreApplication.translate("NewSimConf", u"\u5927\u697c\u603b\u5c42\u6570", None))
        self.label_under_floors.setText(QCoreApplication.translate("NewSimConf", u"\u5730\u4e0b\u697c\u5c42\u6570", None))
        self.wizardPage2.setTitle(QCoreApplication.translate("NewSimConf", u"\u7b2c\u4e8c\u6b65 \u8f93\u5165\u4e00\u4e9b\u5173\u952e\u7684\u4fe1\u606f", None))
        self.wizardPage2.setSubTitle(QCoreApplication.translate("NewSimConf", u"\u8bf7\u8f93\u5165\u6bcf\u53f0\u7535\u68af\u7684\u914d\u7f6e", None))
        self.start_box_2.setTitle(QCoreApplication.translate("NewSimConf", u"\u7535\u68af\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("NewSimConf", u"\u8bf7\u5148\u9009\u62e9\u8981\u7f16\u8f91\u7684\u7535\u68af", None))
        self.elvt_box.setTitle(QCoreApplication.translate("NewSimConf", u"\u7535\u68af\u4fe1\u606f", None))
    # retranslateUi

    @Slot()
    def done_basic(self):
        pass

    @Slot()
    def change_conf_elvt(self):
        pass

    @Slot()
    def done_steptwo(self):
        pass






class ConfigWizard(QWizard):
    def __init__(self, rate):
        super(ConfigWizard, self).__init__()
        self.ui = Ui_NewSimConf()
        self.ui.setupUi(self, rate)
        #self.show()