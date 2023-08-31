import time

import pytest
from selenium import webdriver


@pytest.mark.regression
def test_MessageTest():
    print("Test delete 1 - 1")

@pytest.mark.regression
def test_qwerty():
    print("Test delete 2 - 2")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.codeconvert.ai/java-to-python-converter")
    time.sleep(5)
    print("bD=======")
    driver.quit()

