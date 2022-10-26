# 列表 []
# 可变的数据结构 列表中可以完成 增删改 操作
# 创建列表
# 直接创建
# 使用list方法创建
items2=list(range(1,11))
print(items2)
items3=list('python')
print(items3)
import numpy as np
# 列表的运算符 + -
items4=np.array([1,2,3,4,5,6])
items5=np.array([34,11,1,2,3,4])
items5.reshape(6,1)
items6=['cat']
print(items4+items5)
print(items6*3)
print(items4.dot(items5))
items4=[1,2,3,4,5,6]
print(len(items4))

# 列表的改查
# 列表的索引
items1=['p','c','g','php','j','cpp']
print(items1[0])
items1[2]='go'
print(items1)

#3、查找特定元素的下标位置
print(items1.index('go'))

# 4、列表的切片操作
print(items1[-2:])

# 列表生成式
items2=list(range(1,11))
items=[x for x in range(1,11)]
print(items)

# 字符串 ‘’，“”，""" """
s1='hello world'
s2='你好，世界！'
s3="""hello,
world"""
print(s1+s2)
print(s3)

#字符串的方法
#查找 find 方法，从一个字符串找另一个字符串位置
# print(s1.find('ll'))

#修剪操作 strip()修剪掉字符串元素两边的空格以及换行符
s='    cwnu   \n  '
print(s.strip())

#替换操作
s='hello,world!'
print(s.replace('o','@')) # 全替换
print(s.replace('l','@',2))# 替换两个

# 元组 （） 典型不可变数据结构（不可增删改）
#三元组
# t1=(10,11,12)
# #四元组
# t2=('python',1,2,True)
# t3=('java')
# print(type(t3))
#元组索引方式与列表一致

# 元组的打包和解包操作
# a=1,2,3,4
# print(type(a))
# c=1
# print(type(c))
# # 一元组的建立
# d=(1,)
# print(type(d))
# #解包操作
# #当我们把多个逗号隔开的值赋给一个变量时，多个值会打包成一个元组
# #当我们把一个元组赋值给多个变量时，元组会解包成多个值，然后分别赋值给对应变量
# a=1,2,3,4,5,6,7
# b,c,d,e,f,g,h=a
# print(c)
# print(b,c,d,e)
# #*表达式（解决变量少，赋值多的情况），变量前加*，此变量分配更多的值默认d为列表
# b,*c,d=a
# print(b,c,d)


# 字典  由键值对构成
# {键：值，键：值}
#  字典的创建与使用
# 直接创建
person={'name':'蔡徐坤','age':'24','high':'184','sex':'男','path':'湖南'}
print(person)
# 使用dict函数创建
items1=dict(zip('ABCDE','12345'))
print(items1)

#字典的运算
#字典的成员运算（依据字典中的键）
print('path' in person)  #只能查找键名
#通过索引操作向person字典添加键值对
#还能用于字典的创建
person['tel']='123321'
print(person)
#通过键索引值
print(person['name'])

#字典的方法
#建造嵌套字典
students={
    1001:{'name':'狄仁杰','sex':'男','age':'360','path':'山西大同'},
    1002:{'name':'武则天','sex':'女','age':'365','path':'山西'},
    1003:{'name':'李元芳','sex':'男','age':'335','path':'四川'}
}
#使用get方法获取键对应的值
print(students.get(1002))
print(students[1002])

#获取字典中的键
print(students.keys())
print(students.values())
print(students.items())
for key,values in students.items():
    print(key,'---',values)

stu1=students.pop(1001)
print(students)
print(stu1)







