#Complete the function to print the respective number of the century
#HINT: You may need to import the math module.
from math import floor
def century(year):
    if year % 100 == 0:
        print(floor(year/100))
    else:
        year = 100
        new = floor(year)
        print(new + 1)


#Invoke the function with any given year. 
century(1900)