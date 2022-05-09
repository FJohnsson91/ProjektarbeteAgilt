
from PyQt5 import QtCore, QtGui, QtWidgets
from file_handling import file_handling


class Ui_popup_selected_difficulty(object):

    def __init__(self, text):
        self.text = text

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()

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
        self.infobutton = QtWidgets.QPushButton(popup)
        self.infobutton.clicked.connect(lambda: self.toggle_window(popup))
        self.infobutton.setGeometry(QtCore.QRect(210, 120, 61, 31))
        self.infobutton.setFont(font)
        self.infobutton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.infobutton.setObjectName("infobutton")
        self.infobutton = QtWidgets.QPushButton(popup)
        self.infobutton.clicked.connect(lambda: self.toggle_window(popup))
        self.infobutton.setGeometry(QtCore.QRect(210, 120, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.infobutton.setFont(font)
        self.infobutton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.infobutton.setObjectName("infobutton")
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
        self.infobutton.setText(_translate("popup", "OK"))
        self.label_3.setText(self.text)
