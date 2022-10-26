import requests

url='https://cd.zu.ke.com/zufang/pg1/#contentList'
# 第二层伪装，用户身份
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
         'Cookie':'select_city=510100; lianjia_ssid=13d7f3a0-f60b-4d75-9f87-50e129fbb87a; lianjia_uuid=e51c59be-0240-4e99-adcb-fbfa50cbf515; GUARANTEE_BANNER_SHOW=true; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYmQxNTIyZTQ3NzdhNjEwYjJmMzc1NGY1MjhjMTRmYWJjYTIyYjYwYTA1NjU3YWY5MmZjNDlmYzJmNDgzZDk0NjUxZjMzN2Y2NGUwOTcxYjMyNWYwMjc0MWUxNWQwYjcwNWQ1ZmY2MzRkMGVkOTEzYjdiYzYwMGUwZTc0ZGNkMWVmNTBiNGVmOWQyNWZlNThjNGEwZWZmOGRlYzUxZjVkZWE2ZjM2NTc3MDM3NzE3ZmRkMzBlZjQ3YjEzN2ZiMTc2NjYxNjBmZDU0ODZkYWMzZGIyMTk0MjNhMDFhNzZmZjAyZDRlMzhkZjBjODE2NjUwOTI3NmMzMzVhNWJlZjk0MVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIwNjA0MWRhMlwifSIsInIiOiJodHRwczovL2NkLnp1LmtlLmNvbS96dWZhbmcvcnAxLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9'}

resp=requests.get(url=url,headers=headers)
print(resp.text)

import lxml



