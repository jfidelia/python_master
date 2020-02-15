#Complete the function to print the amount of days it will take to cover a route.
#HINT: You may need to import the math module for this exercise.
from math import ceil

def car_route(n,m):
    print(ceil(m / n))


#Invoke the function with two intergers.
car_route(700,750)