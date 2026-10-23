age = input("provide me an age: ")
age_int = int(age)

if age_int < 13:
    print("Child")
elif age_int < 20:
    print("Teenager")
elif age_int < 59:
    print("Adult")
else:
    print("Senior")