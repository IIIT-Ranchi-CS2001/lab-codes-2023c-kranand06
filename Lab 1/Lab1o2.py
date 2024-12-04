import math

a=int(input("Enter first side "))
b=int(input("Enter second side "))
c=int(input("Enter third side "))

s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))

print("Area of triangle : ",area)
print("Perimeter of triangle : ",(a+b+c))

C=round(math.degrees(math.acos(((a*a)+(b*b)-(c*c)) / (2*a*b))))
A=round(math.degrees(math.acos(((c*c)+(b*b)-(a*a)) / (2*c*b))))
B=round(math.degrees(math.acos(((a*a)+(c*c)-(b*b)) / (2*a*c)))) 

print("Angle of the triangles are : ",A,", ",B," and ",C)