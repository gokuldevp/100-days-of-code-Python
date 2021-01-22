# First *fork* your copy. Then copy-paste your code below this line 👇
# Finally click "Run" to execute the tests
def prime_checker(number):
    count = 0
    for num in range(2, number):
        if number % num == 0 and num != number:
            count += 1
    if count == 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Write your code above this line 👆

# Do NOT change any of the code below👇


n = int(input("Check this number: "))


prime_checker(number=n)
