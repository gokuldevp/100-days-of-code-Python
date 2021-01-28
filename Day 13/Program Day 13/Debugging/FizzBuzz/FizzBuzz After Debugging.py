for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:        #use 'and' dont use 'or'
    print("FizzBuzz")
  elif number % 3 == 0:                          #should use elif
    print("Fizz")
  elif number % 5 == 0:                          #should use elif
    print("Buzz")
  else:
    print(number)                                #dont need to use [] it is number not string