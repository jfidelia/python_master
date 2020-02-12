#Complete the function to print the next and previous number of a given numner.".
def previous_next(num):

    num = int(input())
    print("The next number for the number " + str(num) + " is " + str(num + 1))
    print("The previous number for the number " + str(num) + " is "  + str(num - 1))




#Invoke the function with any interger at its argument. 
previous_next(3)