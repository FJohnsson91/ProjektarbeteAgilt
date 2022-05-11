from mmap import ALLOCATIONGRANULARITY
import os
import unittest
import file_handling

# Instantiating File Hnadling class object
fh = file_handling.file_handling()


class file_handling_tests(unittest.TestCase):

    def test_setPointsGoal(self):

        goal = 10
        fh.setPointsGoal(goal)
        with open("points.txt", "r") as f:
            actual = f.read()

        expected = str(10)

        self.assertEqual(actual, expected)

    def test_setDate(self):

        daysToComplete = 30
        fh.setDate(daysToComplete)

        with open("points.txt", "r") as f:

            # Reading last two lines of the file
            actual = ''.join(f.readlines()[-2:])
            f.seek(0)

            first_line = f.readlines()[0]
            expected = f'{first_line}{int(first_line) + daysToComplete}'

        self.assertEqual(actual, expected)

    def test_getRemainingDays(self):

        with open('points.txt', 'r') as f:
            current_date = int(f.readlines()[1])
            f.seek(0)
            end_date = int(f.readlines()[2])

        expected = str(end_date-current_date)
        actual = fh.getRemainingDays()

        self.assertEqual(actual, expected)

    def test_getRemainingPoints(self):

        with open('points.txt', 'r') as f:

            # Reading the first line of the file
            expected_points = f.readline()

        actual_points = fh.getRemainingPoints()

        self.assertCountEqual(actual_points, expected_points)

    def test_emptyFile(self):

        fh.emptyFile()
        actual_size = os.stat('points.txt').st_size
        expected_size = 0
        self.assertEqual(actual_size, expected_size)

    def test_isFileEmpty(self):

        # Test for when file is empty
        with open('points.txt', 'w') as f:
            f.write('')

        self.assertTrue(fh.isFileEmpty())

        # Test for when file is not empty
        with open('points.txt', 'w') as f:
            f.write('10\n10\n40')

        self.assertFalse(fh.isFileEmpty())


if __name__ == '__main__':

    tester = file_handling_tests()

    try:
        tester.test_setPointsGoal()
        tester.test_setDate()
        tester.test_getRemainingDays()
        tester.test_getRemainingPoints
        tester.test_emptyFile()
        tester.test_isFileEmpty()

        print("ALL TESTS PASSED!")

    except AssertionError:
        print("ONE OR MORE TESTS FAILED!")
    
    unittest.main()
