'''
#一年有多少秒
y = 365
d = 24
h = 60
s = 60
c = y*d*h*s
print('一年有%d秒'%c)
#一公里有多少毫米
#1000米
m = 1000
#1米=10公分
g = 10
#1公分=10厘米
l = 10
#一厘米=10毫米
h = 10
r = m*g*l*h
print('一公里=%d毫米'%r)
'''
'''
x = 2
c = x**2
print(c)
print(6*(x/7))
print(6/(4+5*x))
'''
'''
#个人信息
name = input('请输入您的姓名:')
age = int(input('请输入您的年龄:'))
sex = input('请输入您的性别:')
school = input('请输入您的学校:')
home = input('请输入您的家庭住址:')
shengfen = input('请输入您的省份:')
print('您的姓名是:%s'%name)
print('您的年龄是:%d'%age)
print('您的性别是:%s'%sex)
print('您的学校是:%s'%school)
print('您的家庭住址是:%s'%home)
print('您的省份是:%s'%shengfen)
'''
'''
#公司入职信息
name = input('请输入您的姓名:')
age = int(input('请输入您的年龄:'))
sex = input('请输入您的性别:')
school = input('请输入您的学校:')
home = input('请输入您的家庭住址:')
xueli = input('请输入您的学历:')
hunfuo = input('婚否:')

print('您的姓名是:%s'%name)
print('您的年龄是:%d'%age)
print('您的性别是:%s'%sex)
print('您的家庭住址是:%s'%home)
print('您的学历是:%s'%xueli)
print('婚否:%s'%hunfuo)
'''
'''
y = int(input('请输入年数'))
d = 24
h = 60
s = 60
c = y*365
r = d*h*s*c
print('%d年有%d秒'%(y,r))
'''
UI = int(input('请输入帐号'))
passwd = int(input('请输入密码'))
name = input('请输入姓名')
money = 100000000
m = input('请输入要取的金额')
y = int(money) - int(m)
print('帐号%s'%UI,'密码%d'%passwd,'姓名%s'%name,'原有的金额%s'%money,'要取走的金额%s'%m,'余额%d'%y)
