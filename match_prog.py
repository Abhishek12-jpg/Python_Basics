num1=int(input("enter a number"))
num2=int(input("enter a numnber"))
print("1.add\n2.sub\n3.multi\n4.div")
choice=int(input("enter your choice"))
match choice:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)
    case __:
        print("invalid")

