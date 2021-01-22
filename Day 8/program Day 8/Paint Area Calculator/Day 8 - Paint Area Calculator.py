# Write your code below this line 👇

def paint_calc(height, width, cover):
    amount_of_paint = height * width / cover
    number_of_cans = round(amount_of_paint)
    if amount_of_paint == number_of_cans:
        pass
    else:
        number_of_cans = int(round(amount_of_paint)+1)

    print(f"You will need {number_of_cans} cans of paint.")

# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall : "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
