students=[]

def add_student():
    std={}
    name=input("Enter the student name : ")
    marks=[]
    for s in range(1,4):
        mark=int(input(f"Enter the subject {s} : "))
        marks=marks+[mark]
    print(marks)
    
    total=0
    for k in marks:
        total=total+k
    avg=total/3
    std["name"]=name
    std['marks']=marks
    std["total"]=total
    std["average"]=avg

    students.append(std)
    print(students)
    print("Students added successfully")


def display_students():
    print("------- All Students ---------")
    for s in students:
        print("Student name : ",s['name'])
        print("Mark : ",s['marks'])
        print("Total marks : ",s["total"])
        print("Average : ",s['average'])
        print("\n---------------------")
while True:
    print("1. Add Student\n2. Display All students\n3.Search student\n4.Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        add_student()
    elif choice==2:
        display_students()
    if choice==4:
        break