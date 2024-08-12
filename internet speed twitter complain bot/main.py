from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
from dotenv import load_dotenv
load_dotenv()

PROMISE_DOWN = 150
PROMISE_UP = 10
x_email = os.getenv("TWITTER_EMAIL")
x_username = os.getenv("TWITTER_USERNAME")
x_password = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot():
    def __init__(self):
        self.download = 0
        self.upload = 0
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        go = self.driver.find_element(By.XPATH, value="//*[text()='Go']")
        go.click()
        time.sleep(60)
        download = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
        upload = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text
        self.download = download
        self.upload = upload


    def tweet_at_provider(self):
        self.driver.get("https://x.com/")
        time.sleep(2)
        signin = self.driver.find_element(By.XPATH, value="//*[text()='Sign in']")
        signin.click()
        time.sleep(5)
        email_field = self.driver.find_element(
            By.XPATH,
            value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]"
                  "/div/div/div/div[4]/label/div/div[2]/div/input"
        )
        email_field.send_keys(x_email, Keys.ENTER)
        time.sleep(3)
        username_field = self.driver.find_element(
            By.XPATH,
            value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]"
                  "/div[1]/div/div[2]/label/div/div[2]/div/input"
        )
        username_field.send_keys(x_username, Keys.ENTER)
        time.sleep(3)
        password_field = self.driver.find_element(
            By.XPATH,
            value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]"
                  "/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
        )
        password_field.send_keys(x_password, Keys.ENTER)
        input("Press Enter when you have signed in: ")
        tweet = (f"Hello Internet Provider. Why is my internet speed {self.download}down/{self.upload}up when I"
                 f"pay for {PROMISE_DOWN}down/{PROMISE_UP}up?")
        compose = self.driver.find_element(
            By.XPATH,
            value="//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]"
                  "/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]"
                  "/div/div/div/div/div/div[2]/div/div/div/div"
        )
        compose.send_keys(tweet)
        post = self.driver.find_element(By.XPATH, value="//*[text()='Post']")
        post.click()









bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()