#please write  height countinued by space
# 🚨 Don't change the code below 👇#
student_heights = input("Input a list of student heights .Please write each height continued by a space..\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#First *fork* your copy. Then copy-paste your code below this line 👇
  if n == 0:
    total_student_height = 0
    count = 0
  total_student_height = total_student_height + student_heights[n]
  count = count + 1
  average_height = round(total_student_height/count)
print(average_height)
  #total_height = total_student_height[]
#Finally click "Run" to execute the tests


