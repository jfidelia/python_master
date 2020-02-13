#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestamp(hr1,min1,sec1,hr2,min2,sec2):

    print((3600 * int(hr2 - hr1)) + (60 * int(min2 - min1)) + int(sec2 - sec1))


#Invoke the fuction and pass two timestamps(6 intergers) as its argument.
two_timestamp(2,30,37,2,35,38)