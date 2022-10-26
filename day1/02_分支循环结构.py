# 分支语句
#if else 只有两种条件对应的问题
#if elif else  多种条件下对应的问题
# username = input('用户名：')
# password=input('密码：')
# if username == 'admin' and password=='123456':
#     print('身份验证成功！')
# else:
#     print('身份验证失败！')

# 多个条件对应多种结果的情况
# 3x-5（x>1） x+2([-1,1]) 5x+3(x<-1)
# x=float(input('x='))
# if x>1:
#     y=3*x-5
# elif x<-1:
#     y=5*x+3
# else:
#     y=x+2
# print(y)


# score=float(input('分数：'))
# if score<60:
#     print('E')
# elif score>=60 and score<70:
#     print('D')
# elif score>=70 and score<80:
#     print('C')
# elif score>=80 and score<90:
#     print('B')
# else:
#     print('A')
#
# score=float(input('分数：'))
# level="DCBA"
# if score<=60:
#     print('E')
# else:
#     print(level[int(score//10-6)])

# 循环语句
# for in /while
# while 知道循环结束的条件
# start =0
# for x in range(1,101):
#     start+=x
# print(start)

'''
while 条件（True）
    循环体
    break （达到目标条件之后跳出）
'''
import random
answer=random.randint(1,10)
while True:
    number=int(input('猜数字:'))
    if number<answer:
        print('bigger please!')
    elif number>answer:
        print('smaller please!')
    else:
        print('bingo!')
        break






