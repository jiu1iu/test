# coding=utf-8
import sys
sys.path.append('E:/gitcode/git_work/util')
from load_ini import loadini

'''获取元素'''
class Element():
    def __init__(self, driver):
        self.dr = driver

    def get_element(self, key):
        data = loadini().get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        print(data)
        try:
            if by == 'css':
                return self.dr.find_element_by_css_selector(value)
            elif by == 'id':
                return self.dr.find_element_by_id(value)
            elif by == 'name':
                return self.dr.find_element_by_name(value)
            else:
                return self.dr.find_element_by_xpath(value)
        except:
            return '未找到该定位信息'