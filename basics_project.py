students=[]
def calculate_grade(avg):
    if avg >= 90:
        return "Grade A"
    elif avg >= 80:
        return "Grade B"
    elif avg >= 70:
        return "Grade C"
    else:
        return "Grade F"

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
    grd = calculate_grade(avg)
    



    std["name"]=name
    std['marks']=marks
    std["total"]=total
    std["average"]=avg
    std["grade"]=grd




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
        print("grade : ",s['grade'])
        print("\n---------------------")


def search_student():
    name=input("Enter the name :")
    for st in students:
        if st["name"]==name:
            print("student name:",st['name'])
            print("Mark : ",st['marks'])
            print("Total marks : ",st["total"])
            print("Average : ",st['average'])
            print("grade : ",st['grade'])
            print("\n---------------------")

while True:
    print("1. Add Student\n2. Display All students\n3.Search student\n4.Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        add_student()
    elif choice==2:
        display_students()
    elif choice==3:
        search_student()
    if choice==4:
        break
