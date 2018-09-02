def multiply_by_2(x):
    return 2*x

x = 1
x = multiply_by_2(x)
print(x)

def change(x):
    x[0] = 3

x = [1]
change(x)
print(x)