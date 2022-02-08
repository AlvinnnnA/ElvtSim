"""
配置文件生成向导
"""

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
                               QProgressBar, QSizePolicy, QSpacerItem, QSpinBox,
                               QVBoxLayout, QWidget, QWizard, QWizardPage, QHBoxLayout, QListWidget, QListWidgetItem)

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

        self.elvt_cnt = QSpinBox(self.layoutWidget)  # 电梯数
        self.elvt_cnt.setMinimum(1)
        self.elvt_cnt.setObjectName(u"elvt_cnt")

        self.basic_info.addWidget(self.elvt_cnt)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.basic_info.addItem(self.verticalSpacer)

        self.label_floor_cnt = QLabel(self.layoutWidget)
        self.label_floor_cnt.setObjectName(u"label_floor_cnt")

        self.basic_info.addWidget(self.label_floor_cnt)

        self.floor_cnt = QSpinBox(self.layoutWidget)  # 楼层数
        self.floor_cnt.setMinimum(2)
        self.floor_cnt.setObjectName(u"floor_cnt")

        self.basic_info.addWidget(self.floor_cnt)

        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.basic_info.addItem(self.verticalSpacer_2)

        self.label_under_floors = QLabel(self.layoutWidget)
        self.label_under_floors.setObjectName(u"label_under_floors")

        self.basic_info.addWidget(self.label_under_floors)

        self.under_floors = QSpinBox(self.layoutWidget)  # 地下楼层数
        self.under_floors.setObjectName(u"under_floors")

        self.basic_info.addWidget(self.under_floors)

        NewSimConf.setPage(1, self.wizardPage1)
        self.wizardPage2 = QWizardPage()
        self.wizardPage2.setObjectName(u"wizardPage2")
        self.start_box_2 = QGroupBox(self.wizardPage2)
        self.start_box_2.setObjectName(u"start_box_2")
        self.start_box_2.setGeometry(QRect(0, 0, 401, 211))
        self.progressBar = QProgressBar(self.start_box_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 180, 381, 20))
        self.progressBar.setValue(0)
        self.label = QLabel(self.start_box_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 51, 16))
        self.elvt_box = QGroupBox(self.start_box_2)
        self.elvt_box.setObjectName(u"elvt_box")
        self.elvt_box.setGeometry(QRect(70, 20, 321, 151))
        self.listWidget = QListWidget(self.start_box_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 40, 51, 131))
        NewSimConf.setPage(2, self.wizardPage2)

        self.wizardPage3 = QWizardPage()
        self.wizardPage3.setObjectName(u"wizardPage3")
        self.title_3 = QLabel(self.wizardPage3)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(10, 20, 311, 71))
        self.widget = QWidget(self.wizardPage3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 100, 391, 101))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.name_fin_box = QHBoxLayout()
        self.name_fin_box.setObjectName(u"name_fin_box")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.name_fin_box.addWidget(self.label_3)

        self.cfg_name_final = QLabel(self.widget)
        self.cfg_name_final.setObjectName(u"cfg_name_final")

        self.name_fin_box.addWidget(self.cfg_name_final)

        self.verticalLayout.addLayout(self.name_fin_box)

        self.path_fin_box = QHBoxLayout()
        self.path_fin_box.setObjectName(u"path_fin_box")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.path_fin_box.addWidget(self.label_4)

        self.cfg_path_final = QLabel(self.widget)
        self.cfg_path_final.setObjectName(u"cfg_path_final")

        self.path_fin_box.addWidget(self.cfg_path_final)

        self.verticalLayout.addLayout(self.path_fin_box)

        NewSimConf.addPage(self.wizardPage3)

        NewSimConf.currentIdChanged.connect(self.on_page_done)

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
        self.title_3.setText(QCoreApplication.translate("NewSimConf",
                                                        u"<html><head/><body><p><span style=\" font-size:12pt;\">"
                                                        u"\u6210\u529f\u6dfb\u52a0\u4e86\u65b0\u7684\u4eff\u771f\u914d\u7f6e</span></p><p>"
                                                        u"\u4f60\u53ef\u4ee5\u5728\u4e3b\u754c\u9762\u4e2d\u7684\u4eff\u771f\u914d\u7f6e\u680f"
                                                        u"\u76ee\u4e2d\u627e\u5230\u65b0\u6dfb\u52a0\u7684\u914d\u7f6e</p><p><br/></p></body></html>",
                                                        None))
        self.label_3.setText(QCoreApplication.translate("NewSimConf",
                                                        u"<html><head/><body><p>\u65b0\u6dfb\u52a0\u7684\u914d\u7f6e\u540d\u4e3a\uff1a</p></body></html>",
                                                        None))
        self.cfg_name_final.setText(QCoreApplication.translate("NewSimConf", u"Not specified", None))
        self.label_4.setText(QCoreApplication.translate("NewSimConf",
                                                        u"<html><head/><body><p>\u65b0\u6dfb\u52a0\u7684\u914d\u7f6e\u8def\u5f84\u4e3a\uff1a</p></body></html>",
                                                        None))
        self.cfg_path_final.setText(QCoreApplication.translate("NewSimConf", u"Not Specified", None))

        self.listWidget.itemClicked.connect(self.change_conf_elvt)

        self.current_working_dict = {}
        self.current_working_dict["Elevators"] = []
        # retranslateUi

    @Slot()
    def on_page_done(self, id):
        if id == 2:
            self.done_basic()
            for i in range(1, self.elvt_cnt.value()+1):
                conf_elvt_dict = {"Index": i}
                self.current_working_dict["Elevators"].append(conf_elvt_dict)
            print(self.current_working_dict)
            pass
        elif id == 2:
            self.done_steptwo()

    @Slot()
    def done_basic(self):  # 第一页结束，保存配置信息
        def items(value):
            itemlist = []
            for i in range(1, value+1):
                itemlist.append(str(i))
            return itemlist
        self.current_working_dict["elvt_cnt"] = self.elvt_cnt.value()
        #print(type(self.elvt_cnt.value()),  self.elvt_cnt.value())
        self.current_working_dict["floor_cnt"] = self.floor_cnt.value()
        self.current_working_dict["under_floors"] = self.under_floors.value()
        self.listWidget.clear()
        self.listWidget.addItems(items(self.current_working_dict["elvt_cnt"]))

    @Slot()
    def change_conf_elvt(self, item: QListWidgetItem):  # 更改正在配置的电梯对象
        for elevator in self.current_working_dict["Elevators"]:
            if elevator["Index"] == item.text:
                current_conf_elvt = elevator
                break

    @Slot()
    def done_steptwo(self):  #完成第二页，保存配置信息
        pass






class ConfigWizard(QWizard):
    def __init__(self, rate):
        super(ConfigWizard, self).__init__()
        self.ui = Ui_NewSimConf()
        self.ui.setupUi(self, rate)
        #self.show()