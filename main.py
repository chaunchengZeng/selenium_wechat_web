# coding: utf-8
import unittest
import os
from report import HTMLTestRunner

# 加载所以用例
case_path = os.path.dirname(__file__) + '/test_case'
files = 'test*.py'
discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                               pattern=files)

# 执行用例
report_path = os.path.dirname(__file__) + '/report/report.html'
with open(report_path, 'wb') as fp:
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'企业微信web测试报告',
                                           description=u'首页测试',
                                           retry=0)
    runner.run(discover)
