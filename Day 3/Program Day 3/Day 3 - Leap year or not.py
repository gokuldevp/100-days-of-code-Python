# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
if year%4 == 0:
  if year%100 == 0:
    if year%400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
#Finally click "Run" to execute the tests
