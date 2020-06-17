def zeros(n): 
    x = 0
    i = 5
    while (n/i>=1): 
        x += int(n/i) 
        i *= 5        
    return int(x)
