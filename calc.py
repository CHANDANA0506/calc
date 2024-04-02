import operators as op
a=int(input("enter a number"))
b=int(input("enter a number"))
c=input("input a symbol")
o=0
if(c=='+'):
    o=op.add1(a,b)
elif (c=='-'):
    o=op.sub1(a,b)
elif (c=='/'):
    o=op.div1(a,b)
elif (c=='*'):
    o=op.mul(a,b)
elif (c=='%'):
    o=op.rem(a,b)
else:
    print("input incorrect")
print("output value is",o)
