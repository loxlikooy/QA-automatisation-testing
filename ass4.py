from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Initialize the driver for Safari
driver = webdriver.Safari()

# Navigate to the website
driver.get("https://the-internet.herokuapp.com/")

# 1. Waits - Wait for the 'Form Authentication' link to be clickable
auth_link = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Form Authentication"))
)
auth_link.click()

# 2. Action Class - Hover over an image in the "Hovers" section
driver.get("https://the-internet.herokuapp.com/hovers")

# Wait for the image to be visible
hover_element = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='figure']/img"))
)

action = ActionChains(driver)
action.move_to_element(hover_element).perform()

# Verify that the hover text appears
hover_caption = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='figure']/div/h5"))
)
assert "name: user1" in hover_caption.text
# 3. For the Select Class demonstration, navigate to the dropdown page
driver.get("https://the-internet.herokuapp.com/dropdown")
dropdown_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, 'dropdown'))
)
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text('Option 2')

# Test Report
try:
    assert "The Internet" in driver.title
    print("Test Passed: Title is correct")
except AssertionError:
    print("Test Failed: Title is incorrect")

