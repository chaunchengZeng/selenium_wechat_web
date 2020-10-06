# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base(object):

    def __init__(self, w_driver: webdriver):
        self.driver = w_driver
        self.timeout = 10
        self.t = 0.5

    def find_element_new(self, locator):
        """
        定位到元素返回元素对象，定位不到返回timeout异常
        :param locator: tuple示例("xpath"，"//p")
        :return:
        """
        element = WebDriverWait(self.driver, self.timeout, self.t) \
            .until(EC.presence_of_element_located(locator))
        return element

    def find_element(self, locator):
        """
        查找元素
        :param locator: tuple示例("xpath"，"//p")
        :return: 查找到的元素
        """
        element = WebDriverWait(self.driver, self.timeout, self.t) \
            .until(lambda x: x.find_element(*locator))
        return element

    def find_elements(self, locator):
        elements = WebDriverWait(self.driver, self.timeout, self.t) \
            .until(lambda x: x.find_elements(*locator))
        return elements

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def clear(self, locator):
        element = self.find_element(locator)
        element.clear()

    def is_selected(self, locator):
        element = self.find_element(locator)
        return element.is_selected()

    def is_element_exist(self, locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

    def is_element_exist2(self, locator):
        elements = self.find_elements(locator)
        n = len(elements)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到的元素个数：%s" % n)
            return True

    def is_title(self, title):
        """返回bool值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return result
        except:
            return False

    def is_title_contains(self, title):
        """返回bool值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, title):
        """返回bool值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t) \
                .until(EC.text_to_be_present_in_element(locator, title))
            return result
        except:
            return False

    def is_value_in_element(self, locator, value):
        """返回bool值，value为空字符串返回false"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t) \
                .until(EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    def is_alert(self):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_text(self, locator):
        try:
            t = self.find_element(locator).text
            return t
        except:
            print("获取失败，返回''")
            return ""

    def switch_to_alert(self):
        return self.driver.switch_to_alert()

    def scroll_to_end(self):
        """
        滑动条拉到最后
        :return:
        """
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        self.driver.execute_script(js)

    def scroll_to_top(self):
        """
        滑动条拉到顶部
        :return:
        """
        js = 'window.scrollTo(0, 0)'
        self.driver.execute_script(js)

    def scroll_to_element(self, locator):
        """
        滑动条拉到定位的元素
        :return:
        """
        element = self.driver.find_element(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
