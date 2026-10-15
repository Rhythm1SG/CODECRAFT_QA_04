from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Login
    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Add product to cart
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    # Open cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Start checkout
    driver.find_element(By.ID, "checkout").click()

    # Enter checkout information
    driver.find_element(By.ID, "first-name").send_keys("Rhythm")
    driver.find_element(By.ID, "last-name").send_keys("Shetty")
    driver.find_element(By.ID, "postal-code").send_keys("411001")

    driver.find_element(By.ID, "continue").click()

    # Verify checkout overview
    wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    print("Checkout overview test passed successfully!")

    # Complete the demonstration order
    driver.find_element(By.ID, "finish").click()

    # Verify confirmation
    confirmation = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    )

    assert confirmation.text == "Thank you for your order!"

    print("Order completion test passed successfully!")

except Exception as e:
    print("Checkout test failed:", e)

finally:
    driver.quit()