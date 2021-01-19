#Write your code below this row 👇
last_digit = int(input("Up to which number do you want to find sum of even number of?\n"))
total_of_even = 0
for total in range(2,last_digit+1,2):
  total_of_even = total + total_of_even
print(f"The sum of even less than or equal to {last_digit} is {total_of_even}")
