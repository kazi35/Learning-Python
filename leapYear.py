x = input("Entar a year:")
year = int(x)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
             print(year,"is a Leap Year")
        else:
             print(year,"is not a Leap Year")
    else:
        print(year,"is a Leap Year")
else:
    print(year, "is not a Leap Year")
    
    
#Function of Leap Year
def LeapYear(year:int) -> str:
    if year%4 == 0 and year%100 == 0 and year%400 == 0 :
        return print(year, "is a Leap Year!") 
    else:
        return print(year, "is not a Leap Year!")


y=LeapYear(1990)
