# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_wiz_wip.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget,
    QWizard, QWizardPage)

class Ui_NewSimConf(object):
    def setupUi(self, NewSimConf):
        if not NewSimConf.objectName():
            NewSimConf.setObjectName(u"NewSimConf")
        NewSimConf.setWindowModality(Qt.ApplicationModal)
        NewSimConf.resize(423, 326)
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
        self.baisc_info = QVBoxLayout(self.layoutWidget)
        self.baisc_info.setObjectName(u"baisc_info")
        self.baisc_info.setContentsMargins(0, 0, 0, 0)
        self.label_elvt_cnt = QLabel(self.layoutWidget)
        self.label_elvt_cnt.setObjectName(u"label_elvt_cnt")

        self.baisc_info.addWidget(self.label_elvt_cnt)

        self.elvt_cnt = QSpinBox(self.layoutWidget)
        self.elvt_cnt.setObjectName(u"elvt_cnt")

        self.baisc_info.addWidget(self.elvt_cnt)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.baisc_info.addItem(self.verticalSpacer)

        self.label_floor_cnt = QLabel(self.layoutWidget)
        self.label_floor_cnt.setObjectName(u"label_floor_cnt")

        self.baisc_info.addWidget(self.label_floor_cnt)

        self.floor_cnt = QSpinBox(self.layoutWidget)
        self.floor_cnt.setObjectName(u"floor_cnt")

        self.baisc_info.addWidget(self.floor_cnt)

        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.baisc_info.addItem(self.verticalSpacer_2)

        self.label_under_floors = QLabel(self.layoutWidget)
        self.label_under_floors.setObjectName(u"label_under_floors")

        self.baisc_info.addWidget(self.label_under_floors)

        self.under_floors = QSpinBox(self.layoutWidget)
        self.under_floors.setObjectName(u"under_floors")

        self.baisc_info.addWidget(self.under_floors)

        NewSimConf.setPage(1, self.wizardPage1)
        self.wizardPage2 = QWizardPage()
        self.wizardPage2.setObjectName(u"wizardPage2")
        self.start_box_2 = QGroupBox(self.wizardPage2)
        self.start_box_2.setObjectName(u"start_box_2")
        self.start_box_2.setGeometry(QRect(0, 0, 401, 211))
        self.progressBar = QProgressBar(self.start_box_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 180, 381, 20))
        self.progressBar.setValue(24)
        self.label = QLabel(self.start_box_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 51, 16))
        self.elvt_box = QGroupBox(self.start_box_2)
        self.elvt_box.setObjectName(u"elvt_box")
        self.elvt_box.setGeometry(QRect(70, 20, 321, 151))
        self.advanced_setting = QPushButton(self.elvt_box)
        self.advanced_setting.setObjectName(u"advanced_setting")
        self.advanced_setting.setGeometry(QRect(240, 30, 61, 20))
        self.elvt_capacity = QLineEdit(self.elvt_box)
        self.elvt_capacity.setObjectName(u"elvt_capacity")
        self.elvt_capacity.setGeometry(QRect(70, 120, 31, 21))
        self.elvt_priority = QLineEdit(self.elvt_box)
        self.elvt_priority.setObjectName(u"elvt_priority")
        self.elvt_priority.setGeometry(QRect(70, 90, 31, 21))
        self.label_2 = QLabel(self.elvt_box)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 49, 16))
        self.label_5 = QLabel(self.elvt_box)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 90, 49, 16))
        self.label_6 = QLabel(self.elvt_box)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 120, 49, 16))
        self.layoutWidget1 = QWidget(self.elvt_box)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(70, 30, 158, 48))
        self.floors_cfg_group = QGridLayout(self.layoutWidget1)
        self.floors_cfg_group.setObjectName(u"floors_cfg_group")
        self.floors_cfg_group.setContentsMargins(0, 0, 0, 0)
        self.odd_floors = QCheckBox(self.layoutWidget1)
        self.odd_floors.setObjectName(u"odd_floors")

        self.floors_cfg_group.addWidget(self.odd_floors, 0, 0, 1, 1)

        self.even_floors = QCheckBox(self.layoutWidget1)
        self.even_floors.setObjectName(u"even_floors")

        self.floors_cfg_group.addWidget(self.even_floors, 0, 1, 1, 1)

        self.low_floors = QCheckBox(self.layoutWidget1)
        self.low_floors.setObjectName(u"low_floors")

        self.floors_cfg_group.addWidget(self.low_floors, 1, 0, 1, 1)

        self.high_floors = QCheckBox(self.layoutWidget1)
        self.high_floors.setObjectName(u"high_floors")

        self.floors_cfg_group.addWidget(self.high_floors, 1, 1, 1, 1)

        self.listWidget = QListWidget(self.start_box_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 40, 51, 131))
        NewSimConf.setPage(2, self.wizardPage2)
        self.wizardPage3 = QWizardPage()
        self.wizardPage3.setObjectName(u"wizardPage3")
        self.title_3 = QLabel(self.wizardPage3)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(10, 20, 311, 71))
        self.layoutWidget2 = QWidget(self.wizardPage3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 100, 391, 101))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.name_fin_box = QHBoxLayout()
        self.name_fin_box.setObjectName(u"name_fin_box")
        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.name_fin_box.addWidget(self.label_3)

        self.cfg_name_final = QLabel(self.layoutWidget2)
        self.cfg_name_final.setObjectName(u"cfg_name_final")

        self.name_fin_box.addWidget(self.cfg_name_final)


        self.verticalLayout.addLayout(self.name_fin_box)

        self.path_fin_box = QHBoxLayout()
        self.path_fin_box.setObjectName(u"path_fin_box")
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.path_fin_box.addWidget(self.label_4)

        self.cfg_path_final = QLabel(self.layoutWidget2)
        self.cfg_path_final.setObjectName(u"cfg_path_final")

        self.path_fin_box.addWidget(self.cfg_path_final)


        self.verticalLayout.addLayout(self.path_fin_box)

        NewSimConf.addPage(self.wizardPage3)

        self.retranslateUi(NewSimConf)

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
        self.label.setText(QCoreApplication.translate("NewSimConf", u"<html><head/><body><p>\u9009\u62e9\u7535\u68af</p></body></html>", None))
        self.elvt_box.setTitle(QCoreApplication.translate("NewSimConf", u"\u7535\u68af\u4fe1\u606f", None))
        self.advanced_setting.setText(QCoreApplication.translate("NewSimConf", u"\u9ad8\u7ea7\u914d\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("NewSimConf", u"\u697c\u5c42\u8bbe\u7f6e", None))
        self.label_5.setText(QCoreApplication.translate("NewSimConf", u"\u4f18\u5148\u7ea7", None))
        self.label_6.setText(QCoreApplication.translate("NewSimConf", u"\u4eba\u5458\u5bb9\u91cf", None))
        self.odd_floors.setText(QCoreApplication.translate("NewSimConf", u"\u5947\u6570\u5c42", None))
        self.even_floors.setText(QCoreApplication.translate("NewSimConf", u"\u5076\u6570\u5c42", None))
        self.low_floors.setText(QCoreApplication.translate("NewSimConf", u"\u4f4e\u697c\u5c42", None))
        self.high_floors.setText(QCoreApplication.translate("NewSimConf", u"\u9ad8\u697c\u5c42", None))
        self.title_3.setText(QCoreApplication.translate("NewSimConf", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u6210\u529f\u6dfb\u52a0\u4e86\u65b0\u7684\u4eff\u771f\u914d\u7f6e</span></p><p>\u4f60\u53ef\u4ee5\u5728\u4e3b\u754c\u9762\u4e2d\u7684\u4eff\u771f\u914d\u7f6e\u680f\u76ee\u4e2d\u627e\u5230\u65b0\u6dfb\u52a0\u7684\u914d\u7f6e</p><p><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("NewSimConf", u"<html><head/><body><p>\u65b0\u6dfb\u52a0\u7684\u914d\u7f6e\u540d\u4e3a\uff1a</p></body></html>", None))
        self.cfg_name_final.setText(QCoreApplication.translate("NewSimConf", u"Not specified", None))
        self.label_4.setText(QCoreApplication.translate("NewSimConf", u"<html><head/><body><p>\u65b0\u6dfb\u52a0\u7684\u914d\u7f6e\u8def\u5f84\u4e3a\uff1a</p></body></html>", None))
        self.cfg_path_final.setText(QCoreApplication.translate("NewSimConf", u"Not Specified", None))
    # retranslateUi

