"""
使用urllib.request请求一个网页内容,并把网页打印出来
"""
from urllib import request
if __name__ == '__main__':
    url = "http://www.bjnews.com.cn"
    # 打开相应url并把相应页面作为返回
    rsp = request.urlopen(url)
    # 把返回结果读取出来
    html = rsp.read()
    # 读取出来的结果类型为bytes,要先解码
    print(html.decode())
