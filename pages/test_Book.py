import os
import time
from datetime import datetime
from pyclbr import Class

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_bookingDesk(self):
        time.sleep(2)
        self.driver.find_element(By.NAME, "emailId").send_keys("prasath.ranganathan@brickendon.com")
        time.sleep(5)

    @pytest.mark.qa
    def test_bookingRoom(self):
        self.driver.find_element(By.XPATH, "//*[@type='submit']").click()
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(),name="test_bookingRoom",attachment_type=AttachmentType.PNG)


    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.get("https://www.google.com/")
    # time.sleep(5)
    # print("BR=======")
    # driver.quit()

# def test_bookingParking():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://dgthrms.dreamguystech.com/login")
#     time.sleep(5)
#     print("bD=======")
#     driver.quit()
