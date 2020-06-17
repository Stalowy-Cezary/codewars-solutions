def square_digits(num):
    i =''
    for n in str(num):
        i = i + str((int(n))**2)
    return int(i) 
