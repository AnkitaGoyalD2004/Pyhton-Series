age = input("Enter your age")
age_int = int(age)
day = input("Enter the day:")

if (age_int >= 18 ):
    price = 12
else:
    price = 8

if day.lower() == "wednesday":
    price -=2

print(f"the ticket price is ${price}")
#f -> This is called an f-string in Python. It allows you to insert variables directly into a string using {}.