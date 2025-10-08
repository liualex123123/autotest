from time import sleep
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

#from settings import ENV


class TestLogin:
    # def setup_class(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("https://www.baidu.com/")
    #     sleep(2)

    # def teardown_class(self):
    #     self.driver.quit()

    def test_demo_01(self):
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com/')
        driver.maximize_window()
        # driver = open
        # driver.get(ENV.url)
        sleep(3)
        driver.find_element(By.XPATH, "//textarea[@id='chat-textarea']").send_keys('UI自动化')
        sleep(3)
        driver.find_element(By.XPATH, "//button[@id='chat-submit-button']").click()
        sleep(2)
        driver.maximize_window()
        sleep(3)

    # @pytest.mark.parametrize('phone,VerifyCode,result', [
    #     ('15656081031', '111111', '验证码不存在或已过期,请重新输入')
    # ])

    def test_demo_02(self):#登录，输入错误信息报错
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com/')
        driver.maximize_window()
        sleep(3)
        # driver = open
        driver.find_element(By.XPATH,"//a[@id='s-top-loginbtn']").click()
        sleep(2)
        driver.find_element(By.XPATH, "//span[@id='TANGRAM__PSP_11__changeSmsCodeItem']").click()
        sleep(2)
        driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__smsPhone']").send_keys('15656083333')
        sleep(2)
        driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__smsVerifyCode']").send_keys('111')
        sleep(1)
        driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__smsIsAgree']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__smsSubmit']").click()
        sleep(1)
        result = '验证码不存在或已过期,请重新输入'
        text = driver.find_element(By.XPATH,"//span[@id='TANGRAM__PSP_11__smsError']").text
        assert text == result
if __name__ == "__main__":
    test = TestLogin()
    # pytest.main(['–alluredir', './temp'])
    # os.system('allure generate D:\python-gx\pythonProject\demo/temp -o D:\python-gx\pythonProject\demo/report --clean')
    # test.setup_class()
    # test.test_demo_01()
    # test.test_demo_02()
    # test.teardown_class()
