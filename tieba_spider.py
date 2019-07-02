import requests
import re
from bs4 import BeautifulSoup

def getHtml(url):
    try:
        matcherObj = re.match(r'[http|https]+://[^\s]*[.com|.cn]', url)
        # 正则校验是否是合法的url 非法url不处理
        if matcherObj:
            resp_for_url = requests.get(url)
            if resp_for_url.status_code == 200:
                resp_for_url.encoding = resp_for_url.apparent_encoding
                return resp_for_url.text
            return ""
        else:
            print("unallowable character:", url)
    except:
        return "ERROR"

def get_content(url):
    #存放贴子各层楼
    contexts=[]

    html=getHtml(url)
    soup = BeautifulSoup(html,'lxml')
    divTags = soup.find_all("div",attrs={'class':'l_post l_post_bright j_l_post clearfix'})

    for divTag in divTags:
        context = divTag.find("div",attrs={'class','d_post_content j_d_post_content'})
        print(context.prettify())
        ct={}
        ct['id']= context['id']
        ct['content'] = context.text
        contexts.append(ct)
    print(contexts)


tieba_url = "https://tieba.baidu.com/p/6180444594?pn=1"

get_content(tieba_url)