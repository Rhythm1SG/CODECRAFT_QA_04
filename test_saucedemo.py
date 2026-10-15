from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Verify that the Products page opens
assert "Products" in driver.page_source

print("Login test passed successfully!")

time.sleep(3)
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Log in
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # Add the first product to the cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Open the shopping cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Verify the product is in the cart
    product = driver.find_element(By.CLASS_NAME, "inventory_item_name")

    assert product.text == "Sauce Labs Backpack"

    print("Shopping cart test passed successfully!")

finally:
    driver.quit()