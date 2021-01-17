# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
pepperoni = 0
cheese = 0
if size == "S":
  pizza = 15
  if add_pepperoni == "Y":
    pepperoni = 2
  if extra_cheese == "Y":
    cheese = 1
elif size == "M":
  pizza = 20
  if add_pepperoni == "Y":
    pepperoni = 3
  if extra_cheese == "Y":
    cheese = 1
elif size == "L":
  pizza = 25
  if add_pepperoni == "Y":
    pepperoni = 3
  if extra_cheese == "Y":
    cheese = 1
else:
  print("?")
bill = pepperoni+cheese+pizza
print(f"Your final bill is: ${bill}.")
#Finally click "Run" to execute the tests


#OR


#print("Welcome to Python Pizza Deliveries!")
#size = input("What size pizza do you want? S, M, or L ")
#add_pepperoni = input("Do you want pepperoni? Y or N ")
#extra_cheese = input("Do you want extra cheese? Y or N ")


#bill = 0

#if size == "S":
#  bill += 15
#elif size == "M":
#  bill += 20
#else:
#  bill += 25

#if add_pepperoni == "Y":
#  if size == "S":
#    bill += 2
#  else:
#    bill += 3

#if extra_cheese == "Y":
#  bill += 1

#print(f"Your final bill is: ${bill}.")

