string=input("Enter a string : ")
s=string.split()
b=s[1]
c=b*3
d="Mera "+b;
e=d+" Mahan"
for x in s:
    t=x
    x=x[0].lower()+x[1:].upper()
    print(x,end=" ")
    

print()
print(b)
print(c)
print(d)
print(e)