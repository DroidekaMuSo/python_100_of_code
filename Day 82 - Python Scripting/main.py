from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://en.wikipedia.org/wiki/Morse_code")

letters_elements = driver.find_elements(By.CSS_SELECTOR, value=".jquery-tablesorter td b a")
symbols_elements = driver.find_elements(By.CSS_SELECTOR, value=".oo-ui-labelElement-label")

letters = [element.text[0] for element in letters_elements]
symbols = [element.text for element in symbols_elements]

driver.quit()
