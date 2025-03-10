import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class FlaskAppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configure Chrome to run in headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # Set implicit wait time
        cls.driver.implicitly_wait(10)

        # URL of the Flask application (adjust if needed)
        cls.url = "http://localhost:5000"

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

    def test_homepage_title(self):
        # Navigate to the homepage
        self.driver.get(self.url)

        # Check if the title contains expected text
        self.assertIn("Flask", self.driver.title)

    def test_homepage_content(self):
        # Navigate to the homepage
        self.driver.get(self.url)

        # Check if the page contains the correct content (adjusted based on the actual content)
        content = self.driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("To-Do List", content)  # Update to match actual content on your page


if __name__ == "__main__":
    unittest.main()
