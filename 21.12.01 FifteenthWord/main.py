from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="银行系统测试报告",
    description="中国农业银行银行系统转账模块测试1",
    verbosity=1,
    stream=open(file="bank.html", mode="w+", encoding="utf-8")
)

runner.run(tests)
