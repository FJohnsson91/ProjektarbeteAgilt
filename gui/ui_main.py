# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ui_helptext import Ui_HelpText
from ui_aktivitet import Ui_Aktivitet

class Ui_Main(object):

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
    
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1086, 735)
        Main.setStyleSheet("background-color: rgb(37, 37, 37);\n"
"background-color: rgb(37,37,37);")
        self.widget = QtWidgets.QWidget(Main)
        self.widget.setGeometry(QtCore.QRect(0, 0, 201, 731))
        self.widget.setStyleSheet("\n"
"background-color: rgb(37,37,37);")
        self.widget.setObjectName("widget")
        self.remainingpointsbutton = QtWidgets.QPushButton(self.widget)
        self.remainingpointsbutton.setGeometry(QtCore.QRect(30, 660, 141, 61))
        self.remainingpointsbutton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.remainingpointsbutton.setObjectName("remainingpointsbutton")
        self.activitybutton = QtWidgets.QPushButton(self.widget)
        self.activitybutton.setGeometry(QtCore.QRect(30, 520, 141, 61))
        self.activitybutton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.activitybutton.setObjectName("activitybutton")
        self.activitybutton.clicked.connect(self.open_aktivitetwindow)
        self.infobutton = QtWidgets.QPushButton(self.widget)
        self.infobutton.setGeometry(QtCore.QRect(30, 590, 141, 61))
        self.infobutton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.infobutton.setObjectName("infobutton")
        self.infobutton.clicked.connect(self.open_helpwindow)
        self.label = QtWidgets.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(220, 30, 521, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(0)
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
        font.setPointSize(0)
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
        self.easygoal.setObjectName("easygoal")
        self.mediumgoal = QtWidgets.QPushButton(Main)
        self.mediumgoal.setGeometry(QtCore.QRect(220, 290, 131, 41))
        self.mediumgoal.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.mediumgoal.setObjectName("mediumgoal")
        self.hardgoal = QtWidgets.QPushButton(Main)
        self.hardgoal.setGeometry(QtCore.QRect(220, 360, 131, 41))
        self.hardgoal.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.hardgoal.setObjectName("hardgoal")
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
        self.showpoints = QtWidgets.QTextEdit(Main)
        self.showpoints.setGeometry(QtCore.QRect(890, 470, 71, 31))
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
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
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
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
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
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.showpoints.setPalette(palette)
        self.showpoints.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.showpoints.setObjectName("showpoints")
        self.label_7 = QtWidgets.QLabel(Main)
        self.label_7.setGeometry(QtCore.QRect(680, 470, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font-size: 12px;\n"
"color: rgb(255, 222, 222);\n"
"color: rgb(0, 170, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Main)
        self.label_8.setGeometry(QtCore.QRect(970, 470, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(0)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font-size: 12px;\n"
"color: rgb(255, 222, 222);\n"
"color: rgb(0, 170, 255);")
        self.label_8.setObjectName("label_8")
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
        self.savedays = QtWidgets.QPushButton(Main)
        self.savedays.setGeometry(QtCore.QRect(360, 540, 131, 31))
        self.savedays.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.savedays.setObjectName("savedays")
        self.personaldays = QtWidgets.QLineEdit(Main)
        self.personaldays.setGeometry(QtCore.QRect(220, 540, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
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
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
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
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
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
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
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
        self.showdays = QtWidgets.QTextEdit(Main)
        self.showdays.setGeometry(QtCore.QRect(890, 520, 71, 31))
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
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
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
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
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
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.showdays.setPalette(palette)
        self.showdays.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.showdays.setObjectName("showdays")
        self.label_10 = QtWidgets.QLabel(Main)
        self.label_10.setGeometry(QtCore.QRect(840, 520, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font-size: 12px;\n"
"color: rgb(255, 222, 222);\n"
"color: rgb(0, 170, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Main)
        self.label_11.setGeometry(QtCore.QRect(970, 520, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(0)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font-size: 12px;\n"
"color: rgb(255, 222, 222);\n"
"color: rgb(0, 170, 255);")
        self.label_11.setObjectName("label_11")
        self.personalpoints = QtWidgets.QLineEdit(Main)
        self.personalpoints.setGeometry(QtCore.QRect(220, 470, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
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
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
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
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
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
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
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
        self.saveactivity.setGeometry(QtCore.QRect(360, 470, 131, 31))
        self.saveactivity.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.saveactivity.setObjectName("saveactivity")

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Dialog"))
        self.remainingpointsbutton.setText(_translate("Main", "Vad har jag kvar?"))
        self.activitybutton.setText(_translate("Main", "Aktiviteter"))
        self.infobutton.setText(_translate("Main", "Information"))
        self.label.setText(_translate("Main", "Välj svårighetsgrad på ditt hälso-mål"))
        self.label_2.setText(_translate("Main", "Antingen kan du välja ett lätt, medel, eller ett svårt mål för dig själv"))
        self.label_3.setText(_translate("Main", "Eller en personlig målsättning, välj poäng här under"))
        self.easygoal.setText(_translate("Main", "Lätt mål"))
        self.mediumgoal.setText(_translate("Main", "Medel-svårt mål"))
        self.hardgoal.setText(_translate("Main", "Svårt mål"))
        self.label_4.setText(_translate("Main", "Med lätt mål ska du samla in XXX poäng under 7 dagar"))
        self.label_5.setText(_translate("Main", "Med medel-svårt mål ska du samla in XXX poäng under 5 dagar"))
        self.label_6.setText(_translate("Main", "Med svårt mål ska du samla in XXX poäng 5 dagar"))
        self.label_7.setText(_translate("Main", "Du har valt ett mål där du ska samla in"))
        self.label_8.setText(_translate("Main", "poäng"))
        self.label_9.setText(_translate("Main", "Under hur många dagar "))
        self.savedays.setText(_translate("Main", "Lägg till"))
        self.label_10.setText(_translate("Main", "under"))
        self.label_11.setText(_translate("Main", "dagar"))
        self.saveactivity.setText(_translate("Main", "Lägg till"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())