import os
import time
import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

dotenv.load_dotenv()

INSTAGRAM_URL = "https://www.instagram.com/"
EMAIL = os.environ.get("INSTAGRAM_EMAIL")
PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")
SIMILAR_ACCOUNT = "chefsteps"


class InstagramFollowerBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def log_in(self):
        self.driver.get(url=INSTAGRAM_URL)

        time.sleep(2)
        email_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_input.send_keys(EMAIL)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(PASSWORD)

        submit_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        submit_button.click()

        time.sleep(5)
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(5)
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(5)

        def find_followers(self):
            time.sleep(5)
            # Show followers of the selected account.
            self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

            time.sleep(5.2)
            # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
            modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
            modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)

            for i in range(10):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                time.sleep(2)
    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


instagram_follower = InstagramFollowerBot()
instagram_follower.log_in()
instagram_follower.find_followers()
instagram_follower.follow()