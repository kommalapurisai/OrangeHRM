from selenium import webdriver
from selenium.webdriver.common.by import By

class Home_LogIn:
    txt_username_name="username"
    txt_psw_name="password"
    btn_login_xpath="//button[@type='submit']"
    lnk_Invalid_xpath="//div[@class='oxd-alert-content oxd-alert-content--error']//p"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,user):
        self.driver.find_element(By.NAME,self.txt_username_name).send_keys(user)
    def setPassword(self,psw):
        self.driver.find_element(By.NAME,self.txt_psw_name).send_keys(psw)
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def TextInvalid(self):
        return self.driver.find_element(By.XPATH,self.lnk_Invalid_xpath).text