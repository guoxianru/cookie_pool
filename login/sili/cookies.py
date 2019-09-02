# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import time
from selenium import webdriver


class SiliCookies():
    def __init__(self, username, password):
        """定义类变量,生成浏览器对象"""
        self.url = 'https://www.siliconexpert.cn/zh-cn/login'
        self.username = username
        self.password = password

        # 生产环境:外部连接生成webdriver对象
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        time.sleep(5)
        self.browser = webdriver.Remote(
            command_executor="http://selenium_cookie:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.CHROME)

        # # 开发环境:Chrome无界面
        # from selenium.webdriver.chrome.options import Options
        # opt = Options()
        # opt.add_argument('--headless')
        # self.browser = webdriver.Chrome(chrome_options=opt)

        self.browser.delete_all_cookies()

    def login(self):
        """模拟用户登陆"""
        # 打开登录页面
        self.browser.get(self.url)
        time.sleep(3)

        # 输入用户名
        username_input = self.browser.find_element_by_id('input_email_sd')
        username_input.clear()
        username_input.send_keys(self.username)
        time.sleep(3)

        # 输入密码
        password_input = self.browser.find_element_by_id('pwd')
        password_input.clear()
        password_input.send_keys(self.password)
        time.sleep(3)

        # 截取验证码图片
        verifiy_img = self.browser.find_element_by_id('recaptchaImage')
        verifiy_img.screenshot('yzm.png')

        # 识别验证码

        # 百度API识别
        from .verifiy_image import verifiy_baiduapi
        verifiy_code = verifiy_baiduapi()

        # # OCR识别
        # from .verifiy_image import verifiy_tesserocr
        # verifiy_code = verifiy_tesserocr()

        # # 联众识别
        # from login.sili.verifiy_image import verifiy_liangzhong
        # verifiy_code = verifiy_liangzhong()

        # 输出验证码
        print('验证码为：%s' % str(verifiy_code))

        # 输入验证码
        verifiy_input = self.browser.find_element_by_id('captcha_code')
        verifiy_input.clear()
        verifiy_input.send_keys(str(verifiy_code))
        time.sleep(3)

        # 点击登录按钮
        try:
            login_button = self.browser.find_element_by_id('submitBTN')
            login_button.click()
            time.sleep(3)
        except Exception as e:
            print('Error：%s' % e)

        # 点击继续按钮
        try:
            continue_button = self.browser.find_element_by_xpath('//*[@id="mrp_btn_pwd"][2]')
            continue_button.click()
            time.sleep(3)
        except Exception as e:
            print('Error：%s' % e)

    def cookie(self):
        """验证登陆是否成功,更新cookie"""
        verifiy_str = 'wangyang@cissdata.com'
        # 验证是否通过
        if verifiy_str in self.browser.page_source:
            # 登陆成功，获取cookie，并把selenium格式的cookie转换成scrapy可用格式
            seleniumCookies = self.browser.get_cookies()
            cookie_list = [{i['name']: i['value']} for i in seleniumCookies]
            cookie = {}
            for i in cookie_list:
                cookie.update(i)
            # 返回scrapy可用格式的cookie
            return cookie
        else:
            # 登陆失败，返回提示
            return '验证失败!'

    def close(self):
        """操作结束后关闭浏览器"""
        self.browser.close()

    def main(self):
        """
        破解入口
        :return:
        """
        while 1:
            self.login()
            cookie = self.cookie()
            if cookie != '验证失败!':
                break
        self.close()
        return cookie


if __name__ == '__main__':
    result = SiliCookies('wangyang@cissdata.com', 'Ciss888*').main()
    print(result)
