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
html = getHtml("http://www.baidu.com")
print(html)
soup = BeautifulSoup(html,"html.parser")
a_list = soup.find_all('a')
for a in a_list:
    print(getHtml(a.get('href')))
