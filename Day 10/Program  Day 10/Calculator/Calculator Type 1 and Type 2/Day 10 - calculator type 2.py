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


operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    """recursion of the whole calculation."""
    print(calcart.logo)
    first_number = float(input("\nWhat is the first number : "))
    new_calc = True

    while new_calc:
        print("\n")
        for sign in operators:
            print(f" {sign}")
        operator = input("Which operator to use : ")
        while operator not in operators:
            print("invalid operator")
            for sign in operators:
                print(f" {sign}")
            operator = input("Which operator to use : ")
        second_number = float(input("\nWhat is the next number : "))
        calculation = operators[operator]
        answer = calculation(n1=first_number, n2=second_number)
        final = f"{first_number} {operator} {second_number} = {answer}"
        print(final)
        new_calculation = input(f"\nType 'yes' for new calculator.\nType 'no' for continue with {answer} as first number.\nTyping any thing else to Stop the Calculation.\n").lower()
        if new_calculation == "no":
            first_number = answer
        elif new_calculation == "yes":
            calculator()
        else:
            new_calc = False


calculator()
print("\nThank you for using My simple Calculator Come again later!")
