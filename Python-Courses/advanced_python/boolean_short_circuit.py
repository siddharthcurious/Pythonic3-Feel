def short_circuit(data1, data2):
    return isinstance(data1, str) and isinstance(data2, int)

print(short_circuit("sandhyalal", 1))
print(short_circuit("Kumar", "a"))
print(short_circuit(1, "dog"))
