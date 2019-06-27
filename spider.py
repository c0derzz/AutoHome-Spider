# encoding: utf-8
import requests
import setting
from bs4 import BeautifulSoup

resp = requests.get("http://www.baidu.com")
resp.encoding = resp.apparent_encoding
print(resp.apparent_encoding)
print(resp.encoding)
html = resp.text
print("获取的结果为:",resp.content)

soup = BeautifulSoup(html,"html.parser")

print(soup.prettify())
print(soup.find_all('a'))