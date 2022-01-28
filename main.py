import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from GUI.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, rate):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, rate)


def activate():
    app = QApplication(sys.argv)
    screen = app.screens()[1]
    dpi = screen.devicePixelRatio()-0.35
    #dpi = 1
    #print((dpi))
    window = MainWindow(dpi)
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    activate()
