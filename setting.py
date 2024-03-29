#!/usr/bin/env python
# encoding: utf-8

#  伪装配置
headers = {
    "Accept-Encoding":"gzip",
    "Cache-Control": "max-age=0",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
    "Accept-Language":  "zh-CN,zh;q=0.8,en;q=0.6,en-US;q=0.4,zh-TW;q=0.2",
    "Connection" :  "keep-alive",
    "Accept-Encoding" :  "gzip, deflate",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

# 输出文件路径
file_output = './results/cars.txt'

# 主域名,用于拼接完整URL
domain = "https://www.autohome.com.cn/"
car_domain = "https://www.autohome.com.cn/car/"

# 最开始的品牌入口
start_url = 'http://car.autohome.com.cn/AsLeftMenu/As_LeftListNew.ashx?typeId=1%20&brandId=0%20&fctId=0%20&seriesId=0'

# 每一页下载等待时间
wait_sec = 1