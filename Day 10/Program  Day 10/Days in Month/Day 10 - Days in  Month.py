def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    month = month - 1
    day = month_days[month]
    return day


again = True
while again == True:

    year = int(input("\nEnter a year: "))
    month = int(input("\nEnter a month: "))
    if month in range(1,13):
        days = days_in_month(year, month)
        print(f"\nThere are '{days}' days in month {month} and year {year}.")
    else:
        print("\nEnter a valid month!")
    # print(days)
    try_again = input("\nDo You want to try again? 'yes' or 'no? ").lower()
    if try_again == "yes":
        pass
    else:
        again = False
        print("\nPlease come again later!")



