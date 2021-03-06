# coding: utf-8
from selenium import webdriver
from base.base import Base


class Register(Base):

    _loc_title = ('css selector', '.register_simple_header_title')

    def __init__(self, w_driver: webdriver):
        super().__init__(w_driver)

    def get_title(self):
        return self.get_text(self._loc_title)
