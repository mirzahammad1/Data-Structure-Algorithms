# Q1-- Write a program to find the largest amoung list
print()
list = [23,45,76,97,63,90,234,11]
max = list[0]
for x in list:
    if x > max:
        max = x
print("Largest number is : ",max)
print()

# Q2-- Write a program to check Armstrong number 
sum = 0
num = int(input(" "))
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num , "ARMSTRONG NUMBER")
else:
    print(num , "NOT AN ARMSTRONG NUMBER")
print()

# Q3-- Write a program that reads an intrger between 1 - 12 and print month name
month = int(input(" "))
if month == 1:
    print("JANUARY")
elif month == 2:
    print("FEBRUARY")
elif month == 3:
    print("MARCH")
elif month == 4:
    print("APRIL")
elif month == 5:
    print("MAY")
elif month == 6:
    print("JUNE")
elif month == 7:
    print("JULY")
elif month == 8:
    print("AUGUST")
elif month == 9:
    print("SEPTEMBER")
elif month == 10:
    print("OCTOBER")
elif month == 11:
    print("NOVERMBER")
elif month == 12:
    print("DECEMBER")
else:
    print("WORNG INPUT")
print()

# Q4-- Write a program to check the input is divisble by 5 or not
div_by_5 = int(input(" "))
if div_by_5 % 5 == 0:
    print(div_by_5," DIVISBLE BY 5")
else:
    print(div_by_5," NOT DIVISBLE BY 5")
print()

# Q5-- Write a program to check the year is leap year or not
year = int(input("Enter Year : "))
if (year % 400 == 0) and (year % 100 == 0):
    print(year," LEAP YEAR")
elif (year % 4 == 0) and (year % 100 != 0):
    print(year," LEAP YEAR")
else:
    print(year," NOT A LEAP YEAR")
