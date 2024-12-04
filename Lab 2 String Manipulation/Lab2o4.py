name=input("Enter name of student : ")
roll=input("Enter roll no of student : ")
m=int(input("Enter marks of student : "))
gp=0; r="null";
if(m>=90): 
    gp=10; r="OUTSTANDING"
elif(m>=80):
    gp=9
    r="VERY GOOD"
elif(m>=70):
    gp=8
    r="GOOD"
elif(m>=60):
    gp=7
    r="AVERAGE"
elif(m>=50):
    gp=6
    r="PASS"
else:
    gp=0
    r="FAIL"
print("Name : ",name)
print("Roll Number : ",roll)
print("Marks : ",m)
print("Grade Point : ",gp)
print("Remark : ",r)
