def duplicate_count(text):
    text=text.lower()
    a = set([x for x in text if text.count(x) > 1])
    return (len(a))
