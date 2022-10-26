from lxml import etree

xml_str = """
<supermarket>
    <name>永辉超市</name>
    <address>肖家河大厦</address>
    <goodsList>
        <goods name="泡面" price="3.5" count="20"></goods>
        <goods name="矿泉水" price="2" count="50"></goods>
        <goods name="面包" price="5" count="15"></goods>
    </goodsList>
    <worker_list>
        <cashier name="张三" pay="4000"></cashier>
        <shoppingGuide name="李四" pay="3500"></shoppingGuide>
    </worker_list>
    <goods price="50" count="15">
         <name>烟</name>
    </goods>

</supermarket>
"""
#构造树对象，获取数据节点
supermarket=etree.XML(xml_str)
print(supermarket)
#获取标签（获取节点）
#节点对象.xpath(路径表达式) ---根据路径找到对应节点，返回保存节点对象的列表
#a.绝对路径 ：不管xpath前面是什么，都从根节点开始写起
#写法 /绝对路径
cashier=supermarket.xpath('/supermarket/worker_list/cashier')
print(cashier)

worker_list=supermarket.xpath('/supermarket/worker_list')[0]
print(worker_list)
cashier=worker_list.xpath('/supermarket/worker_list/cashier')
print(cashier)
print('------------------------------------')
#b.相对路径
#用. 来表示当前节点，xpath前面是谁，当前节点就是谁
#用..来表示当前节点的上层节点
# 相对路径./可省略
cashier=supermarket.xpath('./worker_list/cashier')
print(cashier)
cashier=worker_list.xpath('./cashier')
print(cashier)
cashier=worker_list.xpath('cashier')
print(cashier)
print('------------------------------------')
# c.// 路径 ----从全局任意位置开始搜索 粗暴简单
#查找方式和xpath前面的的节点没有关系
# cashier=supermarket.xpath('//cashier')
# print(cashier)
# goods=supermarket.xpath('//goods')
# print(goods)
# goods=supermarket.xpath('//goodsList/goods')
# print(goods)
# Lisi=supermarket.xpath('//shoppingGuide')
# print(Lisi)
print('------------------------------------')
# 获取节点内容 (首位标签之中的内容)
# 获取节点路径/text()
name=supermarket.xpath('./name/text()')
print(name)
cigarette=supermarket.xpath('//goods/name/text()')
print(cigarette)

#获取标签属性值
# 语法： 获取节点路径/@属性名
name=supermarket.xpath('./goodsList/goods/@name')
print(name)

price=supermarket.xpath('//goods/@price')
print(price)










