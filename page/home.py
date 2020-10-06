# coding: utf-8
# author: zcc
import sys
from time import sleep
from selenium import webdriver
from base.base import Base
from page.login import Login
from page.register import Register


class Home(Base):

    # 写成私有，不对外暴露
    _loc_login = ('css selector', '.index_top_operation_loginBtn')
    _loc_download = ('css selector', '.index_top_operation_registerBtn')
    _loc_register = ('css selector', '.index_head_info_pCDownloadBtn')

    def __init__(self, w_driver: webdriver):
        super().__init__(w_driver)

    def login(self):
        self.click(self._loc_login)
        # 根据PageObject原则，返回跳转后的PageObject
        return Login(self.driver)

    def register(self):
        self.click(self._loc_register)
        return Register(self.driver)
