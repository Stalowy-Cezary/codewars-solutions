def narcissistic( value ):
    a = [int(x) for x in str(value)]
    z = sum([i**len(str(value)) for i in a])
    return z == value
