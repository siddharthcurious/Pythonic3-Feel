def excel_column_number(column_name):
    letters = [ chr(c) for c in range(ord('A'), ord('Z')+1)]
    numbers = range(1, 27)
    mapping = dict(zip(letters, numbers))

    column_number = 0
    c = 0
    for num in reversed(range(len(column_name))):
        column_number += mapping[column_name[c]]*pow(26, num)
        c = c + 1
    return column_number

if __name__ == "__main__":

    r = excel_column_number("CDA")
    print(r)