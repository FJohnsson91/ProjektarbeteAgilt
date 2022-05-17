import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from datetime import date


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
        #startDate = str(date.today())
        #startDate = startDate[startDate.rindex('-') + 2]
        #endDate = str(date.today())
        #endDate = endDate[endDate.rindex('-') + 2]
        #endDate = int(endDate) + daysToComplete

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

            if currentDate == endDate:
                msg = QMessageBox()
                msg.setWindowTitle("Finish")
                msg.setText(
                    "You have reached the end of the goal \n You can set up a new goal from the previous page")
                x = msg.exec_()
                self.emptyFile()

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
            msg = QMessageBox()
            msg.setWindowTitle("Goal reached")
            msg.setText(
                "You have reached your goal \n You can set up a new goal from the main page")
            x = msg.exec_()
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
