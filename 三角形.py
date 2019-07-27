import math
a = input("请输入第一条边:")
b = input("请输入第二条边:")
c = input("请输入第三条边:")
a = float(a)
b = float(b)
c = float(c)
if a+b>c and b+c>a and a+c>b:
    C =(a+b+c)/2
    A=math.sqrt(C*(C-a)*(C-b)*(C-c)) 
    print("三角形的周长为：",2*C,"三角形的面积为：",A)
else:
    print("不能构成三角形哦！")    