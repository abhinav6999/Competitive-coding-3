def is_leap(year):
    leap = False
    if year%400==0 or year%4==0 and year%100!=0:
                return True

    return leap

year = int(input("enter year"))
print( is_leap(year))
