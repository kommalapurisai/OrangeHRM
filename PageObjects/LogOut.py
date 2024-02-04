from selenium import webdriver
from selenium.webdriver.common.by import By

class LogOut():
    btn_profile_xpath="//span[@class='oxd-userdropdown-tab']"
    btn_logout_xpath="//ul[@class='oxd-dropdown-menu']//li[4]"
    lnk_logo_xpath="//div[@class='oxd-brand-banner']"

    def __init__(self,driver):
        self.driver=driver

    def ClickProfile(self):
        self.driver.find_element(By.XPATH,self.btn_profile_xpath).click()

    def ClickLogOut(self):
        self.driver.find_element(By.XPATH,self.btn_logout_xpath).click()

    def VerifyLogo(self):
        try:
            return self.driver.find_element(By.XPATH,self.lnk_logo_xpath).is_displayed()
        except:
            return False