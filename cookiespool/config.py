# -*- coding: utf-8 -*-
# -*- author: GXR -*-

# Redis数据库地址
REDIS_HOST = '39.106.189.108'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = '1111'

# 产生器类，如扩展其他站点，请在此配置
GENERATOR_MAP = {
    'sili': 'SiliCookiesGenerator'
}

# 测试类，如扩展其他站点，请在此配置
TESTER_MAP = {
    'sili': 'SiliValidTester'
}

TEST_URL_MAP = {
    'sili': 'https://www.siliconexpert.cn/productcategories'
}

# 产生器和验证器循环周期
CYCLE = 120

# API地址和端口
API_HOST = '0.0.0.0'
API_PORT = 5020

# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = True
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = True
# API接口服务
API_PROCESS = True
