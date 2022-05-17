import sys
import platform
from tkinter import Widget
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                          QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                         QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

from ui_main import Ui_Main
from ui_splash import Ui_SplashScreen
from ui_aktivitet import Ui_Aktivitet
from ui_helptext import Ui_HelpText
from ui_popup import Ui_popup
from file_handling import file_handling

counter = 0


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Main()
        self.ui.setupUi(self)


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()
        counter += 1


class Helptext_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_HelpText()
        self.ui.setupUi(self)


class Popup_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_popup()
        self.ui.setupUi(self)


class activity_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Aktivitet()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    splashwindow = SplashScreen()
    fh = file_handling()
    fh.updateDate()
    sys.exit(app.exec_())
