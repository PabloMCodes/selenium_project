from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # allows delay
import os

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# sets up the chrome wbdriver
driver = webdriver.Chrome()

# opens the instant website
driver.get("https://mobile.instant.co/login")

time.sleep(2)

# array that holds all transaction strings
transactionTexts = []

#fills out email login
emailTextBar = driver.find_element(By.CSS_SELECTOR, "[data-testid='login-email']")
emailTextBar.click()
time.sleep(1)
emailTextBar.send_keys(email)

#fills out password login
passwordTextBar = driver.find_element(By.CSS_SELECTOR, "[data-testid='text-input-flat']")
passwordTextBar.click()
time.sleep(1)
passwordTextBar.send_keys(password)
time.sleep(1)

#clicks the login button
loginButton = driver.find_element(By.CSS_SELECTOR, "[data-testid='create-account-button-text']")
loginButton.click()
time.sleep(2)

#closes thing about using mobile app
closeButton = driver.find_element(By.CSS_SELECTOR, "[data-testid='button-text']")
closeButton.click()
time.sleep(1)

#clicks the 'More Transactions' button
moreTransacButton = driver.find_element(By.CSS_SELECTOR, "[data-testid='view-more-transactions-button-text']")
moreTransacButton.click()
time.sleep(5)

# collects and filters transaction texts that start with '+'
transactions = driver.find_elements(By.CSS_SELECTOR, "[data-testid='transactions-list-item-amount']")

for transaction in transactions:
    if transaction.text and transaction.text[0] == '+':
        transactionTexts.append(transaction.text)


# Print collected transaction texts
print(transactionTexts)

# closes the browser
driver.quit()