import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSd04wdTlR_pvIz30MTakPj9XODjQd8h9QQAvAUfczA58YZQGg/viewform?usp=sf_link"
zillow_url = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(url=zillow_url)
zillow_page = response.text

soup = BeautifulSoup(zillow_page, "lxml")
house_prices = soup.select(selector=".PropertyCardWrapper__StyledPriceLine")
house_addresses = soup.select(selector=".StyledPropertyCardDataArea-anchor")
house_links = soup.select(selector=".StyledPropertyCardDataArea-anchor")

links = [link.get("href") for link in house_links]
prices = [price.text.replace("+", "") for price in house_prices]
prices_update = [price[:6].strip() for price in prices]
addresses = [address.text.strip().replace("|", "") for address in house_addresses]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=form_url)

time.sleep(3)
for item in range(len(prices_update)):
    time.sleep(1)
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(addresses[item])

    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(prices_update[item])

    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(links[item])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()

    time.sleep(1)
    submit_another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another.click()

