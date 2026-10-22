# list is mutable
surname_varities = ["Goyal", "Sharma", "Kumar" , "Gupta"]
print(surname_varities) # output: ['Goyal', 'Sharma', 'Kumar', 'Gupta'] so here we have created a list of surname_varities and printed it.

#0 based indexing 
print(surname_varities[0]) # output: Goyal so here we have accessed the first element of the list using 0 based indexing.
print(surname_varities[-1]) # output: Gupta so here we have accessed the last element of the list using negative indexing.

# we can do slicing in list as well. For eg:
print(surname_varities[0:2]) # output: ['Goyal', 'Sharma'] so here we have accessed the first two elements of the list using slicing. It will return
#we can also do hopping as we did in string
print(surname_varities[0:4:2]) # output: ['Goyal', 'Kumar'] so here we have accessed every 2nd element of the list using slicing with a step of 2.

tea_varities = ["Masala", "Green", "Black", "Lemon"]
print(tea_varities[1:1]) #output : []  

tea_varities[1:1] = ["Ginger"] # so here we have added "Ginger" at index 1 in the list using slicing. It will not replace any element but will add the new element at the specified index.

print(tea_varities) # output: ['Masala', 'Ginger', 'Green', 'Black', 'Lemon'] so here we have printed the list after adding the new element.

for tea in tea_varities:
    print(tea) # output: 
    # Masala
    # Ginger
    # Green
    # Black
    # Lemon so here we have used for loop to iterate through the list and print each element in a new line.

for tea in tea_varities:
    print(tea, end=", ") # output: Masala, Ginger, Green, Black, Lemon, so here we have used end=", " in the print() function which will print each element in a single line separated by a comma and space.

if "Oolang" in tea_varities:
    print("Yes, Oolang is available") # output: Yes, Oolang is available so here we have used if statement to check if "Oolang" is present in the list or not. If it is present then it will print the message.

#if we want to add a new element in the list then we can use append() method. For eg:
tea_varities.append("Oolang") # so here we have added "Oolang" in the list using append() method. It will add the new element at the end of the list.
print(tea_varities) # output: ['Masala', 'Ginger', 'Green', 'Black', 'Lemon', 'Oolang'] so here we have printed the list after adding the new element.

#we have methog pop() which is used to remove the last element from the list. For eg:
tea_varities.pop() # so here we have removed the last element from the list using pop() method. It will remove the last element from the list and return it.
print(tea_varities) # output: ['Masala', 'Ginger', 'Green', 'Black', 'Lemon'] so here we have printed the list after removing the last element.

#if we want to remove a specific element then we can use remove() method. For eg:
tea_varities.remove("Green") #output: ['Masala', 'Ginger', 'Black', 'Lemon'] so here we have removed "Green" from the list using remove() method.

#if we want to insert a new element 
tea_varities.insert(2, "Herbal") # so here we have inserted "Herbal" at index 2 in the list using insert() method. It will add the new element at the specified index and shift the other elements to the right.
print(tea_varities) # output: ['Masala', 'Ginger', 'Herbal', 'Black', 'Lemon'] 

#.copy() method is used to create a copy of the list. Basically with the help of this we have diff reference between the original list and the copied list. For eg:
tea_varities_copy = tea_varities.copy() # so here we have created a copy of the list using copy() method. It will create a new list with the same elements as the original list but with a different reference in memory. So if we change the original list then the copied list will not be affected and vice versa.


#A list comprehension is a short way to build a new list in Python by running an expression and a loop inside a single pair of square brackets
squared_num = [x**2 for x in range(10)]
print(squared_num) # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] so here we have used list comprehension to create a new list of squared numbers from 0 to 9. It will run the expression x**2 for each value of x in the range of 10 and return a new list with the squared values.

