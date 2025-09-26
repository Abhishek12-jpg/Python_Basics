#for loop
"""
a=int(input("enter a number"))
b=int(input("enter the first number"))
c=int(input("enter the second number"))
for i in range(b,c+1):
    if i %a==0:
        print(i)


        """

#while 
'''
num1=int(input("enter 2 numbr"))
num2=int(input("enter a number"))
while num1<=10:
    print(f"{num1}*{num2}={num1*num2}")
'''

#loops
'''
for x in{24,"python","neteam",2.6}:
    print(x)
'''


 #continue and pass and break
"""for num in range(1,11):
    if num==5:
        break
    print(num,end="")

    if True:
        pass
    print("hello")"""

for num in range (1,11):
        if num==3:
            pass
        if num==5:
            continue
        if num==10:
            break
        print(num,end="")
        print("hello")