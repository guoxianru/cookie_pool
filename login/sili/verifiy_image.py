# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import json
import requests
import tesserocr
from PIL import Image


def verifiy_tesserocr():
    """图像验证码识别"""

    def binarizing(img, threshold):
        """传入image对象进行灰度、二值处理"""
        # 转灰度,传入参数'L'
        img = img.convert("L")
        pixdata = img.load()
        w, h = img.size
        # 遍历所有像素，大于阈值的为黑色
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255
        # 返回处理后图片对象
        return img

    def depoint(img):
        """传入二值化后的图片进行降噪处理"""
        pixdata = img.load()
        w, h = img.size
        for y in range(1, h - 1):
            for x in range(1, w - 1):
                count = 0
                # 上
                if pixdata[x, y - 1] > 245:
                    count = count + 1
                # 下
                if pixdata[x, y + 1] > 245:
                    count = count + 1
                # 左
                if pixdata[x - 1, y] > 245:
                    count = count + 1
                # 右
                if pixdata[x + 1, y] > 245:
                    count = count + 1
                # 左上
                if pixdata[x - 1, y - 1] > 245:
                    count = count + 1
                # 左下
                if pixdata[x - 1, y + 1] > 245:
                    count = count + 1
                # 右上
                if pixdata[x + 1, y - 1] > 245:
                    count = count + 1
                # 右下
                if pixdata[x + 1, y + 1] > 245:
                    count = count + 1
                if count > 4:
                    pixdata[x, y] = 255
        # 返回处理后图片对象
        return img

    # 传入图片生成图片对象
    img = Image.open('yzm.png')
    # 进行灰度、二值处理,二值范围参数:threshold
    img = binarizing(img, 200)
    # 进行降噪处理
    img = depoint(img)
    # # 打开图片
    # img.show()
    verifiy_code = tesserocr.image_to_text(img)
    # 返回识别结果
    return verifiy_code


def verifiy_liangzhong():
    api_username = 'gxr940301',
    api_password = 'gbt73016.'
    file_name = 'yzm.png'
    api_post_url = "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload"
    yzm_min = ''
    yzm_max = ''
    yzm_type = '1013'
    tools_token = ''
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Connection': 'keep-alive',
        'Host': 'v1-http-api.jsdama.com',
        'Upgrade-Insecure-Requests': '1'
    }
    files = {
        'upload': (file_name, open(file_name, 'rb'), 'image/png')
    }
    data = {
        'user_name': api_username,
        'user_pw': api_password,
        'yzm_minlen': yzm_min,
        'yzm_maxlen': yzm_max,
        'yzmtype_mark': yzm_type,
        'zztool_token': tools_token
    }
    s = requests.session()
    r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False)
    try:
        verifiy_code = json.loads(r.text)['data']['val']
    except Exception as e:
        print('返回结果：%s；失败原因：%s' % (r.text, e))
        verifiy_code = ''

    return verifiy_code
