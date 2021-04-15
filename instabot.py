from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self, my_username, my_password):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)
        username = self.driver.find_element_by_name("username")
        username.send_keys(my_username)
        password = self.driver.find_element_by_name("password")
        password.send_keys(my_password)
        password.send_keys(Keys.ENTER)

    def find_followers(self, trgt_account):
        self.driver.get(f"https://www.instagram.com/{trgt_account}/followers/")
        self.driver.find_element_by_css_selector("a.-nal3").click()

    def follow(self):
        time.sleep(5)
        scr1 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        u = self.driver.find_element_by_class_name("PZuss")
        i = u.find_elements_by_tag_name("li")
        for user in i:
            try:
                e = user.find_element_by_css_selector(".sqdOP.L3NKy.y3zKF")
                if e.text == "Follow":
                    e.click()
                    print("Added")
            except (NoSuchElementException, ElementClickInterceptedException):
                print("Not Added")
            finally:
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                time.sleep(2)
