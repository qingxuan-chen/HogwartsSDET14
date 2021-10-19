from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By



class TestSeleniumDemo:
    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=opt)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        self.driver.get('https://www.baidu.com/')
        el = self.driver.find_element(By.ID, 'kw')
        el1 = self.driver.find_element(By.ID, 'su')
        el.send_keys('selenium')
        # action = TouchActions(self.driver)
        print(el)
        print(type(el))
        # el2 = self.driver.find_element(By.XPATH, '//*[@id="1"]/h3/a')
        # sleep(1)
        # action.scroll_from_element(el2, 0, 1000).perform()


        # sleep(1)