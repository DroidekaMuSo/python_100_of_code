from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
import dotenv
import time
import os

dotenv.load_dotenv()

LINKEDIN_URL = ("https://tinder.com/")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=LINKEDIN_URL)

#Main window
time.sleep(2)
base_window = driver.window_handles[0]
decline_cookies = driver.find_element(by=By.XPATH,
                                      value='//*[@id="u-1419960890"]/div/div[2]/div/div/div[1]/div[2]/button')
decline_cookies.click()

log_in = driver.find_element(by=By.XPATH,
                             value='//*[@id="u-1419960890"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
log_in.click()

time.sleep(2)
facebook_log_in = driver.find_element(by=By.XPATH,
                                      value='//*[@id="u1146625330"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]')
facebook_log_in.click()

# Facebook pop up window
time.sleep(2)
fb_popup_window = driver.window_handles[1]
driver.switch_to.window(fb_popup_window)

email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("diegomunozsolis@hotmail.com")

password_input = driver.find_element(By.NAME, "pass")
password_input.send_keys("toribio")

fb_log_in_button = driver.find_element(By.NAME, "login")
fb_log_in_button.click()

#Switching back to base screen
time.sleep(3)
driver.switch_to.window(base_window)

time.sleep(3)
allow_location_button = driver.find_element(By.XPATH, '//*[@id="u1146625330"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

dismiss_notifications = driver.find_element(By.XPATH, '//*[@id="u1146625330"]/div/div/div/div/div[3]/button[2]')
dismiss_notifications.click()

time.sleep(7)

for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
                                          '//*[@id="u-1419960890"]/div/div[1]/div/main/div[2]/div/div/div[1]/div['
                                          '1]/div/div[3]/div/div[4]/button')

        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
