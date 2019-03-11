from selenium import webdriver
from cfg import *
import time


class applicationForprinting():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(URL)


    def login(self):
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('username').send_keys(user)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('login-action').click()

    def enter_application_for_printing(self):
        # 进入用印申请的界面
        self.driver.find_element_by_css_selector('h2.collapsable').click()
        self.driver.find_element_by_css_selector('#mCSB_3_container > ul > li:nth-child(1) > div').click()
        self.driver.find_element_by_css_selector('#mCSB_3_container > ul > li:nth-child(1) > ul > li:nth-child(1) > div > a').click()

    def add_to_application_for_printing(self):





