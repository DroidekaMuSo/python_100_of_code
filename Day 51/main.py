import os
import time

import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

dotenv.load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
X_URL = "https://x.com/"
SPEED_TEST_URL = "https://www.speedtest.net/"

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url=SPEED_TEST_URL)

        start_button = self.driver.find_element(by=By.XPATH,
                                                value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_button.click()

        time.sleep(60)
        back_to_results = self.driver.find_element(by=By.XPATH,
                                                   value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')
        back_to_results.click()

        self.up = self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

        print(f"You download speed is {self.up.text} and your upload speed is {self.down.text}")

    def tweet_at_provider(self):
        self.driver.get(url=X_URL)

        time.sleep(2)
        dismiss_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[2]/div/div/div/button')
        dismiss_button.click()

        time.sleep(2)
        google_log_in = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a')
        google_log_in.click()

        time.sleep(2)
        email_log_in = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email_log_in.send_keys(f"{EMAIL}")

        next_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        next_button.click()

        time.sleep(2)
        password_log_in = self.driver.find_element(By.XPATH,
                                                   '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_log_in.send_keys(f"{PASSWORD}")

        log_in = self.driver.find_element(By.XPATH,
                                          '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        log_in.click()

        time.sleep(4)
        dismiss_button = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/button')
        dismiss_button.click()

        tweet_compose = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


internet_speed = InternetSpeedTwitterBot()
internet_speed.get_internet_speed()
internet_speed.tweet_at_provider()
