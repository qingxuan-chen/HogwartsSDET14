import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Test():
    def setup_method(self, method):
        option = Options()
        #和浏览器打开的调试端口进行通信
        #浏览器要使用 --remote-debugging-port=9222 开启调试
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def test_fuyong(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        # time.sleep(1)
        self.driver.find_element(By.ID, "su").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="2"]/h3/a/em').click()

    def test_weixin(self):
        self.driver.get("https://work.weixin.qq.com")
        # 创建一个数据库
        # db = shelve.open("cookies")
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688856682282916'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325109516673'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688856682282916'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'dMntC62r-EJ_WBqtYU3q_KQpNAc08AMtLD3-DNtycqlx1-k4CslL92tqqlroo4YXsk5eQJs3xxItwtZg2K18eKSvhu_DzykG6hg4lrfCGNr081g0zDro9go1QZ1oZ58rGW2a-SLoUGwe--l3WWNRRY8ZWzHVlH8Bc5NTfM10Wu79mFBDTYLn5ofMAva5NNJUhEtBxqvS_M6OHqdqf5QE2CkrvWAO_zy2XP4eK7A8P_14EPR4iBJZTcZ6yEWOc8KQbZVvEOK2I9XBGRkBkTyPuA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'PJcIiqJCxOXCfnxz-JZ_K9Bt9SeQSi31TUfVojhHJbhI8IlsLF1_Wpvn1iSN3Zqv'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a9468547'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.qq.com', 'expiry': 1634780667, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1634780661'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '02607231'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.qq.com', 'expiry': 1634867030, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.304104207.1634778737'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1666316661, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1634778737,1634780608'}, {'domain': '.work.weixin.qq.com', 'expiry': 1637372661, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1666055535, 'httpOnly': False, 'name': 'eas_sid', 'path': '/', 'secure': False, 'value': 'D1s643K455o1m9N5d3U5O7w196'}, {'domain': '.qq.com', 'expiry': 1697852630, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.967829235.1634778737'}, {'domain': '.work.weixin.qq.com', 'expiry': 1666314736, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '2430402236'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'd1002ef6b02a54ca5b5d1f015f0f2ce18e4b9a37e712d5be840b3d4929c4c149'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'cMooV2S7GI'}]
        # 将数据存储的shalve中
        # db['cookies'] = cookies
        # db.close()
        # 取出数据
        # cookies = db['cookies']

        #获取cookies
        # print(self.driver.get_cookies())


        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688856682282916'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325109516673'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688856682282916'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'dMntC62r-EJ_WBqtYU3q_KQpNAc08AMtLD3-DNtycqlx1-k4CslL92tqqlroo4YXsk5eQJs3xxItwtZg2K18eKSvhu_DzykG6hg4lrfCGNr081g0zDro9go1QZ1oZ58rGW2a-SLoUGwe--l3WWNRRY8ZWzHVlH8Bc5NTfM10Wu79mFBDTYLn5ofMAva5NNJUhEtBxqvS_M6OHqdqf5QE2CkrvWAO_zy2XP4eK7A8P_14EPR4iBJZTcZ6yEWOc8KQbZVvEOK2I9XBGRkBkTyPuA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'PJcIiqJCxOXCfnxz-JZ_K9Bt9SeQSi31TUfVojhHJbhI8IlsLF1_Wpvn1iSN3Zqv'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a9468547'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.qq.com', 'expiry': 1634780667, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1634780661'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '02607231'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.qq.com', 'expiry': 1634867030, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.304104207.1634778737'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1666316661, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1634778737,1634780608'}, {'domain': '.work.weixin.qq.com', 'expiry': 1637372661, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1666055535, 'httpOnly': False, 'name': 'eas_sid', 'path': '/', 'secure': False, 'value': 'D1s643K455o1m9N5d3U5O7w196'}, {'domain': '.qq.com', 'expiry': 1697852630, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.967829235.1634778737'}, {'domain': '.work.weixin.qq.com', 'expiry': 1666314736, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '2430402236'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'd1002ef6b02a54ca5b5d1f015f0f2ce18e4b9a37e712d5be840b3d4929c4c149'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'cMooV2S7GI'}]
        for cookie in cookies:
            if "expory" in cookie.keys():
                cookie.pop("expory")
            #把字典加入到driver的cookie中
            self.driver.add_cookie(cookie)


        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID, 'menu_contacts').click()
        # db.close()