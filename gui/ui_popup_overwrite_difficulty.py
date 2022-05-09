
from PyQt5 import QtCore, QtGui, QtWidgets
from file_handling import file_handling


class Ui_popup_overwrite_difficulty(object):

    def __init__(self, text, btn):
        self.text = text
        self.btn = btn

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()

    def overWrite(self):
        fh = file_handling()
        if self.btn == "easy":
            fh.emptyFile()
            fh.setPointsGoal(10)
            fh.setDate(7)
        if self.btn == "medium":
            fh.emptyFile()
            fh.setPointsGoal(15)
            fh.setDate(5)
        if self.btn == "hard":
            fh.emptyFile()
            fh.setPointsGoal(20)
            fh.setDate(5)

    def setupUi(self, popup):
        popup.setObjectName("popup")
        popup.resize(285, 165)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        popup.setFont(font)
        popup.setAutoFillBackground(False)
        popup.setStyleSheet("background-color: rgb(37, 37, 37);\n"
                            "background-color: rgb(37,37,37);\n"
                            "\n"
                            "")
        self.yesBtn = QtWidgets.QPushButton(popup)
        self.yesBtn.clicked.connect(lambda: self.toggle_window(popup))
        self.yesBtn.setGeometry(QtCore.QRect(210, 120, 61, 31))
        self.yesBtn.setFont(font)
        self.yesBtn.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.yesBtn.setObjectName("infobutton")
        self.yesBtn = QtWidgets.QPushButton(popup)
        self.yesBtn.clicked.connect(
            lambda: self.toggle_window(popup))
        self.yesBtn.clicked.connect(
            lambda: self.overWrite())
        self.yesBtn.setGeometry(QtCore.QRect(210, 120, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.yesBtn.setFont(font)
        self.yesBtn.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.yesBtn.setObjectName("infobutton")
        # 2ND BTN
        self.noBtn = QtWidgets.QPushButton(popup)
        self.noBtn.clicked.connect(lambda: self.toggle_window(popup))
        self.noBtn.setGeometry(QtCore.QRect(150, 120, 61, 31))
        self.noBtn.setFont(font)
        self.noBtn.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.noBtn.setObjectName("noBtn")
        self.noBtn = QtWidgets.QPushButton(popup)
        self.noBtn.clicked.connect(lambda: self.toggle_window(popup))
        self.noBtn.setGeometry(QtCore.QRect(150, 120, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.noBtn.setFont(font)
        self.noBtn.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.noBtn.setObjectName("infobutton")
        # END
        self.label_3 = QtWidgets.QLabel(popup)
        self.label_3.setGeometry(QtCore.QRect(40, 50, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-size: 12px;\n"
                                   "font: 10pt \"Segoe UI\";\n"
                                   "color: rgb(255, 222, 222);\n"
                                   "color: rgb(0, 170, 255);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(popup)
        QtCore.QMetaObject.connectSlotsByName(popup)

    def retranslateUi(self, popup):
        _translate = QtCore.QCoreApplication.translate
        popup.setWindowTitle(_translate("popup", "Health-Goal"))
        self.yesBtn.setText(_translate("popup", "Yes"))
        self.noBtn.setText(_translate("popup", "No"))
        self.label_3.setText(self.text)
