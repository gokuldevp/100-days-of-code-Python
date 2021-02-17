import datetime as dt

# from datetime library we use datetime class
now = dt.datetime.now()
date_of_birth = dt.datetime(year=1997, month=8, day=9)
print(now)
if now.year == 2021:
    print(now.year - date_of_birth.year)
    print(now-date_of_birth)
