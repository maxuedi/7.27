a = input ("请输入用户名:")
b = input ("请输入密码:")
a = str(a)
b = int(b)
if a == "方开":
    if b == 123:
        print("欢迎方开管理员!")
    else:
        print("密码错误")
elif a=="刘晨":
    if b == 12345:
        print("欢迎刘晨管理员!")
    else:
        print("密码错误")
elif a=="张旭":
    if b == 123321:
        print("超级用户")
    else:
        print("密码错误")
elif a=="沈章" or a=="许景":
    if b == 123456:
        print("超级用户")
    else:
        print("密码错误")
else:
    print("访客") 
         


