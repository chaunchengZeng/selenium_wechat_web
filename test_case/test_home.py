# coding: utf-8
from selenium import webdriver
import unittest
from page.home import Home


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.wd = webdriver.Chrome(r'E:\package\chromedriver')

    def setUp(self):
        self.wd.get('https://work.weixin.qq.com/')
        self.wd.maximize_window()
        self.home = Home(self.wd)

    def tearDown(self):
        self.wd.delete_all_cookies()
        self.wd.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.wd.quit()

    def test_login(self):
        # 根据PO原则，用例只保留基本步骤。
        wd = self.home.login()
        text = wd.get_title()
        self.assertEqual("企业登录", text)

    def test_register(self):
        wd = self.home.register()
        text = wd.get_title()
        self.assertEqual("注册企业微信", text)
