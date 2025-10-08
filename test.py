from time import sleep
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.story("百度首页")
class TestLogin:

    @allure.step("搜索功能正常")
    def test_demo_01(self):
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com/')
        driver.maximize_window()
        sleep(2)
        driver.find_element(By.XPATH, "//textarea[@id='chat-textarea']").send_keys('UI自动化')
        sleep(2)
        driver.find_element(By.XPATH, "//button[@id='chat-submit-button']").click()
        sleep(2)
        driver.maximize_window()
        sleep(2)

    @allure.step("验证码错误，登录失败")
    def test_demo_02(self):#登录，输入错误信息报错
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com/')
        driver.maximize_window()
        sleep(2)
        driver.find_element(By.XPATH,"//a[@id='s-top-loginbtn']").click()
        sleep(2)
        driver.find_element(By.XPATH, "//span[@id='TANGRAM__PSP_11__changeSmsCodeItem']").click()
        sleep(2)
        driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__smsPhone']").send_keys('15656083333')
        sleep(2)
        driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__smsVerifyCode']").send_keys('111')
        sleep(2)
        driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__smsIsAgree']").click()
        sleep(2)
        driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__smsSubmit']").click()
        sleep(2)
        result_01 = '验证码不存在或已过期,请重新输入'
        result_02 = '登录过于频繁,请24小时后再试'
        text = driver.find_element(By.XPATH,"//span[@id='TANGRAM__PSP_11__smsError']").text
        assert text == result_01 or text == result_02
if __name__ == "__main__":
    test = TestLogin()
