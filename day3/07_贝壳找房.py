import requests
from lxml import etree
import csv
import xlwt

cities=['wh','bj']

pages=range(1,2)
list1=[]
for city in cities:
    for page in pages:
        url = f'https://{city}.zu.ke.com/zufang/pg{page}/#contentList'
        # 第二层伪装，用户身份
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
            'Cookie': 'select_city=510100; lianjia_ssid=13d7f3a0-f60b-4d75-9f87-50e129fbb87a; lianjia_uuid=e51c59be-0240-4e99-adcb-fbfa50cbf515; GUARANTEE_BANNER_SHOW=true; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYmQxNTIyZTQ3NzdhNjEwYjJmMzc1NGY1MjhjMTRmYWJjYTIyYjYwYTA1NjU3YWY5MmZjNDlmYzJmNDgzZDk0NjUxZjMzN2Y2NGUwOTcxYjMyNWYwMjc0MWUxNWQwYjcwNWQ1ZmY2MzRkMGVkOTEzYjdiYzYwMGUwZTc0ZGNkMWVmNTBiNGVmOWQyNWZlNThjNGEwZWZmOGRlYzUxZjVkZWE2ZjM2NTc3MDM3NzE3ZmRkMzBlZjQ3YjEzN2ZiMTc2NjYxNjBmZDU0ODZkYWMzZGIyMTk0MjNhMDFhNzZmZjAyZDRlMzhkZjBjODE2NjUwOTI3NmMzMzVhNWJlZjk0MVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIwNjA0MWRhMlwifSIsInIiOiJodHRwczovL2NkLnp1LmtlLmNvbS96dWZhbmcvcnAxLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9'}

        resp = requests.get(url=url, headers=headers)
        # 确定编码
        parser = etree.HTMLParser(encoding='utf-8')
        # 将获取的网页源码构造为树对象
        tree = etree.XML(resp.text, parser=parser)
        # title=tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/p[1]/a/text()')
        # print(title)
        # price=tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/span/em/text()')
        # print(price)
        # #尝试拿到一整页的标题信息
        # titles=tree.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[1]/a/text()')
        # print(titles)
        # prices=tree.xpath('//*[@id="content"]/div[1]/div[1]/div/div/span/em/text()')
        # print(prices)
        #
        # for i in range(0,len(titles)):
        #     titles[i]=titles[i].strip()
        # print(titles)
        # items=dict(zip(titles,prices))
        # print(items)

        all_list = tree.xpath('//*[@id="content"]/div[1]/div[1]/div')
        print(len(all_list))

        for all in all_list:
            title = all.xpath('./div/p[1]/a/text()')
            price = all.xpath('./div/span/em/text()')
            area = all.xpath('./div/p[2]/a/text()')
            # condition=all.xpath('./div/p[2]/text()')
            # list1.append([title,area,condition[-4:-1],price])
            sift = all.xpath('./div/p[2]/text()[1]')
            if '精选' in sift:
                size = all.xpath('./div/p[2]/text()[7]')
                toword = all.xpath('./div/p[2]/text()[8]')
                huose_type = all.xpath('./div/p[2]/text()[9]')
            else:
                size = all.xpath('./div/p[2]/text()[5]')
                toword = all.xpath('./div/p[2]/text()[6]')
                huose_type = all.xpath('./div/p[2]/text()[7]')
            list1.append([title, price, area, size, toword, huose_type])

        ####   异常捕获  跳过异常情况

for i in list1:
    try:
        i[0][0] = i[0][0].strip()
        i[3][0] = i[3][0].strip()
        i[4][0] = i[4][0].strip()
        i[5][0] = i[5][0].strip()
    except:
        pass
# for i in list1:
#     print(list1)

# # csv 逗号分隔符文件
# # 构造csv对象
# # w,文件正常写入
# writer=csv.writer(open('data.csv','w',encoding='utf-8'))
# #写入列名信息
# writer.writerow(['title', 'price', 'area', 'size', 'toword', 'huose_type'])
# writer.writerows(list1)

#存储为excel文件
# wb=xlwt.Workbook()
# sheet =wb.add_sheet('data')
# titles=('title', 'price', 'area', 'size', 'toword', 'huose_type')
# # 需要给出三个维度元素（行、列、数值）
# for index,title in enumerate(titles):#将数据系列传入enumerate方法 将会得到数据序列的索引值以及自身数值
#     sheet.write(0,index,title)     # sheet.write(行索引,列索引,自身值)
# for i,item in enumerate(list1):
#     for j,val in enumerate(item):
#         sheet.write(i+1,j,val)
# wb.save('house.xls')




