import unittest
import day1


class TestDayOne(unittest.TestCase):

    def test1(self):
        text = '''1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet'''
        lines = text.splitlines()
        self.assertEqual(day1.calibrate(lines), 142)

    def test2(self):
        text = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''
        lines = text.splitlines()
        self.assertEqual(day1.calibrate(lines), 281)


if __name__ == '__main__':
    unittest.main()