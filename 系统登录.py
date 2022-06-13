account='wyw'
pwd='123'
for i in range(3):
    zh=input('请输入账号:')
    pd=input('请输入密码:')
    if account==zh and pwd==pd:
       input('恭喜您登录成功...')
        break
        pass

    pass
else:
    print('您的帐号已被系统锁定...')
