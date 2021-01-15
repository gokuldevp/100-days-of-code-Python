#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the Tip Calculator.")
bill = float(input("What is the Bill? $"))
tip = int(input("The Percentage of Tip you are willing to give 10%, 12% or 15%? "))
total = (bill + (bill*tip/100))
people = int(input("Number of people splitting the bill? "))
pay_per_person = total/people
pay_per_person = "{:.2f}".format(pay_per_person)
print(f"Each person should pay : '${pay_per_person}'.")
