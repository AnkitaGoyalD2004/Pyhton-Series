#tuple is immutable data type in python and we declare it with ()
t = (1, 2, 3, 4, 5)
print(t) # output: (1, 2, 3, 4, 5)

t[0] # output: 1
t[1:3] #output: (2,3)

t[0] = 10 # it will give an error because tuple is immutable data type and we cannot change the value of a tuple once it is created.

len(t) # output: 5 , because there are 5 elements in the tuple.

first_name = ("John", "Doe")
last_name = ("Smith", "Johnson")
full_name = first_name + last_name
print(full_name) # output: ('John', 'Doe', 'Smith', 'Johnson')

last_name = ("goyal" , "gupta" , "bansal")
last_name.count("goyal") #output : 1
last_name.count("dutt") #output : 0