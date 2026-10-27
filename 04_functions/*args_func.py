#Function with *args 
#Problem : Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args): # * this will tell that we can take multiple arguments
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3,4))

#if we want to multiply by 2 then we can do 
def mult(*args):
    for i in args:
     print(i * 2)


(mult(2,5,4,3)) #output: 4,10,8,6

#another problem : We have to craete a function that accepts any number of keyword arguments and prints them in fomat key:value

def print_kwargs(name , age):
   print("Name:" , name , " Age:", age)

print_kwargs("Ankita" , 19)
#but there is one case if i want to pass only one thing like name or age
print_kwargs("Abhay") # in this case it will give me an error and the error is missing 1 required positional argument: 'age'

#so for this case we will do (we use **kwargs)
def print_kwargss(**kwargs):
   for key , value in kwargs.items():
      print(f"{key}: {value}")

print_kwargss(name="Ankita" , age=21 , occ="Engineer") # output is name: Ankita age: 21 , occ: Engineer