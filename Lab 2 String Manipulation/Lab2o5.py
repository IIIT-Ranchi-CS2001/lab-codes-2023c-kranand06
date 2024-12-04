import math

a=int(input("Enter first coefficient : "))
b=int(input("Enter second coefficient : "))
c=int(input("Enter third coefficient : "))

d=(b*b)-(4*a*c);

if (d==0):
    r=(-1*b)/(2*a)
    print("Both root are real and equal, x = ",r)
    
elif (d>0):
    s=math.sqrt(d)
    r1=((-1*b)+s)/(2*a)
    r2=((-1*b)-s)/(2*a)
    print ("The equation has two distinct real roots, r1 = ",r1," and r2 = ",r2)

else:
    r=(-1*b)/(2*a)
    i=(math.sqrt(-1*d))/(2*a)
    print ("The equation has two complex roots, real part = ",r," and imaginary part = ",i)