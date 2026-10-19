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
