a = int(input('请输入a的值:'))
b = int(input('请输入b的值:'))
#print('a+b的值为 %d'%(a+b))
#print('a-b的值为 %d'%(a-b))
#print('a*b的值为 %d'%(a*b))
#print('a/b的值为 %d'%(a/b))
def jia(a,b):
    return(a+b)
def jian(a,b):
    return(a-b)
def cheng(a,b):
    return(a*b)
def chu(a,b):
    return(a/b)
c = input('请输入运算符:')
if c == '+' :
    r = jia(a,b)
    print(r)
elif c == '-' :
    r = jian(a,b)
    print(r)
elif c == '*' :
    r = cheng(a,b)
    print(r)
elif c == '/' :
    r = chu(a,b)
    print(r)
