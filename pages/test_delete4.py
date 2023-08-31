from selenium import webdriver


def test_one():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.codeconvert.ai/java-to-python-converter")
    act_title = driver.title
    exp_title = "%^^CodeConvert AI - Convert code with a click of a button"
    assert act_title.__eq__(exp_title)
    print(act_title)
    print(exp_title)
    driver.get("https://www.google.com/")


