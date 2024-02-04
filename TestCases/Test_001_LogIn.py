import time

import pytest
import openpyxl
from PageObjects.LogIn import Home_LogIn
from PageObjects.LogOut import LogOut
from Utilities.ReadPropertys import ReadConfig
from Utilities import XLUtilities
class Test_001_LogIn:
    baseURL=ReadConfig.getApplicationURL()

    def test_account_login(self,setup):
        self.driver=setup
        res_list=[]

        file="TestData\\LogIN.xlsx"

        self.driver.get(self.baseURL)
        time.sleep(3)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lg=Home_LogIn(self.driver)
        self.lo=LogOut(self.driver)

        self.rows=XLUtilities.getRowCount(file,"Orange")
        for r in range(2,self.rows+1):
            user=XLUtilities.readValues(file,"Orange",r,2)
            psw=XLUtilities.readValues(file,"Orange",r,3)
            self.lg.setUsername(user)
            self.lg.setPassword(psw)
            self.lg.clickLogin()
            time.sleep(3)
            self.exp=self.lo.VerifyLogo()

            if self.exp==True:
                res_list.append("Pass")
                self.lo.ClickProfile()
                self.lo.ClickLogOut()
            elif self.lg.TextInvalid()=="Invalid credentials":
                res_list.append("Pass")

            elif self.exp==False:
                res_list.append("Fail")
                self.lo.ClickProfile()
                self.lo.ClickLogOut()

            else:
                res_list.append("Fail")

        self.driver.close()

        if "Fail" not in res_list:
            assert True
        else:
            assert False



