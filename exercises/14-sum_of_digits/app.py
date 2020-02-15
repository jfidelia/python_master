#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
    a = num % 1000 // 100
    b = num % 100 // 10
    c = num % 10
    print(a + b + c)




#Invoke the function with any three-digit-number
digits_sum(125)