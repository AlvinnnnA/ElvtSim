import json
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from GUI.mainwindow import Ui_MainWindow
from GUI.configgen import UIConfig

CONF_PATH = "GUI/conf"


def get_frontend_conf():
    path = CONF_PATH
    try:
        with open(path + "front_conf.json") as file:
            conf = UIConfig(json.load(file))
    except:
        with open(path + "default.json") as file:
            conf = UIConfig(json.load(file))
    finally:
        default_dict = {
            "lang": 0,
            "verbosity": 0
        }
        conf = UIConfig(default_dict)
        return conf


class MainWindow(QMainWindow):
    def __init__(self, rate, configure):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, rate, configure)


def activate():
    app = QApplication(sys.argv)
    screen = app.screens()[1]
    dpi = screen.devicePixelRatio() - 0.35
    # dpi = 1
    # print((dpi))
    ui_conf = get_frontend_conf()
    window = MainWindow(dpi, ui_conf)
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    activate()
