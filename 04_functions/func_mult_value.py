#in this we have to craete a function that return both the area and circumference of a circle given its radius

def area_circum(radius):
    area = 3.14 * (radius ** 2)
    circum = 2 * 3.14 * radius
    return(area , circum)

print(area_circum(8))

import math

def circle_stat(r):
    area = math.pi * (r**2)
    cir = 2 * math.pi * 2