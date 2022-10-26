import requests
# requests请求+xpath解析
#请求响应机制
#确定目标页面 确定url:网络统一资源标识符
url='https://www.baidu.com/'
# 目标服务器开启了反爬机制
# 为了破解对方服务器的反爬机制，给我们发出的请求加上伪装
# 加上第一层伪装，浏览器的身份
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'}
resp=requests.get(url=url.strip(),headers=headers)#发送请求，用resp接收
# print(resp.text)
# 解决乱码问题
# resp=resp.content.decode('utf-8')
# print(resp)
#查看状态码
print(resp.status_code)
'''
状态码
200：大概率可以访问到该服务器
404：网页丢失
500：服务器错误
403：服务器发现爬虫
406：无法解析服务端返回内容
'''

