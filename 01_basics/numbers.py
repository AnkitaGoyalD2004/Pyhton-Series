x = 2
y = 3
z = x + y

print(z) # output: 5

x = 4
print(z) # output: 5
z = x + y
print(z)  # output: 7

repr('Hello') # output: "'Hello'"
str('Hello') # output: 'Hello'
print('Hello') # output: Hello

#  Command                       | In super simple words
#   -------------------------------|---------------------------------------------------------------------------------
#    print()                       | "Show this on my screen!" (It is an action)
#    str()                         | "Make this friendly for normal people to read."
#    repr()                        | "Show me the secret technical details so I don't get confused as a programmer."

#for eg:

a = 5 
b = '5'

print(a) # output: 5
print(b) # output: 5

# here we donot know the type of a and b. so we can use repr() and str() to know the type of a and b.
print(repr(a)) # output: 5
print(repr(b)) # output: '5'

# common library that we can use is math library. It has many functions that we can use in our code. For eg: sqrt() function is used to find the square root of a number.
import math 

#basically floor will gives us the bottom value of the number. For eg: if we have 3.7 then floor will give us 3 and if we have -3.2 then floor will give us -4. 
math.floor(3.7) # output: 3
math.floor(-3.2) # output: -4

#trunc - basically trunc will give us the value towards zero. For eg: if we have 3.7 then trunc will give us 3 and if we have -3.2 then trunc will give us -3.
math.trunc(3.7) # output: 3
math.trunc(-3.2) # output: -3

#octal numbers 
0o20 # output: 16 so o represents octal number system. 2*8^1 + 0*8^0 = 16
oct(64) # output: '0o100' so oct() function is used to convert decimal number to octal number. 1*8^2 + 0*8^1 + 0*8^0 = 64

#Hexadecimal numbers
0x20 # output: 32 so x represents hexadecimal number system. 2*16^1 + 0*16^0 = 32
hex(32) # output: '0x20' so hex() function is used to convert decimal number to hexadecimal number. 2*16^1 + 0*16^0 = 32

#Binary numbers
0b1000 # output: 8 so b represents binary number system base 2. 1*2^3 + 0*2^2 + 0*2^1 + 0*2^0 = 8
bin(8) # output: '0b1000' so bin() function is used to convert decimal number to binary number. 1*2^3 + 0*2^2 + 0*2^1 + 0*2^0 = 8

###-----------------SETS------------------------

setone = {1, 2, 3, 4, 5}
setone & {3,4} # output : {3, 4} so & operator is used to find the intersection of two sets. It will return the common elements in both sets.
setone | {3,4} # output : {1, 2, 3, 4, 5} so | operator is used to find the union of two sets. It will return all the elements in both sets.

setone - {1,2,3,4,5} # output : set() here we get set() not empty {} because {} is dictionary 

# there is one more thing if we want to check if two variable point to same object in memory then we can use is operator. For eg:

# as we know in most of places we treat true is 1 and false is 0 but in python true is not equal to 1 and false is equal to 0.
print(True == 1) # output: True
print(False == 0) # output: True    

print(True is 1) # output: False because internally True is not equal to 1 and False is not equal to 0. so we can use is operator to check if two variable point to same object in memory or not.
