import os
import unittest
import file_handling

from datetime import date


# Instantiating File Hnadling class object
fh = file_handling.file_handling()


class file_handling_tests(unittest.TestCase):

    "This method is a test case for setting points to your goal."

    def test_setPointsGoal(self):

        goal = 10
        fh.setPointsGoal(goal)
        with open("points.txt", "r") as f:
            actual = f.read()

        expected = str(10)

        self.assertEqual(actual, expected)

    "This method is a test case for testing the date."

    def test_setDate(self):

        daysToComplete = 30
        fh.setDate(daysToComplete)

        with open("points.txt", "r") as f:

            # Reading last two lines of the file
            actual = ''.join(f.readlines()[-2:])
            f.seek(0)

            pop = str(date.today())
            temp = pop[pop.rindex('-') + 1]

            if str(temp) == "0":
                currentDate = pop[pop.rindex('-') + 2]

            else:
                currentDate = pop[pop.rindex(
                    '-') + 1] + pop[pop.rindex('-') + 2]

            expected = f'{currentDate}\n{int(currentDate) + daysToComplete}'

        self.assertEqual(actual, expected)

    "This method tests if how many days you have left."

    def test_getRemainingPoints(self):

        with open('points.txt', 'r') as f:

            # Reading the first line of the file
            expected_points = f.readline()

        actual_points = fh.getRemainingPoints()

        self.assertCountEqual(actual_points, expected_points)

    "This method is used when points to deduct the current_points."

    def test_emptyFile(self):

        fh.emptyFile()
        actual_size = os.stat('points.txt').st_size
        expected_size = 0
        self.assertEqual(actual_size, expected_size)

    "This method is used to check if the file is empty or not."

    def test_isFileEmpty(self):

        # Test for when file is empty
        with open('points.txt', 'w') as f:
            f.write('')

        self.assertTrue(fh.isFileEmpty())

        # Test for when file is not empty
        with open('points.txt', 'w') as f:
            f.write('10\n10\n40')

        self.assertFalse(fh.isFileEmpty())

        fh.emptyFile()


if __name__ == '__main__':

    tester = file_handling_tests()

    try:
        tester.test_setPointsGoal()
        tester.test_setDate()
        # tester.test_getRemainingDays()
        tester.test_getRemainingPoints()
        # tester.test_deductPoints()
        tester.test_emptyFile()
        tester.test_isFileEmpty()

        print("ALL TESTS PASSED!")

    except AssertionError:
        print("ONE OR MORE TESTS FAILED!")

    unittest.main()
