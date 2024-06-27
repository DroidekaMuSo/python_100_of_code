from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import dotenv
import time
import os

dotenv.load_dotenv()

LINKEDIN_URL = ("https://www.linkedin.com/jobs/search/?currentJobId=3944582586&f_AL=true&geoId=101526486&keywords=python"
            "%20developer&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true&sortBy=R")
LINKEDIN_EMAIL = os.environ.get("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")

def abort_application():
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=LINKEDIN_URL)

#Click sign in button
sign_in_button = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in_button.click()
time.sleep(2)

#Filling out the sign in form
email_input = driver.find_element(By.ID, "username")
email_input.send_keys(LINKEDIN_EMAIL)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(LINKEDIN_PASSWORD)

submit_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
submit_button.click()

#Get jobs
all_jobs = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")

for job in all_jobs:
    print("Opening Listing")
    job.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue
