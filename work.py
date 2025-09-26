"""
num=int(input("Enter a number:"))
#is_number=True
if num>=0:
    print("The number is positive")
    if num %2==0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("negative number")

"""
"""
num1=int(input("ENTER A NUMBER:"))
num2=int(input("ENTER A NUMBER:"))
print("1.addition\n2.sub\n3.multi\n4.division,")
choice=int (input("ENTER A CHOICE :"))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
else:
    print("INVALID NUMBER")
    """
'''
mark=int(input("enter your mark:"))
if mark>=50:
    print("pass")
    if mark>=95:
     print("student passed")     
    elif mark>=90:
     print("A+")
    elif mark>=80:
     print("b grade")
    elif mark>=70:
     print("c grade")
    elif mark>=60:
     print("d grade")

else:
    print("fail")

'''
""""
num=int(input("enter a number :"))
fact=1
for n in range(1,num+1):
    fact=fact*n
    print(fact)

"""

'''

my_list=["Apple","range","green"]
for f in my_list:
    if f[0]=="A" or f[0]=="a":
        print(f)

'''
"""
my_list=["Apple","orange","green"]
for f in my_list:
    if f[0] in "AEIOUaeiou":
        print(f)

"""
"""
count =10
first,second=0,1
for k in range(count):
    print(first,end="")
    third=first+second
    first,second=second,third
    four=first+second
    print(four,end="")

"""


'''number=[5,10,15,20,25]
total=0
for k in number:
    total=total+k
    print("sum=",total)'''

'''numbers=list
total=0
for n in numbers:
    total=total+n
print("sum of =",total)'''




while True:
    num1=int(input("enter first number"))
    num2=int(input("enter the second number"))
    print("1.add\n2.sub\n3.mul\n4.div\n")
    choice=int (input("enter a choice"))
    if choice==1:
        print(num1+num2)
    elif choice==2:
        print(num1-num2)
    elif choice==3:
        print(num1*num2)
    elif choice==4:
        print(num1/num2)
    else:
        print("invalid")

    s=input("do you want to continue (y/n)?")
    if s!="y":
        break









