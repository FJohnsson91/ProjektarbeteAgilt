import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from datetime import date
from ui_popup_selected_difficulty import Ui_popup_selected_difficulty


class file_handling:
    def __init__(self):
        return None

    def main():
        return None

    def setPointsGoal(self, goal):
        '''Writes the points goal to the file.
           Takes the parameter goal:int'''
        f = open("points.txt", "w")
        f.write(str(goal))
        f.close()

    def setDate(self, daysToComplete):
        currentDate = str(date.today())
        temp = currentDate[currentDate.rindex('-') + 1]
        if str(temp) == "0":
            currentDate = currentDate[currentDate.rindex('-') + 2]
            endDate = int(currentDate) + daysToComplete
        else:
            temp1 = currentDate[currentDate.rindex('-') + 1]
            temp2 = currentDate[currentDate.rindex('-') + 2]
            currentDate = temp1 + temp2
            str(currentDate)
            endDate = int(currentDate) + daysToComplete

        f = open("points.txt", "a")
        f.write("\n" + str(currentDate))
        f.write("\n" + str(endDate))
        f.close()

    def updateDate(self):
        if self.isFileEmpty():
            return None
        else:
            f = open("points.txt", "r")
            lines = f.readlines()
            endDate = lines[2]
            f.close()

            currentDate = str(date.today())
            temp = currentDate[currentDate.rindex('-') + 1]
            if str(temp) == "0":
                currentDate = currentDate[currentDate.rindex('-') + 2]
            else:
                temp1 = currentDate[currentDate.rindex('-') + 1]
                temp2 = currentDate[currentDate.rindex('-') + 2]
                currentDate = temp1 + temp2
                str(currentDate)

            if currentDate >= endDate:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_popup_selected_difficulty(
                    "You have reached the\nend of your goal")
                self.ui.setupUi(self.window)
                self.window.show()
                self.emptyFile()

    def getRemainingDays(self):
        f = open("points.txt", "r")
        lines = f.readlines()
        currentDate = lines[1]
        endDate = lines[2]
        remainingDays = int(endDate) - int((currentDate))
        return str(remainingDays)

    def getRemainingPoints(self):
        f = open("points.txt", "r")
        return f.readline()
        f.close()

    def deductPoints(self, pointsToDeduct):
        with open("points.txt") as f:
            lines = f.readlines()
            points = int(self.getRemainingPoints())
            points = points - pointsToDeduct
            lines

            lines[0] = "" + str(points) + "\n"
            lines
        with open("points.txt", "w") as f:
            f.writelines(lines)
        if points <= 0:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_popup_selected_difficulty(
                "Goal complete! \nSet a new goal from previous page")
            self.ui.setupUi(self.window)
            self.window.show()
            # msg = QMessageBox()
            # msg.setWindowTitle("Goal reached")
            # msg.setText(
            #     "You have reached your goal \n You can set up a new goal from the main page")
            # x = msg.exec_()
            self.emptyFile()

    def emptyFile(self):
        with open("points.txt", 'r+') as f:
            f.truncate(0)

    def isFileEmpty(self):
        fileSize = os.path.getsize("points.txt")
        if fileSize == 0:
            return True
        else:
            return False

    if __name__ == "__main__":
        main()
