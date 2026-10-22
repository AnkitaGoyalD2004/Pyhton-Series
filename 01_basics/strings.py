Name = "Ankita"
print(Name) # output: Ankita

first_char = Name[0]
print(first_char) # output: A

slice_name = Name[0:3]
print(slice_name) # output: Ank

sliced_name = Name[0:4:2]
print(sliced_name) # output: Ak because here 2 represents the step size. so it will take every 2nd character from the string.

slic_name = Name[::2]
print(slic_name) # output:Akt 

#like by mistake we have put space in string eg:
Last_name = " Goyal "
print(Last_name) # output:  Goyal
#we have space in this in the beginning and end of the string. so we can use strip() function to remove the space from the string.
print(Last_name.strip()) # output:Goyal

Full_name = "Ankita Goyal"
print(Full_name.replace("Ankita" , "Dishu")) # output: Dishu Goyal so replace() function is used to replace the string with another string.

chai = "Lemon, Ginger, Masala, Green, Black"
print(chai.split()) # output: ['Lemon,', 'Ginger,', 'Masala,', 'Green,', 'Black'] so split() function is used to split the string into a list of words. By default it will split the string by space but we can also specify the separator. For eg:
print(chai.split(',')) # output: ['Lemon', ' Ginger', ' Masala', ' Green', ' Black'] so here we have specified the separator as comma. so it will

#find() is a built-in string method used to locate the position (index) of the first occurrence of a substring within a given string
print(chai.find("Masala")) # output: 15 so here it will return the index of the first occurrence of the substring "Masala" in the string "chai". If the substring is not found, it will return -1.

Chai = "Masala Chai Chai Chai"
print(Chai.count("Chai")) # output: 3 so here it will return the number of occurrences of the substring "Chai" in the string "Chai". If the substring is not found, it will return 0.

#format method
chai_type = "Masala" 
quantity = 2
order = "I would like to order {} cups of {} chai."
print(order.format(quantity, chai_type)) # output: I would like to order 2 cups of Masala chai. so here we have used format() method to format the string. It will replace the {} with the values passed in the format() method in the order they are passed.


#join() method is used to combine (concatenate) all the elements of an iterable (like a list, tuple, or set) into a single string
Friends = ["Ankita", "Dishu", "Rohit"]
print(", ".join(Friends)) # output: Ankita, Dishu, Rohit
print(" & ".join(Friends)) # output: Ankita & Dishu & Rohit so here we have used join() method to join the elements of the list "Friends" with the separator "&".

#for finding length
print(len(Name)) # output: 6 so here it will return the length of the string "Name". It will count the number of characters in the string including spaces.

#if we want to print every char of a string 
for char in Name:
    print(char) # output: 
    # A
    # n
    # k
    # i
    # t
    # a this is the output we get why in vertical because we have used print() function which will print every char in a new line. If we want to print every char in a single line then we can use end="" in the print() function. For eg:
for char in Name:
    print(char, end="") # output: Ankita so here we have used end="" in the print() function which will print every char in a single line.

#Chaii = "He said "masala chai is awesome" " this will give us error because we have used double quotes inside double quotes. so we can use single quotes inside double quotes or vice versa and also we can use backslash to escape the double quotes. For eg:
Chaii = "He said \"masala chai is awesome\" " # so here we have used backslash to escape the double quotes. so it will not give us error.
print(Chaii) # output: He said "masala chai is awesome"

# so \ is a unicode character which is used to escape the special characters in a string. For eg: \n is used to print a new line .
# for eg: if we wantt to declare some path like c:\Users\Ankita\Desktop\Python-Series then we can use raw string by putting r before the string. For eg:
path = r"c:\Users\Ankita\Desktop\Python-Series"
print(path) # output: c:\Users\Ankita\Desktop\Python-Series 