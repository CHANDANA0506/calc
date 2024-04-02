def add1(a,b):
    return a+b
def sub1(a,b):
    return a-b
def div1(a,b):
    return a/b
def mul(a,b):
    return a*b
a=int(input("enter a number"))
b=int(input("enter a number"))
c=input("input a symbol")
o=0
if(c=='+'):
    o=add1(a,b)
elif (c=='-'):
    o=sub1(a,b)
elif (c=='/'):
    o=div1(a,b)
elif (c=='*'):
    o=mul(a,b)
else:
    print("input incorrect")
print("output value is",o)
