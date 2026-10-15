# Task 4: Automated Web Application Testing

## 1. Project Overview

This project focuses on automated testing of the SauceDemo web application using Python and Selenium WebDriver. The objective is to verify important user workflows, including login, shopping cart functionality, and checkout.

## 2. Tools and Technologies

- Programming Language: Python 3.13.2
- Automation Tool: Selenium WebDriver
- Browser: Google Chrome
- Code Editor: Visual Studio Code
- Test Website: SauceDemo

## 3. Test Cases and Results

### Test Case 1: Login Functionality

Objective: Verify that a user can log in with valid credentials.

Steps:
1. Open the SauceDemo website.
2. Enter valid login credentials.
3. Click the Login button.
4. Verify successful login.

Expected Result: The user should access the product listing page.

Actual Result: Login test passed successfully.

Status: PASS

### Test Case 2: Shopping Cart

Objective: Verify that a product can be added to the shopping cart.

Steps:
1. Log in to SauceDemo.
2. Select a product.
3. Add the product to the cart.
4. Open the shopping cart.
5. Verify the selected product.

Expected Result: The selected product should appear in the cart.

Actual Result: Shopping cart test passed successfully.

Status: PASS

### Test Case 3: Checkout Overview

Objective: Verify that the checkout process reaches the order overview page.

Steps:
1. Log in to the application.
2. Add a product to the cart.
3. Open the cart.
4. Click Checkout.
5. Enter the required customer information.
6. Continue to the checkout overview.

Expected Result: The checkout overview should display the order details.

Actual Result: Checkout overview test passed successfully.

Status: PASS

### Test Case 4: Order Completion

Objective: Verify that a demonstration order can be completed.

Steps:
1. Proceed to the checkout overview.
2. Click Finish.
3. Verify the order confirmation message.

Expected Result: The application should display an order confirmation.

Actual Result: Order completion test passed successfully.

Status: PASS

## 4. BrowserStack Testing

BrowserStack Live was explored to investigate testing on remote browsers and devices. Access was limited by the available free-trial allowance and plan restrictions.

The automated tests documented above were executed locally using Selenium WebDriver and Google Chrome. Remote cross-browser testing is not reported as completed.

## 5. Conclusion

The automated tests successfully verified the login, shopping cart, checkout overview, and order completion workflows on SauceDemo using Python and Selenium WebDriver.

This project provided practical experience in web automation, functional testing, test verification, and documenting test results.