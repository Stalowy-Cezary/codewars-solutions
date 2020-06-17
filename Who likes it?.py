def likes(names):
    names = list(names)
    if not names:
        return ('no one likes this')
    if len(names) == 1:
        return ('{} likes this'.format(*names))
    if len(names) == 2:
        return ('{} and {} like this'.format(*names))
    if len(names) == 3:
        return ('{}, {} and {} like this'.format(*names))
    if len(names) > 3:
        return ('{}, {} and {numer} others like this'.format(*names, numer=len(names)-2))
