username = "Ankita" # this is global declaration

# The location where the variable is declared , decides the accessibility of the var .therefore , the scope of var decides where a var can be accessed at.
# The 2 basic scopes of var : local var , global var

def func():
    username = "Dishu"
    print(username)

print(username)
func()

x = 99
def func2(y):
    z = x + y
    print(z)

func2(5) # output is 104 because x we declare is global and we can access that 

def fun3():
    global x # with this we are actually manipulating the x now the x value will be traeted as 12 not 99 anymore
    x = 12

fun3()
print(x)

def fun4():
    z = 4 + x # now the x is treating as 12
    print(z)

fun4() #output : 16

def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1() # this will give me an output of 88 but what if we are not declaring x in f1 then we get 12 because x also decalre globally

#lets discuss clousers now

