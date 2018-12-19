'''登陆新平台'''
New_address = 'https://lxerptest.66123123.com/'


from driver.alldriver import choicedr
import time
from selenium.webdriver.common.action_chains import ActionChains


class handles():
    def __init__(self, driver):
        self.dr = choicedr(driver)

    def login(self):
        '''用户登陆'''
        self.dr.get(New_address)
        self.dr.find_element_by_xpath('.//input[@placeholder="请输入账号"]').clear()
        self.dr.find_element_by_xpath('.//input[@placeholder="请输入账号"]').send_keys('aaa')
        self.dr.find_element_by_xpath('.//input[@placeholder="请输入密码"]').clear()
        self.dr.find_element_by_xpath('.//input[@placeholder="请输入密码"]').send_keys('1')
        self.dr.find_element_by_xpath('.//button[@class="el-button el-button--primary"]').click()

    def choicemod(self, mod):
        '''选择操作模块'''
        self.dr.find_element_by_xpath('.//li[text()="'+mod+'"]').click()

    def homepagehandles():
        '''首页操作'''
        pass

    def goodshandles():
        '''商品模块操作'''
        pass

    def addsupplier(self):
        self.dr.implicitly_wait(3)
        '''添加供应商'''
        self.dr.find_element_by_xpath('.//a[@href="#/supplier/supplierindex/addSupplier"]').click()
        time.sleep(2)
        self.dr.switch_to_window(self.dr.window_handles[1])
        '''供应商名称'''
        self.dr.find_element_by_xpath('.//input[@placeholder="字数长度1~30以内"]').clear()
        self.dr.find_element_by_xpath('.//input[@placeholder="字数长度1~30以内"]').send_keys('北汽集团')
        '''公司简称'''
        self.dr.find_element_by_xpath('.//input[@placeholder="字数长度1~15以内"]').clear()
        self.dr.find_element_by_xpath('.//input[@placeholder="字数长度1~15以内"]').send_keys('北汽集团')
        '''供应商等级'''
        self.dr.find_element_by_xpath('.//input[@placeholder="供应商等级"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('.//span[text()="1级"]').click()
        '''公司法人'''
        self.dr.find_element_by_xpath('.//input[@placeholder="输入姓名，字数1~15以内"]').clear()
        self.dr.find_element_by_xpath('.//input[@placeholder="输入姓名，字数1~15以内"]').send_keys('法人')
        '''法人身份证'''
        self.dr.find_element_by_xpath('.//input[@placeholder="18位字符"]').clear()
        self.dr.find_element_by_xpath('.//input[@placeholder="18位字符"]').send_keys('123456789123456789')
        '''社会信用代码'''
        self.dr.find_element_by_xpath('.//input[@placeholder="请输入公司纳税识别号"]').clear()
        self.dr.find_element_by_xpath('.//input[@placeholder="请输入公司纳税识别号"]').send_keys('1')
        '''经营范围'''
        self.dr.find_element_by_xpath('.//textarea[@placeholder="字数长度1~1000以内"]').clear()
        self.dr.find_element_by_xpath('.//textarea[@placeholder="字数长度1~1000以内"]').send_keys('1')
        '''地址选择'''
        self.dr.find_element_by_xpath('.//input[@placeholder="省"]').click()
        time.sleep(2)
        a1 = self.dr.find_elements_by_xpath('//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[@class="el-select-dropdown__item"]')
        if a1[1].is_displayed():
            a1.click()
        else:
            print('fail')
        self.dr.find_element_by_xpath('.//input[@placeholder="市"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('.//span[@text()="贵阳"]').click()
        self.dr.find_element_by_xpath('.//input[@placeholder="县/区"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('.//span[@text()="市辖区"]').click()
        self.dr.find_element_by_xpath('.//textarea[@placeholder="请输入200字以内"]').send_keys('详细地址')
        '''上传资质文件'''
        self.dr.find_element_by_xpath(
            './/input[@class="el-upload__input"]').send_keys('E:\\u=4118960086,2125569760&fm=27&gp=0.jpg')
        '''公司经营区域'''
        self.dr.find_element_by_xpath('.//span/span[@text()="贵州"]').click()
        '''经营分类'''
        '''经营品牌'''
        '''公司纳税级别'''
        self.dr.find_element_by_xpath('.//input[@value="TAX_LEVEL0"]').click()
        '''开户行'''
        self.dr.find_element_by_xpath('.//div/div[20]/div/div[1]/input').send_keys('1')
        '''开户名称'''
        self.dr.find_element_by_xpath('.//div/div[21]/div/div[2]/input').send_keys('1')
        '''开户账号'''
        self.dr.find_element_by_xpath('.//div/div[22]/div/div[1]/input').send_keys('1')
        '''开票地址'''
        self.dr.find_element_by_xpath('.//textarea[@placeholder="输入姓名，字数1~15以内"]').send_keys('1')
        '''开票电话'''
        self.dr.find_element_by_xpath('.//input[@placeholder="输入姓名，字数1~15以内"]').send_keys('111')

    def choicesupplier(self):
        '''供货商查询'''
        self.dr.find_element_by_xpath('//input[@placeholder="供应商ID"]').send_keys(123)
        self.dr.find_element_by_xpath('//input[@placeholder="公司名称/简称"]').send_keys(123)
        self.dr.find_element_by_xpath('//input[@placeholder="公司法人"]').send_keys(123)
        self.dr.find_element_by_xpath('//input[@placeholder="供应商等级"]').click()
        time.sleep(2)
        a1 = self.dr.find_element_by_xpath('//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[1]')
        ActionChains(self.dr).move_to_element(a1)
        a1.click()
        self.dr.find_element_by_xpath('//input[@placeholder="更新状态"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//span[@text()="草稿"]').click()
        self.dr.find_element_by_xpath('//button[@class="el-button w80 h40 el-button--default el-button--small"]').click()

a = handles('firefox')
a.login()
time.sleep(4)
a.choicemod('供应商')
time.sleep(2)
a.choicesupplier()