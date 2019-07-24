import math

year = float(input("输入年份\n"))
is_leap=(year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)
