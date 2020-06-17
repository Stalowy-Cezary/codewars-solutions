def bouncingBall(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    y = -1
    while h > window:
        h = h * bounce
        y+=2
    return (y)
