print("Welcome To Mark to Grading converter!")

student_scores = {}
student_grades = {}
count = True

while count == True:
    add = input("\nDo you enter a New Student Score? Yes or No?\n").lower()
    if add == "yes":
        name = input("\nEnter the name :  ").upper()
        mark = int(input("\nEnter the mark :  "))
        student_scores[name] = mark
    else:
        count = False
for name in student_scores:
    if student_scores[name] in range(91,101):
        student_grades[name] = "Outstanding"
    elif student_scores[name] in range(81,91):
        student_grades[name] = "Exceeds Expectations"
    elif student_scores[name] in range(71,81):
        student_grades[name] = "Acceptable"
    elif student_scores[name] in range(0,71):
        student_grades[name] = "Fail"
    else:
        student_grades[name] = "** Invalid Score **"

print("\n")
print(student_grades)
