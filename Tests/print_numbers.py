def abc(x, result=None):
    if result is None:
        result = []

    for n in x:
        if isinstance(n, list):
            abc(n, result)
        else:
            result.append(n)

    return result

r  = abc([[1,2,[3, 4]],[5,6],])
print(r)