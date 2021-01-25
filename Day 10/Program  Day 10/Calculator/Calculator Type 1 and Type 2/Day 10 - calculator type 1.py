import calcart


def add(n1, n2):
    """Add first number with second number and return the value."""
    return n1 + n2


def sub(n1, n2):
    """Subtract first number with second number and return the value."""
    return n1 - n2


def mul(n1, n2):
    """Multiply first number with second number and return the value."""
    return n1 * n2


def div(n1, n2):
    """Divide first number with second number and return the value."""
    return n1 / n2


def result(first_number, second_number):
    """Return the result of operation between first number and second number"""
    if operator == "+":
        calculation = add(n1=first_number, n2=second_number)
    elif operator == "-":
        calculation = sub(n1=first_number, n2=second_number)
    elif operator == "*":
        calculation = mul(n1=first_number, n2=second_number)
    elif operator == "/":
        calculation = div(n1=first_number, n2=second_number)
    else:
        calculation = "\nThe operator is invalid"

    return calculation


calc = True
while calc:
    print(calcart.logo)
    print("\nWelcome to My Simple Calculator!")
    first_number = float(input("\nWhat is the first number : "))
    new_calc = True

    while new_calc:
        operator = input("\nAddition '+'\nSubtraction '-'\nMultiplication '*'\nDivision '/'\n\nWhich operator to use : ")
        second_number = float(input("\nWhat is the next number : "))
        calculation = result(first_number, second_number)
        final = f"{first_number} {operator} {second_number} = {calculation}"
        print(final)
        new_calculation = input("\nstart a new calculation ?Type 'yes' or 'no'? Typing any thing else to EXIT the Calculation : ").lower()
        if new_calculation == "no":
            calc = False
            first_number = calculation
        elif new_calculation == "yes":
            calc = True
            new_calc = False
        else:
            calc = False
            new_calc = False

print("\nThank you for using My simple Calculator Come again later!")
