'''x = float(input('x='))
f = 0
if x > 1:
    f = 3 * x - 5
if (x >= -1) and (x <= 1):
   f=x+2
if x<-1:
    f=5*x+3
print(f)'''
# value=float(input("请输入长度"))
# unit=input('请输入单位')
# if unit=='in'or unit=='英寸':
#     print('%f英寸 = %f厘米' % (value, value * 2.54))
# elif unit=='cm' or unit=='厘米':
#     print('%f厘米 = %f英寸' % (value, value / 2.54))
# else:
#     print("请输入有效单位")
# from random import randint
# face=randint(1,6)
# if face == 1:
#     result = '唱首歌'
# elif face == 2:
#     result = '跳个舞'
# elif face == 3:
#     result = '学狗叫'
# elif face == 4:
#     result = '做俯卧撑'
# elif face == 5:
#     result = '念绕口令'
# else:
#     result = '讲冷笑话'
# print(result)
# score = float(input("请输入成绩:"))
# if score >= 90:
#     grade = 'A'
# if score >= 80:
#     grade = 'B'
# if score >= 70:
#     grade = 'C'
# if score>=60:
#     grade='D'
# else:
#     grade='E'
# print('对应的等级是:', grade)
# from math import sqrt as s
#
# a = float(input("a="))
# b = float(input('b='))
# c = float(input('c='))
# if a+b>c and a+c>b and b+c>a:
#     print('周长:%f'%(a+b+c))
#     p=(a+b+c)/2
#     area=s(p*(p-a)*(p-b)*(p-c))
#     print('面积%f'%(area))
# else:
#     print('不是三角形')
salary = float(input('本月收入'))
insurance = float(input("五险一金"))
diff = salary - insurance - 5000
if diff <= 0:
    rate = 0
    deduction = 0
elif diff<1500:
    rate=0.03
    deduction=0
elif diff<4500:
    rate=0.1
    deduction=105
elif diff<9000:
    rate=0.2
    deduction=555
elif diff<35000:
    rate=0.25
    deduction=1005
elif diff<55000:
    rate=0.3
    deduction=2755
elif diff<80000:
    rate=0.35
    deduction=5505
else:
    rate=0.45
    deduction=13505
tax=abs(diff*rate-deduction)
print('个人所得税:￥%.2f元' % (tax))
print('实际到手收入:￥%.2f元' % (diff+5000-tax))