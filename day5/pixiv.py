import requests
from lxml import etree
import csv
import xlwt
import sys
import time
from selenium import  webdriver
from  selenium.webdriver.chrome.service import Service
from  selenium.webdriver.edge.service import Service


path = Service( "C:/Users/tkdg/PJ_1/day5/MicrosoftWebDriver.exe")

url = 'https://www.pixiv.net/artworks/100702079'
# 打开谷歌浏览器
'''
executable_path被重构进了service.py中，我们可以实例化一个Service对象来表示浏览器驱动的路径
driver = webdriver.Chrome(executable_path=path)
'''
driver = webdriver.Chrome(executable_path="C:/Users/tkdg/PJ_1/day5/MicrosoftWebDriver.exe")
driver.maximize_window()    #最大化窗口
# 打开主页
driver.get(url)
'''
考虑到网页打开的速度取决于每个人的电脑和网速，
使用time库sleep()方法，让程序睡眠5秒
'''
# time.sleep(5)
'''
调用selenium库中的find_element_by_xpath()方法定位搜索框，
同时使用send_keys()方法在其中输入信息
'''
# driver.find_element_by_xpath('copy你的输入框xpath').send_keys('输入信息')
# time.sleep(2)
# driver.find_element_by_xpath('copy密码框xpath').send_keys('密码')
# time.sleep(2)
'''
调用selenium库中的find_element_by_xpath()方法定位搜索按钮，
同时使用click()方法对按钮进行点击
'''
driver.find_element_by_xpath('鼠标点击的xpath').click()





# list1=[]
# # while list1!=None:
# # 对于翻页，两种情况
# url = 'https://www.pixiv.net/artworks/100702079'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
#     'referer': 'https://www.pixiv.net/',
#     'Cookie':'first_visit_datetime_pc=2022-08-30+17%3A54%3A21; p_ab_id=2; p_ab_id_2=4; p_ab_d_id=1460463370; yuid_b=FEdiNlE; privacy_policy_agreement=5; PHPSESSID=75928517_LGnV6Vx4sPd3YLbp47Ban2PJs4m2HWZ2; c_type=22; privacy_policy_notification=0; a_type=0; b_type=2; __utmz=235335808.1661849765.1.1.utmcsr=accounts.pixiv.net|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=235335808.|3=plan=normal=1^5=gender=female=1^6=user_id=75928517=1^11=lang=zh=1; _fbp=fb.1.1661849777107.522535109; _im_vid=01GBPZW9DAG6564NQNM5KVA699; adr_id=emigWtgxlpm3MnCs6MwjBNgj0CiK4DmpalTC7EnHqWWpg2qu; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; __utmc=235335808; __utma=235335808.708931318.1661849696.1666627851.1666760728.24; __cf_bm=YV19Wigkkhur_qIlrTBT98xjKegWMQIbAyDR2OdrGhU-1666760748-0-AV7hy4GfLRzl0e53sxKgV60uRouTHdH5KglVE28P9aOKCE7s89voJAax0s8/X1hnI/Ip5FNXfe5A6GGJABVtHtl5pinWZyFq5DKvbd45PwBh4LiNJFiTCI14ySqOmtJAlO2b9vYDduY3vS+SkGQC4UpQRNFIYo934YIy/qa852Ib/PpnnG1BozK9xPqSpH/x5A==; _gid=GA1.2.444833879.1666760774; __utmt=1; _ga=GA1.2.708931318.1661849696; __utmb=235335808.12.10.1666760728; tag_view_ranking=_EOd7bsGyl~ziiAzr_h04~0xsDLqCEW6~mLrrjwTHBm~5oPIfUbtd6~dqqWNpq7ul~Lt-oEicbBr~SZJe4DVQ3-~aKhT3n4RHZ~2kSJBy_FeR~-InT1j9djd~dg_40nEhSE~TqiZfKmSCg~MnGbHeuS94~iHzY4dKo2u~1TeQXqAyHD~DchFSjUaxU~RTJMXD26Ak~faHcYIP1U0~PRWMzlhTtT~pzZvureUki~eVxus64GZU~HY55MqmzzQ~BSlt10mdnm~_hSAdpN9rx~s1DI4r3R9d~Ie2c51_4Sp~KMpT0re7Sq~PPlOx6uK-R~OUF2gvwPef~0APtr_pGV6~gnmsbf1SSR~pnCQRVigpy~wmxKAirQ_H~FE9s9RlCMY~azESOjmQSV~NIpEilHR4P~SRs1etnL-l~zyKU3Q5L4C~fSpKMBo2AI~MrfqvAEc07~npWJIbJroU~Weudh4D-vx~tAZXG3M0z-~IpBVNx19zX~F3cbycMFub~0Sds1vVNKR~sAwDH104z0~6-lVM9rI6b~VRuBtwFc6O~VR_7iptpRd~pm5i5dbV3-~CActc_bORM~uW5495Nhg-~VPl-5u9cu6~ToKsH6lBiU~OgLi_QXWK2~tgP8r-gOe_~yjlWcgOFIp~E3iHAAc-OA~rzcxsaPw24~WKQApwRaQn~zJ9HPr_eGC~6nciQgCSzR~kB9dCdAQdc~5VAAx-TfrH~fW51ff7RoH~QjJSYNhDSl~gCB7z_XWkp~CrFcrMFJzz~NFfyoibIwq~rOnsP2Q5UN~JN2fNJ_Ue2~aPdvNeJ_XM~bvp7fCUKNH~vNsVmUxe-K~NaPTSg42YI~HbfqxxCMSP~HZk-7ZdqP6~0xRZYD1xTs~LlXnve21-S~KN7uxuR89w~vxqZQOR3t2~vSWEvTeZc6~iVTmZJMGJj~EhqvooMrEX~NVzV1KfpaO~3IY-LGDpU5~mmsiALpQfe~VfrCXBGpnO~XGIFyGsM9U~4TDL3X7bV9~bvMtpdGkNu~gA6Aw1tmzd~562khdE7He~cbwWM2-ZsP~U-RInt8VSZ~1iqCIV_cwt~cbYABrimU1~xIo4-oSX0_; _ga_75BBYNYN9J=GS1.1.1666760739.27.1.1666761553.0.0.0; cto_bundle=OJUrwF8lMkJyWUIzNmFCemM5cGQybm1OcXhFV0hCSiUyQnlzT2ltYm03cGh0RTZpdXFveFQwOHpkRU8zMGZDTE1vZ2hVSXlUZkhEVVJNR3llWTdQRGtKVEslMkJDa2MwSFNSVUklMkZ1eXJ0ZER2OXlaZ0RmT3p6RCUyQnJSSTBKSW5MaXlzWWJ4aDZjc3FzVmFkVnI3ajZ3S2lXMHp0OWpwaVJnJTNEJTNE',
#     'x-user-id': '75928517'
# }
# resp = requests.get(url=url, headers=headers)
# print(resp.status_code)
    # 确定编码
# parser = etree.HTMLParser(encoding='utf-8')
#
# tree = etree.XML(resp.text, parser=parser)
# all_list = tree.xpath('//*[@id="root"]/div[2]/div/div[2]/div/div[6]/div/section[2]/div[2]/ul/li')
# print(len(all_list))

