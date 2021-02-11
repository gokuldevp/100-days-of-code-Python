import random

# # creating directory from list
# dict_name = {key: value for item in list}
student_list = ["sanithya", "gopika", "jishnu", "vishnu", "arju", "kashi", "adhul"]
mark_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
student_dict = {students: random.choice(mark_list) for students in student_list}
print(student_dict)

# # creating directory from other directory
# new_dict = {key: value for (key, value) in old_dict.item()}
new_student_dict = {student: marks * 2 for (student, marks) in student_dict.items()}
print(new_student_dict)

# # creating conditional directory comprehension
# new_dict = {key: value for (key, value) in old_dict.item() if test}

passed_students = {student: mark for (student, mark) in new_student_dict.items() if mark >= 60}
print(passed_students)
