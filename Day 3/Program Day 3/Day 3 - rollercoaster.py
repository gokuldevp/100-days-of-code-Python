print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster.")
  age = int(input("What is your age? "))
  if age < 12:
      bill = 5
      print(f"Ticket is ${bill}.")
  elif age <18:
      bill = 7
      print(f"Ticket is ${bill}.")
  elif age >= 18 and not range(45,56):
      bill = 12
      print(f"Ticket is ${bill}.")
  else:
      bill = 0
  photo = input("Do you need a photo or not?Yes or No? ")
  photo = photo.lower()
  if age >=18 and range(45,56):
      print(f"you need to pay ${bill}")
  elif photo == "no":
      print(f"You need to pay ${bill}.")
  elif (photo == "yes"):# and (age != range(45,56)):
      pay = bill + 3
      print(f"You need to pay ${pay}.")
#  elif photo == "no" or age == range(45,56):
 #     print(f"You need to pay ${bill}.")
else:
  print("Grow Taller and then come again!")
