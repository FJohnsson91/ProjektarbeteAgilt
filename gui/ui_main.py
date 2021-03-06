from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from ui_popup import Ui_popup
from ui_helptext import Ui_HelpText
from ui_aktivitet import Ui_Aktivitet
from file_handling import file_handling
from ui_popup_message import Ui_popup_message
from ui_popup_overwrite_difficulty import Ui_popup_overwrite_difficulty


class Ui_Main(object):

    def show_remainingpoints(self):
        fh = file_handling()
        if fh.isFileEmpty():
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_popup_message(
                "You need to set a goal before you \ncan view your progress")
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_popup()
            self.ui.setupUi(self.window)
            self.window.show()

    def open_helpwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HelpText()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_aktivitetwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Aktivitet()
        self.ui.setupUi(self.window)
        self.window.show()

    def mediumGoal(self):
        fh = file_handling()
        if fh.isFileEmpty():
            fh.setPointsGoal(15)
            fh.setDate(5)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_popup_message(
                "You chose medium difficulty\nCollect: 15 in 5 days")
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_popup_overwrite_difficulty(
                "Overwrite your previous goal?\nYour progess will be lost", "medium")
            self.ui.setupUi(self.window)
            self.window.show()

    def hardGoal(self):
        fh = file_handling()
        if fh.isFileEmpty():
            fh.setPointsGoal(20)
            fh.setDate(5)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_popup_message(
                "You chose hard difficulty\nCollect: 20 in 5 days")
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_popup_overwrite_difficulty(
                "Overwrite your previous goal?\nYour progess will be lost", "hard")
            self.ui.setupUi(self.window)
            self.window.show()

    def easyGoal(self):
        fh = file_handling()
        if fh.isFileEmpty():
            fh.setPointsGoal(10)
            fh.setDate(7)

            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_popup_message(
                "You chose easy difficulty\nCollect: 10 in 7 days")
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_popup_overwrite_difficulty(
                "Overwrite your previous goal?\nYour progess will be lost", "easy")
            self.ui.setupUi(self.window)
            self.window.show()

    def setPersonalGoal(self):
        fh = file_handling()
        daysInput = self.personaldays.text()
        pointsInput = self.personalpoints.text()
        if fh.isFileEmpty():
            if daysInput.isnumeric():
                fh.setPointsGoal(int(pointsInput))
                fh.setDate(int(daysInput))

            else:
                print("Not a number")
        else:
            if daysInput.isnumeric():
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_popup_overwrite_difficulty(
                    "Overwrite your previous goal?\nYour progess will be lost", "personal", int(pointsInput), int(daysInput))
                self.ui.setupUi(self.window)
                self.window.show()
            else:
                return None

    def setupUi(self, Main):
        Main.setFixedSize(1086, 735)
        Main.setObjectName("Main")
        Main.resize(1086, 735)
        Main.setStyleSheet("background-color: rgb(37, 37, 37);\n"
                           "background-color: rgb(37,37,37);")
        self.widget = QtWidgets.QWidget(Main)
        self.widget.setGeometry(QtCore.QRect(880, 0, 201, 731))
        self.widget.setStyleSheet("\n"
                                  "background-color: rgb(37,37,37);")
        self.widget.setObjectName("widget")
        self.remainingpointsbutton = QtWidgets.QPushButton(self.widget)
        self.remainingpointsbutton.setGeometry(QtCore.QRect(30, 660, 141, 61))
        self.remainingpointsbutton.setStyleSheet(
            "background-color: rgb(0, 170, 255);")
        self.remainingpointsbutton.setObjectName("remainingpointsbutton")
        self.remainingpointsbutton.clicked.connect(self.show_remainingpoints)
        self.activitybutton = QtWidgets.QPushButton(self.widget)
        self.activitybutton.setGeometry(QtCore.QRect(30, 520, 141, 61))
        self.activitybutton.setStyleSheet(
            "background-color: rgb(0, 170, 255);")
        self.activitybutton.setObjectName("activitybutton")
        self.activitybutton.clicked.connect(self.open_aktivitetwindow)
        self.infobutton = QtWidgets.QPushButton(self.widget)
        self.infobutton.setGeometry(QtCore.QRect(30, 590, 141, 61))
        self.infobutton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.infobutton.setObjectName("infobutton")
        self.infobutton.clicked.connect(self.open_helpwindow)
        self.label = QtWidgets.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(220, 30, 701, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 30px;\n"
                                 "font: bold;\n"
                                 "color: rgb(255, 222, 222);\n"
                                 "color: rgb(0, 170, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Main)
        self.label_2.setGeometry(QtCore.QRect(220, 140, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-size: 15px;\n"
                                   "color: rgb(255, 222, 222);\n"
                                   "color: rgb(0, 170, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Main)
        self.label_3.setGeometry(QtCore.QRect(220, 430, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-size: 12px;\n"
                                   "font: 8pt \"Segoe UI\";\n"
                                   "color: rgb(255, 222, 222);\n"
                                   "color: rgb(0, 170, 255);")
        self.label_3.setObjectName("label_3")
        self.easygoal = QtWidgets.QPushButton(Main)
        self.easygoal.setGeometry(QtCore.QRect(220, 220, 131, 41))
        self.easygoal.setStyleSheet("background-color: rgb(0, 170, 255);")
        # Easy goal button
        self.easygoal.setObjectName("easygoal")
        self.easygoal.clicked.connect(lambda: self.easyGoal())
        self.mediumgoal = QtWidgets.QPushButton(Main)
        self.mediumgoal.setGeometry(QtCore.QRect(220, 290, 131, 41))
        self.mediumgoal.setStyleSheet("background-color: rgb(0, 170, 255);")
        # Medium goal button
        self.mediumgoal.setObjectName("mediumgoal")
        self.mediumgoal.clicked.connect(lambda: self.mediumGoal())
        self.hardgoal = QtWidgets.QPushButton(Main)
        self.hardgoal.setGeometry(QtCore.QRect(220, 360, 131, 41))
        self.hardgoal.setStyleSheet("background-color: rgb(0, 170, 255);")
        # Hard goal button
        self.hardgoal.setObjectName("hardgoal")
        self.hardgoal.clicked.connect(lambda: self.hardGoal())
        self.label_4 = QtWidgets.QLabel(Main)
        self.label_4.setGeometry(QtCore.QRect(370, 220, 291, 31))

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font-size: 12px;\n"
                                   "font: 8pt \"Segoe UI\";\n"
                                   "color: rgb(255, 222, 222);\n"
                                   "color: rgb(0, 170, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Main)
        self.label_5.setGeometry(QtCore.QRect(370, 290, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font-size: 12px;\n"
                                   "font: 8pt \"Segoe UI\";\n"
                                   "color: rgb(255, 222, 222);\n"
                                   "color: rgb(0, 170, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Main)
        self.label_6.setGeometry(QtCore.QRect(370, 360, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font-size: 12px;\n"
                                   "font: 8pt \"Segoe UI\";\n"
                                   "color: rgb(255, 222, 222);\n"
                                   "color: rgb(0, 170, 255);")
        self.label_6.setObjectName("label_6")

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)

        self.label_9 = QtWidgets.QLabel(Main)
        self.label_9.setGeometry(QtCore.QRect(220, 510, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font-size: 14px;\n"
                                   "font: 10pt \"Segoe UI\";\n"
                                   "color: rgb(255, 222, 222);\n"
                                   "color: rgb(0, 170, 255);")
        self.label_9.setObjectName("label_9")

        self.personaldays = QtWidgets.QLineEdit(Main)
        self.personaldays.setGeometry(QtCore.QRect(220, 540, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        self.personaldays.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.personaldays.setFont(font)
        self.personaldays.setAutoFillBackground(False)
        self.personaldays.setStyleSheet("font: 14pt \"Segoe UI\";\n"
                                        "background-color: rgb(37, 37, 37);")
        self.personaldays.setObjectName("personaldays")

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)

        self.label_10 = QtWidgets.QLabel(Main)
        self.label_10.setGeometry(QtCore.QRect(770, 520, 90, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font-size: 12px;\n"
                                    "color: rgb(255, 222, 222);\n"
                                    "color: rgb(0, 170, 255);")
        self.label_10.setObjectName("label_10")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)

        self.personalpoints = QtWidgets.QLineEdit(Main)
        self.personalpoints.setGeometry(QtCore.QRect(220, 470, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        self.personalpoints.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.personalpoints.setFont(font)
        self.personalpoints.setAutoFillBackground(False)
        self.personalpoints.setStyleSheet("font: 14pt \"Segoe UI\";\n"
                                          "background-color: rgb(37, 37, 37);")
        self.personalpoints.setObjectName("personalpoints")
        self.saveactivity = QtWidgets.QPushButton(Main)
        self.saveactivity.setGeometry(QtCore.QRect(220, 590, 131, 31))
        self.saveactivity.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.saveactivity.setObjectName("saveactivity")
        self.saveactivity.clicked.connect(lambda: self.setPersonalGoal())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Health-Goal"))
        self.remainingpointsbutton.setText(
            _translate("Main", "Remaining points/days"))

        self.activitybutton.setText(_translate("Main", "Activities"))
        self.infobutton.setText(_translate("Main", "Information"))
        self.label.setText(_translate(
            "Main", "Select a difficulty for your Health-Goal"))
        self.label_2.setText(_translate(
            "Main", "Choose between easy, medium, hard, or set your own goal"))
        self.label_3.setText(_translate(
            "Main", "Personal goal | Points"))
        self.easygoal.setText(_translate("Main", "Easy"))
        self.mediumgoal.setText(_translate("Main", "Medium"))
        self.hardgoal.setText(_translate("Main", "Hard"))
        self.label_4.setText(_translate(
            "Main", "Earn 10 points over 7 days"))
        self.label_5.setText(_translate(
            "Main", "Earn 15 points over 5 days"))
        self.label_6.setText(_translate(
            "Main", "Earn 20 points over 5 days"))

        #self.label_8.setText(_translate("Main", "po??ng"))
        self.label_9.setText(_translate("Main", "Personal goal | Days"))

        self.saveactivity.setText(_translate("Main", "Add"))
