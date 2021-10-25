from selenium import webdriver
from selenium.webdriver.common.by import By

from test_wework_login.login import Login
from test_wework_login.register import Register


class Index:
    """
    首页页面po
    """
    def __init__(self):
        option = Options()
        # 和浏览器打开的调试端口进行通信
        # 浏览器要使用 --remote-debugging-port=9222 开启调试
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def goto_register(self):
        """
        点击立即注册
        进入注册页po
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, '').click()
        return Register()

    def goto_login(self):
        """
        点击企业登录
        进入登录页面po
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, '').click()
        return Login(self.driver)
