def print_capital(func):
    def inner():
        str1 = func()
        str2 = str1.upper()
        return str2
    return inner

def print_str():
    return "Good morning"

p = print_capital(print_str)
print(p())