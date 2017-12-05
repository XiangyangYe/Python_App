# import urllib.request
from urllib import request
import chardet                                         #自动判断编码

if __name__ == "__main__":
    response = request.urlopen("http://www.baidu.com")
    html = response.read()
    # charset = chardet.detect(html)					#判断网页是何种编码
    # print(charset)
    html = html.decode("utf-8")
    print(html)