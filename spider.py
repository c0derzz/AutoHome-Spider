# encoding: utf-8
import requests
import re
from bs4 import BeautifulSoup

def getHtml(url):
    matcherObj = re.match(r'[http|https]+://[^\s]*[.com|.cn]',url)
    #正则校验是否是合法的url 非法url不处理
    if matcherObj:
        resp_for_url = requests.get(url)
        if resp_for_url.status_code == 200:
            resp_for_url.encoding = resp_for_url.apparent_encoding
            return resp_for_url.text
        return ""
    else:
        print("unallowable character:",url)

'''
遍历标签
:param htm:html
:param tag_type:标签类型
'''
def forEashTag(htm,tag_type):
    if htm == None or htm == '':
        return "htm 不能为空"
    if htm == None or htm == '':
        return "tag_type 不能为空"
    soup = BeautifulSoup(htm, "html.parser")
    tag_list = soup.find_all(tag_type)
    for tag in tag_list:
        print(tag)
    return tag_list

html = getHtml("http://www.baidu.com")
tags = forEashTag(html,'a')

for tag in tags:
    print(tag.attrs)
