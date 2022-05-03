import os


class file_handling:
    def __init__(self):
        return None

    def setPointsGoal(self, goal):
        '''Writes the points goal to the file.
           Takes the parameter goal:int'''
        f = open("points.txt", "w")
        f.write(str(goal))
        f.close()
        f = open("points.txt", "r")
        print(f.read())

    def getRemainingPoints(self):
        f = open("points.txt", "r")
        return f.readline()
        f.close()

    def isFileEmpty(self):
        fileSize = os.path.getsize("points.txt")
        if fileSize == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    main()
