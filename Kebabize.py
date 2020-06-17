def kebabize(string):
    string = ''.join([i for i in string if not i.isdigit()])
    return ''.join(['-' + c.lower() if c.isupper() else c for c in string]).lstrip('-')
