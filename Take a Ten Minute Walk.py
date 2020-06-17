def is_valid_walk(walk):
    x=0
    y=0
    for i in walk:
        if i=='n':
            y=y+1
        if i=='s':
            y=y-1
        if i=='w':
            x=x-1
        if i=='e':
            x=x+1
    return (x==0 and y==0 and len(walk)==10)
