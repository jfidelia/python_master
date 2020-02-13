#Complete the fuction to print the swapped digits of a given two-digit-interger.
def swap_digits(num):
    a = num // 10
    b = num % 10
    c = (b * 10) + a
    print(c)
   
   
   
#Invoke the function with any two digit interger as its argument
swap_digits(92)

