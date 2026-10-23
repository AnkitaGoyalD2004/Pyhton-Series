num = int(input("Enter thr number"))
sum_even = 0

for i in range(1, num+1):
    if i%2 == 0:
        sum_even += 1
print("The numbers are: ", sum_even)
