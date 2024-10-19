
# A student grading project using lists of lists
# practice try except blocks

students = [["ALI",1,70,80,90],["REHAN",2,11,22,33],["UMER",3,22,11,441]]
try:
    rollno=int(input("enter roll no."))
    try:
        student = next(student for student in students if student[1] == rollno)
        print(student)
    except StopIteration:
        print("rollno not found")

except ValueError:
    print("rollno should be integer only")
    