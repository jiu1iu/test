# coding=utf-8

import configparser

class loadini():
    def __init__(self, FileName = None):
        if FileName == None:
            FileName = 'E:/gitcode/git_work/config/test_config.ini'
        self.cf = self.load_ini(FileName)

    def load_ini(self, a):
        cf = configparser.ConfigParser()
        cf.read(a, 'utf-8')
        return cf

    def get_value(self, key, value):
        return self.cf.get(key, value)


