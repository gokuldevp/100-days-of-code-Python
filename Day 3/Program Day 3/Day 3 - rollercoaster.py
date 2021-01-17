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
  elif age > 50:
      bill = 0
      print(f"Ticket is ${bill}.")
  elif age >= 18 :
      bill = 12
      print(f"Ticket is ${bill}.")
  photo = input("Do you need a photo or not?Yes or No? ")
  photo = photo.lower()
  if age > 50:
      print(f"you need to pay ${bill}")
  elif photo == "no":
      print(f"You need to pay ${bill}.")
  elif (photo == "yes"):
      pay = bill + 3
      print(f"You need to pay ${pay}.")
else:
  print("Grow Taller and then come again!")
