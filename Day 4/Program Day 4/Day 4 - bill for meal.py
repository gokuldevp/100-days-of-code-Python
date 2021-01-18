# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
len = len(names)
#print(len)
pay = random.randint(0,len-1)
#print(pay)
pay_person = names[pay]
print(f"{pay_person} is going to buy meal today!")
