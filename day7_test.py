import unittest
import day7


class TestDaySeven(unittest.TestCase):

    def test1(self):
        self.assertEqual(7, day7.rank('*****'))

    def test2(self):
        self.assertEqual(4, day7.rank('123**'))

    def test3(self):
        self.assertEqual(2, day7.rank('TKQ*7'))

    def test4(self):
        self.assertEqual(6, day7.rank('TT*Q*'))

    def test5(self):
        self.assertEqual(5, day7.rank('TT*QQ'))





