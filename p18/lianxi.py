'''
import random, time
#i = 0
while True:      #i <=1000:
    c = random.randint(1,100)
    print(' '*c,'*'*2)
    #i += 1
    time.sleep(0.1)
'''
'''
import random, time
while True:
    n = random.randint(1,100)
    s = random.randint(1,5)
    print(' '*n,'*'*s)
    time.sleep(0.2)
    '''
a = lambda a,b:a+b
print(a(1,2))
b = lambda a,b:a-b
print(b(4,3))
c = lambda a,b:a*b
print(c(4,7))
d = lambda a,b:a/b
print(d(8,2))
l = [(lambda a:a**2),(lambda b:b/2),(lambda c:c-4)]
print(l[0](2),l[1](8),l[1](8))
d = {'a':(lambda:2*1),'b':(lambda:4-1)}
print(d['a'](),d['b']())
