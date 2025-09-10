students = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks of {name}: "))
    
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    students[name] = {"Marks": marks, "Grade": grade}


print("\nStudent Grades:")
print(students)
