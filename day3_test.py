import unittest
import day3


class TestDayThree(unittest.TestCase):

    def test1(self):
        text = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
        lines = text.splitlines()
        num, part2 = day3.gears(lines)
        self.assertEqual(4361, num)
        self.assertEqual(467835, part2)

    def test2(self):
        text = '''.....
..290
.....'''
        lines = text.splitlines()
        num, part2 = day3.gears(lines)
        self.assertEqual(0, num)




