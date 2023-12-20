import logging
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Set up the Safari browser for testing
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Safari()
    yield driver
    driver.quit()


def test_google_search(browser):
    with allure.step("Navigating to Google"):
        logger.info("Navigating to Google")
        browser.get("https://www.google.com")  # Navigate to Google

    with allure.step("Enter 'OpenAI' into search box"):
        logger.info("Entering search query: OpenAI")
        search_box = browser.find_element(By.NAME, "q")
        search_box.send_keys("OpenAI")
        search_box.submit()  # Conduct the search

    # Wait for the title to contain "OpenAI"
    WebDriverWait(browser, 10).until(EC.title_contains("OpenAI"))

    with allure.step("Verify search results are shown"):
        assert "OpenAI" in browser.title, "Search results title does not contain 'OpenAI'."
