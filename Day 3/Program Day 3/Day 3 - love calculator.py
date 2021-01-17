# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
name = name1 + name2
t = name.count("t")
r = name.count("r")
u = name.count("u")
e1 = name.count("e")
true = t+r+u+e1
l = name.count("l")
o = name.count("o")
v = name.count("v")
e2 = name.count("e")
love = l+o+v+e2
love_score = int(str(true)+str(love))
if love_score > 90 or love_score < 10:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score in range(40,51):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
#Finally click "Run" to execute the tests

