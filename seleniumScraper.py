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
time.sleep(14)

# Gets a list of all iframes on the page
#iframes = driver.find_elements("tag name", "iframe")
#print(f"Found {len(iframes)} iframes")

# Prints out iframe's attributes to help identify
#for index, iframe in enumerate(iframes):
   # print(f"Iframe {index}: {iframe.get_attribute('title')}")


# scrolling the #root element
#scrollable_container = driver.find_element(By.CSS_SELECTOR, "#root")
#driver.execute_script("arguments[0].scrollTop += 500;", scrollable_container)
#time.sleep(2)  # Wait to observe the effect

# Find an element further down on the page
#element_to_scroll_to = driver.find_element(By.CSS_SELECTOR, "footer")
#driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll_to)
#time.sleep(2)  # Wait to observe the effect



# collects and filters transaction texts that start with '+'
transactions = driver.find_elements(By.CSS_SELECTOR, "[data-testid='transactions-list-item-amount']")

for transaction in transactions:
    if transaction.text and transaction.text[0] == '+':
        transactionTexts.append(transaction.text)


# Print collected transaction texts
print(transactionTexts)

transactionNums = []
avg = 0

for transaction in transactionTexts:
    transaction = transaction[2:]
    transaction = float(transaction)
    transactionNums.append(transaction)

avg = sum(transactionNums) / len(transactionNums)

print(f"You have been averaging: ${avg} in tips every shift")


# closes the browser
driver.quit()