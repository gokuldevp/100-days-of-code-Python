#Write your code below this row 👇
last_digit = int(input("Last digit? "))
for call in range(1,last_digit+1):
  if call%3 == 0 and call%5 == 0:
    print("FizzBuzz")
  elif call%5 == 0:
    print("Buzz")
  elif (call%3 == 0):
    print("Fizz")
  else:
    print(call)
