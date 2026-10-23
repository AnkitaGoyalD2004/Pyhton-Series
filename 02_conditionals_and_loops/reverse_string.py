name = "Ankita"
reverse_name = ""
for char in name:
    reverse_name = char + reverse_name
print(reverse_name)   

last_name = "Goyal"
#reverse = last_name[-1:0:-1] #this will exclude 0 so for getting G we have to do something like this
reverse = last_name[-1::-1]
print(reverse)