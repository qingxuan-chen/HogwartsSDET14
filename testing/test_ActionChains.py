from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestSeleniumDemo:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_actionchains(self):
        self.driver.get('https://www.baidu.com/')
        el = self.driver.find_element(By.ID, 'kw')
        el1 = self.driver.find_element(By.ID, 'su')
        action = ActionChains(self.driver)
        action.send_keys_to_element(el, 'selenium')
        action.click(el1)
        action.perform()
        el2 = self.driver.find_element(By.XPATH, '//*[@id="1"]/h3/a')
        action.click(el2)
        action.perform()
        sleep(3)