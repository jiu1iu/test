from selenium import webdriver

def choicedr(driver):
    '''浏览器选择'''
    if driver=='ie':
        return webdriver.Ie()
    elif driver=='chrome':
        return webdriver.Chrome()
    elif driver=='firefox':
        return webdriver.Firefox()