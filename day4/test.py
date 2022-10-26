from lxml import etree

import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'referer': 'https://www.bilibili.com/',
    'Cookie':'innersign=0; buvid3=1583537C-E347-8740-C41B-3106FBF5A8FC90074infoc; b_nut=1666350490; i-wanna-go-back=-1; b_lsid=C53EBE24_183FA3AA7E9; _uuid=C9A1010A79-5F10B-EB8C-A5A1-248EB56344DB91634infoc; buvid4=70210CAF-A710-C15A-DA4A-4BFDF13A48FF91683-022102119-oLBZYf4/EwTl77kGB5W52w%3D%3D; fingerprint=8ead44492a03459cc8dbf7c43e50f8c2; buvid_fp_plain=undefined; SESSDATA=7eec376c%2C1681902525%2C122c0%2Aa2; bili_jct=03023f044694fe2a979f0a2c51a1891a; DedeUserID=593032927; DedeUserID__ckMd5=8187e158cbcdac86; sid=749p75oc; CURRENT_FNVAL=16; buvid_fp=f30f06200b69ba4d266ddd647558ea6c; b_ut=5; nostalgia_conf=-1'}


url = 'https://www.bilibili.com/v/popular/rank/all'

response = requests.get(url, headers=headers, timeout=5)
# 判断是否响应成功
if (response.status_code) == 200:
    # 构造了一个XPath解析对象并对HTML文本进行自动修正。
    html = etree.HTML(response.text)
    # 标题
    title_list = html.xpath('//div[@class="info"]/a/text()')
    # 链接
    link_list = html.xpath('//div[@class="info"]/a/@href')
    # 总评分
    hot_list = html.xpath('//div[@class="pts"]/div/text()')
    # 播放量
    watch_list = html.xpath('//div[@class="detail"]/span[1]/text()')
    # 弹幕量
    barrage_list = html.xpath('//div[@class="detail"]/span[2]/text()')
    # 作者
    author_list = html.xpath('//div[@class="detail"]/a/span/text()')
print(hot_list)