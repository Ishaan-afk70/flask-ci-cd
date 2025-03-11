import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver_path = "C://chromedriver//chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    yield driver
    driver.quit()

def test_google(browser):
    browser.get("http://www.google.com")
    assert "Google" in browser.title
