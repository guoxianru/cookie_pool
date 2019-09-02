# -*- coding: utf-8 -*-
# -*- author: GXR -*-

from cookiespool.db import RedisClient

conn = RedisClient('accounts', 'sili')


def set(account, sep='-'):
    username, password = account.split(sep)
    result = conn.set(username, password)
    print('账号', username, '密码', password)
    print('录入成功' if result else '录入失败')


def scan():
    print('请输入账号密码组(格式：账号-密码，输入exit退出读入)：')
    while True:
        account = input()
        if account == 'exit':
            break
        set(account)


if __name__ == '__main__':
    scan()
