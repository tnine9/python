'''
    扫描两条用例，
    运行用例，
    生成测试报告
'''
from HTMLTestRunner import HTMLTestRunner
import unittest

# 1.扫描所有用例
tests = unittest.defaultTestLoader.discover(r"D:\测试开发\python\作业\21.11.29 FourteenthWord", pattern="Test*.py")  # 扫描这个路径下所有test开头的文件

# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器测试报告",
    description="加法运算",
    verbosity=2,
    stream=open(file="计算器.html", mode="w+", encoding="utf-8")
)

# 3.运行
runner.run(tests)
