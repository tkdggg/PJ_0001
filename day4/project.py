import requests
from lxml import etree
import csv
import xlwt

def dellist(oldlist):
    new2 = []
    for sam in oldlist:
        new1 = []
        for x in sam:
            if x:
                new1.append(x)
        new2.append(new1)
    newlist = [x for x in new2 if x]
    return newlist

pages = range(1, 3)
cities=['530','531']
list1=[]
for city in cities:
    for page in pages:
        url = f'https://sou.zhaopin.com/?jl={city}&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&p={page}'
        # 第二层伪装，用户身份
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
            'Cookie': 'x-zp-client-id=d23ee8dc-0254-4f6a-8b98-d35975de12f6; acw_tc=2760828316662638634313793e6523e7ac1939efff85cb7b1c87bef6477717; sajssdk_2015_cross_new_user=1; selectCity_search=530; locationInfo_search={%22code%22:%22811%22%2C%22name%22:%22%E5%8D%97%E5%85%85%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1666263887; zp_passport_deepknow_sessionId=d7a19092sd7e0d41a28b886d1d5e35b0f085; at=1fff4ab883c24b899c5a06b21f5da951; rt=050df32997404aa2876f40fa4319f0e6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221150675991%22%2C%22first_id%22%3A%22183f510e3ac6a-0b6f63cd26b2d08-26021f51-1327104-183f510e3ad5d5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgzZjUxMGUzYWM2YS0wYjZmNjNjZDI2YjJkMDgtMjYwMjFmNTEtMTMyNzEwNC0xODNmNTEwZTNhZDVkNSIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjExNTA2NzU5OTEifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221150675991%22%7D%2C%22%24device_id%22%3A%22183f510e3ac6a-0b6f63cd26b2d08-26021f51-1327104-183f510e3ad5d5%22%7D; ZP-ENV-FLAG=gray; sts_deviceid=183f5191b654a3-0ddabf0e3b8392-26021f51-1327104-183f5191b66a0b; ZP_OLD_FLAG=false; sts_sg=1; sts_sid=183f519570e230-019bba19a140d6-26021f51-1327104-183f519570f4b5; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fpassport.zhaopin.com%2F; ZL_REPORT_GLOBAL={%22/resume/new%22:{%22actionid%22:%22504ca0c0-d87b-47b2-a3bd-db90e6be5c23%22%2C%22funczone%22:%22addrsm_ok_rcm%22}}; sts_evtseq=9; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1666264700'}

        resp = requests.get(url=url, headers=headers)
        # 确定编码
        parser = etree.HTMLParser(encoding='utf-8')
        # 将获取的网页源码构造为树对象
        tree = etree.XML(resp.text, parser=parser)

        all_list = tree.xpath('//*[@id="positionList-hook"]/div/div')
        print(len(all_list))

        for all in all_list:
            work = all.xpath('./a/div[1]/div[1]/span/@title')
            com = all.xpath('./a/div[1]/div[2]/span/text()')
            money=all.xpath('./a/div[2]/div[1]/p/text()')          #2.5万-3.5万  · 14薪  需要处理掉14薪

            area = all.xpath('./a/div[2]/div[1]/ul/li[1]/text()')
            quest1=all.xpath('./a/div[2]/div[1]/ul/li[2]/text()')
            quest2 = all.xpath('./a/div[2]/div[1]/ul/li[3]/text()')
            # condition=all.xpath('./div/p[2]/text()')
            # list1.append([title,area,condition[-4:-1],price])
            work_type = all.xpath('./a/div[3]/div[1]/div/text()')
            list1.append([work, com, money, area, quest1,quest2, work_type])
list1=dellist(list1)
for i in list1:
    i[2][0] = i[2][0].strip()

# # csv 逗号分隔符文件
# # 构造csv对象
# # w,文件正常写入
# writer=csv.writer(open('data_proj.csv','w',encoding='utf-8'))
# #写入列名信息
# writer.writerow(['work', 'com', 'money', 'area', 'quest1', 'quest2','work_type'])
# writer.writerows(list1)

#存储为excel文件
# wb=xlwt.Workbook()
# sheet =wb.add_sheet('data')
# titles=('work', 'com', 'money', 'area', 'quest1', 'quest2','work_type')
# # 需要给出三个维度元素（行、列、数值）
# for index,title in enumerate(titles):#将数据系列传入enumerate方法 将会得到数据序列的索引值以及自身数值
#     sheet.write(0,index,title)     # sheet.write(行索引,列索引,自身值)
# for i,item in enumerate(list1):
#     for j,val in enumerate(item):
#         sheet.write(i+1,j,val)
# wb.save('house.xls')

for i in list1:
    print(i)







