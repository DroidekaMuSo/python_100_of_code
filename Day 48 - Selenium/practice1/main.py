from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

# number_articles = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# number_articles.click()

search = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a')
search.click()

input_tag = driver.find_element(By.CSS_SELECTOR, value="cdx-text-input__input")
input_tag.send_keys("Python", Keys.ENTER)



# driver.quit()

