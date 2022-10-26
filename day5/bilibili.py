import requests
from lxml import etree
import csv
import xlwt
from selenium import webdriver

list1=[]
# while list1!=None:
# 对于翻页，两种情况
url = 'https://search.bilibili.com/all?keyword=%E5%8E%9F%E7%A5%9E&from_source=webtop_search&spm_id_from=333.1007&search_source=5&page=2&o=30'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'referer': 'https://www.bilibili.com/',
    'Cookie':'innersign=0; buvid3=1583537C-E347-8740-C41B-3106FBF5A8FC90074infoc; b_nut=1666350490; i-wanna-go-back=-1; b_lsid=C53EBE24_183FA3AA7E9; _uuid=C9A1010A79-5F10B-EB8C-A5A1-248EB56344DB91634infoc; buvid4=70210CAF-A710-C15A-DA4A-4BFDF13A48FF91683-022102119-oLBZYf4/EwTl77kGB5W52w%3D%3D; fingerprint=8ead44492a03459cc8dbf7c43e50f8c2; buvid_fp_plain=undefined; SESSDATA=7eec376c%2C1681902525%2C122c0%2Aa2; bili_jct=03023f044694fe2a979f0a2c51a1891a; DedeUserID=593032927; DedeUserID__ckMd5=8187e158cbcdac86; sid=749p75oc; CURRENT_FNVAL=16; buvid_fp=f30f06200b69ba4d266ddd647558ea6c; b_ut=5; nostalgia_conf=-1'}

resp = requests.get(url=url, headers=headers,timeout=5)
print(resp)
    # 确定编码
parser = etree.HTMLParser(encoding='utf-8')

tree = etree.XML(resp.text, parser=parser)
all_list = tree.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div[1]/div')
print(len(all_list))
for all in all_list:
    title = all.xpath('./div/div[2]/div/div/a/h3/@title')
    time = all.xpath('./div/div[2]/div/div/p/a/span[2]/text()')
    play_num = all.xpath('./div/div[2]/a/div/div[2]/div/div/span[1]/span/text()')  #
    uper = all.xpath('./div/div[2]/div/div/p/a/span[1]/text()')  # up主
    # tag = all.xpath('./a/div[2]/div[1]/ul/li[2]/text()')
    # list1.append([title, time, play_num, uper, tag])
    list1.append([title, time, play_num, uper])

for i in list1:
    print(i)

# add_argument("headless")
#
#
# from selenium.webdriver.common.by import By
# option = webdriver.Edge
# option.add_argument("headless")
# # 这里适用Edge浏览器
# driver = webdriver.Edge(options=option)
# driver.get("https://www.pixiv.net/artworks/102123185")
# html_page = driver.page_source
# print(html_page)
#
#
# from selenium import webdriver
# driver=webdriver.Edge()
# driver.maximize_window()
# driver.get('https://cn.bing.com/')

#
#
# dirver = webdriver.Chrome(executable_path=r'C:\Users\tkdg\PJ_1\day5\chromedriver.exe')
# dirver.get('https://www.pixiv.net/artworks/102123185')    #加载url
# count = 1    #执行次
# response = dirver.page_source    #获取网页源码
# html_str = etree.HTML(response)    #HTML格式展示
