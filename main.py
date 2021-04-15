import time
from instabot import InstaFollower

MY_USERNAME = "my_instagram_username"
MY_PASSWORD = "my_instagram_username_password"
TARGET_ACCOUNT = "account_to_autofollow_followers"

CHROME_DRIVER_PATH = "/Users/nn-admin/Desktop/Python Course/chromedriver"

instabot = InstaFollower(CHROME_DRIVER_PATH)
instabot.login(MY_USERNAME, MY_PASSWORD)
time.sleep(3)
instabot.find_followers(TARGET_ACCOUNT)
time.sleep(3)
instabot.follow()
