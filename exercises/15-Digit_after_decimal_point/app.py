#Complete the function to print the first digit to the right of the decimal point.
#Hint: Import the math module.
def first_digit(num):
    print(int(float(num * 10) % 10))


#Invoke the function with a positive real number. ex. 34.33
first_digit(1.79)