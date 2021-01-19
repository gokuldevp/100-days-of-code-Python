# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores.Please write each score continued by a space.. ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
highest_score = 0
for score in student_scores:
  if highest_score < score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")
#Finally click "Run" to execute the tests
