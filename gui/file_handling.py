class file_handling:
    def __init__(self):
        return None

    def setPointsGoal(self, goal):
        '''Writes the points goal to the file.
           Takes the parameter goal:int'''
        f = open("point_file", "a")
        f.write(str(goal))
        f.write("\n")
        f.close()

    def writePointGoal(self, point):
        return None


if __name__ == '__main__':
    main()
