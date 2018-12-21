# coding=utf-8
from selenium import webdriver
import sys
sys.path.append('..')
from util.load_ini import loadini

'''基本操作'''
class dr_handles():
    def __init__(self, url, driver='firefox'):
        self.dr = self.opendriver(url, driver)

    '''打开url网站'''
    def opendriver(self, url, driver):
        if driver == 'ie':
            dr = webdriver.Ie()
        elif driver == 'chrome':
            dr = webdriver.Chrome()
        else:
            dr = webdriver.Firefox()
        dr.get(url)
        dr.maximize_window()
        return dr
