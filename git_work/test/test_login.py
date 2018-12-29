# coding=utf-8

New_address = 'https://lxerptest.66123123.com/'
import sys
sys.path.append("..")
from driver.alldriver import dr_handles
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from util.findelement import Element
'''新平台操作'''
class handles():
    def __init__(self, url):
        self.dr = self.get_driver(url)

    def get_driver(self, url):
        dr = webdriver.Firefox()
        dr.get(url)
        dr.maximize_window()
        return dr

    def user_input(self, key, value, data):
        self.get_user_element(key, value).send_keys(data)

    def get_user_element(self, key, value):
        find_element = Element(self.dr)
        user_element = find_element.get_element(key, value)
        return user_element

    def main(self):
        user_name = 'aaa'
        password = '1'
        self.get_user_element('LoginData', 'username').clear()
        self.user_input('LoginData', 'username', user_name)
        self.get_user_element('LoginData', 'password').clear()
        self.user_input('LoginData', 'password', password)
        self.get_user_element('LoginData', 'button').click()
        time.sleep(3)
        self.dr.close()

if __name__ == '__main__':
    user = handles(New_address)
    user.main()
