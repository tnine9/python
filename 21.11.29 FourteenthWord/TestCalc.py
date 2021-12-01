'''
    1.用例的数据太多
    2.结果不方便观察
    3.测试报告
    unittest
    1.子类继承TestCase
    2.testXXXX

'''

from unittest import TestCase
from Calc import Calc


class TestCalc(TestCase):

    def testAdd1(self):
        a = 6
        b = 5
        c = 11

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd2(self):
        a = -6
        b = 5
        c = -1

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd3(self):
        a = 5
        b = -5
        c = 1

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd4(self):
        a = -5
        b = -5
        c = -10

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd5(self):
        a = 5000000000000000000000000000000000000000000000000000000
        b = 6
        c = 5000000000000000000000000000000000000000000000000000006

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd6(self):
        a = 0
        b = 6
        c = 6

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd7(self):
        a = -0
        b = 6
        c = 6

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd8(self):
        a = -0
        b = -6
        c = -6

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd9(self):
        a = -5000000000000000000000000000000000000000000000000000000
        b = 6
        c = 5000000000000000000000000000000000000000000000000000006

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd10(self):
        a = '2'
        b = 6
        c = 8

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)
