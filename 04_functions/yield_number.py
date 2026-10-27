#In Python, a yield statement turns a standard function into a generator, allowing it to return values one at a time and suspend its execution until the next value is requested.

#problem statement:
#Write a generator function that yields even numbers up to a specified limit

def even_gen(limit):
    for i in range(2, limit + 1 , 2):
        print(i)

even_gen(10) #output : 2 ,4 , 6, 8 , 10

#if we want to return
def even_gene(limit):
    for i in range(2, limit + 1 , 2):
        return i

even_gene(11) # this will return 2 only so if we want the whole what else we can do is something likr this :


def even_gen(limit):
    result = []

    for i in range(2, limit + 1, 2):
        result.append(i)

    return result

print(even_gen(10)) # [2, 4, 6, 8, 10] but it is giving me list i donot want list so in python we have one more thing which is called as yield.


def even_generator(limit):
    for i in range(2, limit + 1 , 2):
        yield i
  
for num in even_generator(10):
    print(num) # 2, 4, 6, 8, 10