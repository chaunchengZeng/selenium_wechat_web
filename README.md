# 企业微信web端自动化测试框架

## 采用的技术 
selenium + python3 + unittest + allure

##基于PageObject的基本原则
base：对selenium的方法进行二次封装层
data：存放测试数据，有excel格式、
page：以页面为单位对页面设计的操作进行方法封装
report：存放测试报告，生成HtmlTestRunner的测试报告
test_case: 编写测试用例