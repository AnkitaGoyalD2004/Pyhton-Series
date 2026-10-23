score = int(input("Please enter your score"))

if score >= 101:
    print("please verify your grade")
    exit() # exit() is used for terminate or stop the exec of running script

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")