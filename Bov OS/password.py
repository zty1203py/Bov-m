import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
from pyfiglet import Figlet
fig = Figlet(font='slant')

ascii_art = fig.renderText('Login')
print(ascii_art)
print('-'*50)
from pyfiglet import Figlet
fig = Figlet(font='slant')

ascii_art = fig.renderText('for')
print(ascii_art)
print('-'*50)
from pyfiglet import Figlet
fig = Figlet(font='slant')

ascii_art = fig.renderText('sign up')
print(ascii_art)
print('-'*50)
print('【登录或注册您的dov OS帐户(1为登录，2为注册）】')
while 1 or 2:
    chiose=eval(input('>>>'))
    if chiose==1:
        for i in range(3):
            name = input('请输入用户名：')
            mima = input('请输入你的密码:')
            if name == 'zty' and mima == '1109':
                print('登录成功！')
                os.system("python system16\BovOSv1.0.py")
                break
                i = 5
            else:
                if i < 2:
                    print('对不起，您还有', 2 - i, '次机会')
            i += 1
        if i == 3:
            print('登录失败！')
            break
    else:
        password=input('请输入您的帐户名称：')
        password1=eval(input('请输入您的帐号密码(开头不能为0）：'))
        password2=eval(input('请确认您的帐号密码：'))
        for i in range(100):
            if password2!=password1:
               print('密码不正确！请重新输入！')
               password2 = eval(input('请确认您的帐号密码：'))
               if password2==password1:
                   print('注册成功！')
                   break
        else:
            print('注册成功！')
            os.system("python system16\BovOSv1.0.py")
            break
