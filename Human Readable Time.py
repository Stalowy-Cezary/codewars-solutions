def make_readable(seconds):
    SS = 0
    MM = 0
    HH = 0
    for i in range(seconds):
        SS+=1
        if SS == 60:
            SS=0
            MM+=1
            if MM == 60:
                    MM=0
                    HH+=1
    return '{HH}:{MM}:{SS}'.format(HH = "%02d"%HH, MM = "%02d"%MM, SS = "%02d"%SS)
