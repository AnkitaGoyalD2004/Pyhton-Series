#dic are mutable, unordered and indexed collection of key-value pairs. Each key is unique and is used to access the corresponding value. Dictionaries are defined using curly braces {} and key-value pairs are separated by colons (:).
# we can create a dictionary using {} or dict() function. For eg:

chai_types = {"masala": "Spicy" , "ginger":"Zesty" , "green":"Healthy" , "black":"Strong"}
print(chai_types) # output: {'masala': 'Spicy', 'ginger': 'Zesty', 'green': 'Healthy', 'black': 'Strong'} so here we have created a dictionary of chai_types and printed it. It will return the dictionary with key-value pairs.

chai_types["masala"] # output: 'Spicy'

#we can change the value of a key in dic
chai_types["masala"] = "Sweet"
print(chai_types) # output: {'masala': 'Sweet', 'ginger': 'Zesty', 'green': 'Healthy', 'black': 'Strong'}


for key in chai_types:
    print(key) # output: 
    # masala
    # ginger
    # green
    # black so here we have used for loop to iterate through the dictionary and print each key in a new line.

for key in chai_types:
    print(key , chai_types[key]) # output:
    # masala Sweet
    # ginger Zesty
    # green Healthy
    # black Strong

#one more way to iterate through the dictionary is to use items() method. For eg:
for key, value in chai_types.items():
    print(key , value) # output:
    # masala Sweet
    # ginger Zesty
    # green Healthy
    # black Strong
if "masala" in chai_types:
    print("Yes") #output : Yes and we can only check the key not the value

print(len(chai_types)) # output: 4 , why ? because there are 4 key-value pairs in the dictionary.


#we can add a new key value pair 
chai_types["Earl Grey"] = "Citrus"
print(chai_types) # output: {'masala': 'Sweet', 'ginger': 'Zesty', 'green': 'Healthy', 'black': 'Strong', 'Earl Grey': 'Citrus'}

#we can pop also but here we have to pass a key
chai_types.pop("Earl Grey")

#if we want to check what we add at last with the help of popitem()

chai_types.popitem() # it will remove the last added key-value pair and return it. In this case it will return ('black', 'Strong') and remove it from the dictionary.

#there is one method which we can use to remove is del keyword actually it will remove the refrence from memory. For eg:
del chai_types["green"] # it will remove the key-value pair with key "green"


tea_shop = {
    "chai": {"masala": "Spicy", "ginger": "Zesty"},
    "tea": {" Earl Grey": "Citrus" , "Green": "Healthy"},
}

print(tea_shop) # output: {'chai': {'masala': 'Spicy', 'ginger': 'Zesty'}, 'tea': {' Earl Grey': 'Citrus', 'Green': 'Healthy'}} so here we have created a nested dictionary where the value of each key is also a dictionary.

print(tea_shop["chai"]["masala"]) # output: Spicy 

squared_num = {x:x**2 for x in range(1,6)}
print(squared_num) # output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} so here we have created a dictionary using dictionary comprehension where the key is the number and the value is the square of the number.

squared_num.clear() # it will remove all the key-value pairs from the dictionary and return an empty dictionary.
print(squared_num) # output: {} 

keys = ["masala", "ginger", "green", "black"]
default_value = "Unknown"
new_dic = dict.fromkeys(keys, default_value) # it will create a new dictionary with the keys from the list and the default value for each key.
print(new_dic) # output: {'masala': 'Unknown', 'ginger': 'Unknown', 'green': 'Unknown', 'black': 'Unknown'}

