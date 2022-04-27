# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Aktivitet.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import mysql.connector


class Ui_Aktivitet(object):

    def setupUi(self, Aktivitet):
        Aktivitet.setObjectName("Aktivitet")
        Aktivitet.resize(1109, 730)
        Aktivitet.setStyleSheet("background-color: rgb(37, 37, 37);\n"
                                "background-color: rgb(37,37,37);")
        self.widget = QtWidgets.QWidget(Aktivitet)
        self.widget.setGeometry(QtCore.QRect(0, 0, 201, 721))
        self.widget.setStyleSheet("\n"
                                  "background-color: rgb(37,37,37);")
        self.widget.setObjectName("widget")
        self.TillbakaAktivitet = QtWidgets.QPushButton(self.widget)
        self.TillbakaAktivitet.setGeometry(QtCore.QRect(30, 650, 141, 61))
        self.TillbakaAktivitet.setStyleSheet(
            "background-color: rgb(0, 170, 255);")
        self.TillbakaAktivitet.setObjectName("TillbakaAktivitet")

        # valda aktiviteter
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(50, 20, 121, 141))
        self.textEdit.setTextColor(QtGui.QColor(0, 170, 255))
        self.textEdit.setObjectName("textEdit")
        self.SparaAktivitet = QtWidgets.QPushButton(self.widget)
        self.SparaAktivitet.setGeometry(QtCore.QRect(50, 230, 111, 41))
        self.SparaAktivitet.setStyleSheet(
            "background-color: rgb(0, 170, 255);")
        self.SparaAktivitet.setObjectName("SparaAktivitet")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        self.label_3.setPalette(palette)
        self.label_3.setStyleSheet("font: 12pt \"Segoe UI\";\n"
                                   "color: rgb(0, 170, 255)")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Aktivitet)
        self.label.setGeometry(QtCore.QRect(350, 10, 481, 61))
        self.label.setStyleSheet("font-size: 30px;\n"
                                 "font: bold;\n"
                                 "color: rgb(255, 222, 222);\n"
                                 "color: rgb(0, 170, 255);")
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Aktivitet)
        self.tableWidget.setGeometry(QtCore.QRect(210, 200, 821, 421))
        palette = QtGui.QPalette()
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
        self.tableWidget.setPalette(palette)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet("QHeaderView::section { color:rgb(0, 170, 255); background-color:rgb(37, 37, 37)}")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(197)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.label_2 = QtWidgets.QLabel(Aktivitet)
        self.label_2.setGeometry(QtCore.QRect(210, 660, 641, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-size: 15px;\n"
                                   "color: rgb(255, 222, 222);\n"
                                   "color: rgb(0, 170, 255);")
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(Aktivitet)
        self.layoutWidget.setGeometry(QtCore.QRect(212, 630, 191, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SaveAktivitet = QtWidgets.QPushButton(self.layoutWidget)
        self.SaveAktivitet.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.SaveAktivitet.setObjectName("SaveAktivitet")

        # On lägg till button press
        self.SaveAktivitet.clicked.connect(
            lambda: self.addChoice())

        self.horizontalLayout.addWidget(self.SaveAktivitet)

        # Input box
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
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
        self.lineEdit.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("font: 9pt \"Segoe UI\";\n"
                                    "background-color: rgb(37, 37, 37);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.visafysik = QtWidgets.QPushButton(Aktivitet)
        self.visafysik.setGeometry(QtCore.QRect(330, 150, 111, 41))
        self.visafysik.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.visafysik.setObjectName("visafysik")
        # Display physical activities
        self.visafysik.clicked.connect(
            lambda: self.displayPhysicalActivities())
        self.visamental = QtWidgets.QPushButton(Aktivitet)
        self.visamental.setGeometry(QtCore.QRect(690, 150, 111, 41))
        self.visamental.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.visamental.setObjectName("visamental")
        # Display mental activities
        self.visamental.clicked.connect(lambda: self.displayMentalActivities())
        self.label_4 = QtWidgets.QLabel(Aktivitet)
        self.label_4.setGeometry(QtCore.QRect(440, 100, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font-size: 15px;\n"
                                   "color: rgb(255, 222, 222);\n"
                                   "color: rgb(0, 170, 255);")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Aktivitet)
        QtCore.QMetaObject.connectSlotsByName(Aktivitet)

    def retranslateUi(self, Aktivitet):
        _translate = QtCore.QCoreApplication.translate
        Aktivitet.setWindowTitle(_translate("Aktivitet", "Dialog"))
        self.TillbakaAktivitet.setText(_translate("Aktivitet", "Tillbaka"))
        self.SparaAktivitet.setText(_translate("Aktivitet", "Spara"))
        self.label_3.setText(_translate("Aktivitet", "Valda aktiviteter"))
        self.label_3.setText(_translate("Aktivitet", "Avklarade aktiviteter"))
        self.label.setText(_translate(
            "Aktivitet", "Olika aktiviteter att välja bland"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Aktivitet", "Aktivitet"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Aktivitet", "Längd"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Aktivitet", "Poäng"))
        self.label_2.setText(_translate(
            "Aktivitet", "Välj vilka aktiviteter du vill göra genom att skriva in det nummer som står framför vald aktivitet"))
        self.SaveAktivitet.setText(_translate("Aktivitet", "Lägg till"))
        self.visafysik.setText(_translate("Aktivitet", "Fysiska aktiviteter"))
        self.visamental.setText(_translate("Aktivitet", "Mentala aktiviteter"))
        self.label_4.setText(_translate(
            "Aktivitet", "Välj vilken kategori av aktiviteter nedan"))

    def displayPhysicalActivities(self):
        mydb = mysql.connector.connect(
            host="emilone.eurovoice.net", user="healthgoaluser", password="zUd19HMoLtc61f7L", database="healthgoaldb"
        )
        mycursor = mydb.cursor()
        sql = "SELECT * FROM fysiska"
        mycursor.execute(sql)
        myResult = mycursor.fetchall()
        self.tableWidget.setRowCount(len(myResult))
        rowCount = 0
        for x in myResult:
            self.tableWidget.setItem(
                rowCount, 0, QtWidgets.QTableWidgetItem(x[1]))
            self.tableWidget.setItem(
                rowCount, 1, QtWidgets.QTableWidgetItem(str(x[2])))
            self.tableWidget.setItem(
                rowCount, 2, QtWidgets.QTableWidgetItem(str(x[3])))
            rowCount += 1
        self.physical = True
        self.mental = False

    def displayMentalActivities(self):
        mydb = mysql.connector.connect(
            host="emilone.eurovoice.net", user="healthgoaluser", password="zUd19HMoLtc61f7L", database="healthgoaldb"
        )
        mycursor = mydb.cursor()
        sql = "SELECT * FROM mentala"
        mycursor.execute(sql)
        myResult = mycursor.fetchall()
        self.tableWidget.setRowCount(len(myResult))
        rowCount = 0
        for x in myResult:
            self.tableWidget.setItem(
                rowCount, 0, QtWidgets.QTableWidgetItem(x[1]))
            self.tableWidget.setItem(
                rowCount, 1, QtWidgets.QTableWidgetItem(str(x[2])))
            self.tableWidget.setItem(
                rowCount, 2, QtWidgets.QTableWidgetItem(str(x[3])))
            rowCount += 1
        self.mental = True
        self.physical = False

    def addChoice(self):
        choiceNumber = self.lineEdit.text()
        if self.physical is True:
            # fysiska table
            mydb = mysql.connector.connect(
                host="emilone.eurovoice.net", user="healthgoaluser", password="zUd19HMoLtc61f7L", database="healthgoaldb"
            )
            mycursor = mydb.cursor()
            sql = "SELECT * FROM fysiska"
            mycursor.execute(sql)
            myResult = mycursor.fetchall()

            # Finds the corresponding activty for choiceNumber and adds it to the list
            counter = 0
            for entry in myResult:
                if int(entry[counter]) == int(choiceNumber):
                    self.textEdit.append(
                        entry[1] + " | " + str(entry[2]) + " | " + str(entry[3]) + "P")
            counter += 1
        if self.mental is True:
            # mentala table
            mydb = mysql.connector.connect(
                host="emilone.eurovoice.net", user="healthgoaluser", password="zUd19HMoLtc61f7L", database="healthgoaldb"
            )
            mycursor = mydb.cursor()
            sql = "SELECT * FROM mentala"
            mycursor.execute(sql)
            myResult = mycursor.fetchall()

            # Finds the corresponding activty for choiceNumber and adds it to the list
            counter = 0
            for entry in myResult:
                if int(entry[counter]) == int(choiceNumber):
                    self.textEdit.append(
                        entry[1] + " | " + str(entry[2]) + " | " + str(entry[3]) + "P")
            counter += 1

        # ADD FUNCTIONALITY TO SAVE TO FILE
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Aktivitet = QtWidgets.QDialog()
    ui = Ui_Aktivitet()
    ui.setupUi(Aktivitet)
    Aktivitet.show()
    sys.exit(app.exec_())
