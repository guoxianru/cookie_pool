##### cookie_pool 爬虫可扩展cookie池


* 借鉴于：https://github.com/Python3WebSpider/CookiesPool
* 2019.07.02 改进部分代码


### 一、下载安装
```shell
git clone https://github.com/guoxianru/cookie_pool
```

### 二、安装依赖
```shell
pip install -r requirements.txt
```

### 三、配置config
* config.py 为项目配置文件

## 基础配置
```python
# Redis数据库地址，生产环境请配置为公网IP
REDIS_HOST = '39.106.189.108'
# Redis端口
REDIS_PORT = 6379
# Redis密码，如无填None
REDIS_PASSWORD = ''
# 产生器使用的浏览器
BROWSER_TYPE = 'Chrome'
# 产生器类，如扩展其他站点，请在此配置
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}
# 测试类，如扩展其他站点，请在此配置
TESTER_MAP = {
    'weibo': 'WeiboValidTester'
}
# 检测器检测接口
TEST_URL_MAP = {
    'weibo': 'https://m.weibo.cn/api/container/getIndex?uid=1804544030&type=uid&page=1&containerid=1076031804544030'
}
# 产生器和验证器循环周期
CYCLE = 120
# API地址和端口
API_HOST = '0.0.0.0'
API_PORT = 5020
```

## 进程开关
```python
# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = True
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = True
# API接口服务
API_PROCESS = True
```

### 四、账号购买

账号可在淘宝购买

## 导入账号
```shell
python importer.py
```

```shell
请输入账号密码组(格式：账号-密码，输入exit退出读入)：
18459748505-astvar3647
14760253606-gmidy8470
14760253607-uoyuic8427
18459749258-rktfye8937
账号 18459748505 密码 astvar3647
录入成功
账号 14760253606 密码 gmidy8470
录入成功
账号 14760253607 密码 uoyuic8427
录入成功
账号 18459749258 密码 rktfye8937
录入成功
exit
```

### 五、运行

请先导入一部分账号之后再运行，运行命令：

```shell
python run.py
```
## 运行效果

三个进程全部开启：

```shell
API接口开始运行
 * Running on http://0.0.0.0:5020/ (Press CTRL+C to quit)
Cookies生成进程开始运行
Cookies检测进程开始运行
正在生成Cookies 账号 14747223314 密码 asdf1129
正在测试Cookies 用户名 14747219309
Cookies有效 14747219309
正在测试Cookies 用户名 14740626332
Cookies有效 14740626332
正在测试Cookies 用户名 14740691419
Cookies有效 14740691419
正在测试Cookies 用户名 14740618009
Cookies有效 14740618009
正在测试Cookies 用户名 14747222472
Cookies有效 14747222472
Cookies检测完成
验证码位置 420 580 384 544
成功匹配
拖动顺序 [1, 4, 2, 3]
成功获取到Cookies {'SUHB': '08J77UIj4w5n_T', 'SCF': 'AimcUCUVvHjswSBmTswKh0g4kNj4K7_U9k57YzxbqFt4SFBhXq3Lx4YSNO9VuBV841BMHFIaH4ipnfqZnK7W6Qs.', 'SSOLoginState': '1501439488', '_T_WM': '99b7d656220aeb9207b5db97743adc02', 'M_WEIBOCN_PARAMS': 'uicode%3D20000174', 'SUB': '_2A250elZQDeRhGeBM6VAR8ifEzTuIHXVXhXoYrDV6PUJbkdBeLXTxkW17ZoYhhJ92N_RGCjmHpfv9TB8OJQ..'}
成功保存Cookies
```

### 五、Docker

1.开发环境 Docker
```shell
# Workdir proxy_pool
docker build -t proxy_pool .
docker run -it --rm -v $(pwd):/usr/src/app -p 5010:5010 proxy_pool
```

2.生产环境 Docker/docker-compose
```shell
## Workdir proxy_pool
# docker build -t proxy_pool .
# pip install docker-compose
docker-compose -f docker-compose.yml up -d --build
```


### 六、使用

1.可以通过api访问 39.106.189.108:5020 查看
```shell
{
'/<website>/add/<username>/<password>': u'添加账号组',
'/<website>/count': u'cookie数量',
'/<website>/random': u'获取一个cookie',
'使用方法': 'host:port/关键词'
}
```
2.爬虫使用
* 如果要在爬虫代码中使用的话， 可以将此api封装成函数直接使用.