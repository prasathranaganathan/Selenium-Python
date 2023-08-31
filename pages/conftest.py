import os

import pytest
from selenium import webdriver


@pytest.mark.qa
@pytest.fixture(autouse=True, scope="class")
# @pytest.fixture()
def setup_and_teardown(request):
    options = webdriver.ChromeOptions()
    # options.add_argument("--disable-info bars")
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument('--incognito')
    options.add_experimental_option('detach', True)
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://hhplus-preprod.hybridhero.com/")
    request.cls.driver = driver
    print(driver.title)
    driver.maximize_window()
    yield
    print(driver.title)
# if __name__ == '__main__':
#     pytest.main()  # start pytest framework
#     os.system('allure generate temps_dir -o report_dir --clean')  # generate report
#     os.system('allure open report_dir -p 0')
# --------------------------------------------
# # def pytest_addoption(parser):
#     parser.addoption("--browser")

# @pytest.fixtures()
# def setup_and_teardown(request):
#     global driver
#     browser = request.config.getoption("--browser")
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "edge":
#         driver = webdriver.Edge()
#     driver.get("https://hhplus-preprod.hybridhero.com/")
#     print(driver.title)
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.quit()
