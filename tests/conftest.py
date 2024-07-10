import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", default="chrome", action="store"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        obj = webdriver.ChromeOptions()
        obj.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=obj)
        driver.get("https://www.amazon.com")
        driver.maximize_window()
        driver.implicitly_wait(5)
        request.cls.driver = driver
    elif browser_name == "edge":
        obj = webdriver.EdgeOptions()
        obj.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=obj)
        driver.get("https://www.amazon.com")
        driver.maximize_window()
        driver.implicitly_wait(5)
        request.cls.driver = driver
    yield
    driver.close()
