# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import json
from cookiespool.db import RedisClient
from login.sili.cookies import SiliCookies


class CookiesGenerator(object):
    def __init__(self, website='default'):
        """
        父类, 初始化一些对象
        :param website: 名称
        """
        self.website = website
        self.cookies_db = RedisClient('cookies', self.website)
        self.accounts_db = RedisClient('accounts', self.website)

    def new_cookies(self, username, password):
        """
        新生成Cookies，子类需要重写
        :param username: 用户名
        :param password: 密码
        :return:
        """
        raise NotImplementedError

    def run(self):
        """
        运行, 得到所有账户, 然后顺次模拟登录
        :return:
        """
        accounts_usernames = self.accounts_db.usernames()
        cookies_usernames = self.cookies_db.usernames()

        for username in accounts_usernames:
            if not username in cookies_usernames:
                password = self.accounts_db.get(username)
                print('正在生成Cookies', '账号', username, '密码', password)
                result = self.new_cookies(username, password)
                cookies = result
                print('成功获取到Cookies', cookies)
                if self.cookies_db.set(username, json.dumps(cookies)):
                    print('成功保存Cookies')
        else:
            print('所有账号都已经成功获取Cookies')


class SiliCookiesGenerator(CookiesGenerator):
    def __init__(self, website='sili'):
        """
        初始化操作
        :param website: 站点名称
        """
        CookiesGenerator.__init__(self, website)
        self.website = website

    def new_cookies(self, username, password):
        """
        生成Cookies
        :param username: 用户名
        :param password: 密码
        :return: 用户名和Cookies
        """
        return SiliCookies(username, password).main()


if __name__ == '__main__':
    generator = SiliCookiesGenerator()
    generator.run()
