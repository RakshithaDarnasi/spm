#1
'''
a=123456789
b=str(a)
print(b)
print(len(b))
c=int(b[::-1])
print(c)
print(type(c))
#or #cutshot method
b=int(str(a)[::-1])#type casting
print(b)
'''
#2
'''
a=('python','saketh',25,'codegnan',36,'mentor',[1,4,5],26)
print(a[1:8:2])
'''
#3
'''
print('a'.join('ppy!'))
'''
#4
'''a = ["I'","work", "i", "Code"]
b = ["am", "ing", "n", "gnan"]
print(a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3])
'''
#5
'''
a=["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
a[-3][-2][-2].extend(['h','j'])
print(a)
'''
#6
'''
a= "Ivis";b="code"
c=a[0]+b[-1]+a[1]+b[-2]+a[2]+b[-3]+a[3]+b[-4]
print(c)
'''
#7
'''
a ="I work in codegnan,and codegnan is in Mangalagiri & i love codegnan"
b=a.count('codegnan')
print(b)
'''
#8
'''
a="Saketh-is-Python-Mentor"
print(a.split('-'))
'''
#9
'''
a = "Python learning am I"
b=a[19]+" "+a[16:18]+" "+a[7:15]+" "+a[0:6]
print(b)
'''
#10
'''
a = "silent"
b=a[2]+a[1]+a[0]+a[5]+a[3]+a[4]
print(b)
'''



















