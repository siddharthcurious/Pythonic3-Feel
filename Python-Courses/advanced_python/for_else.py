for n in range(1, 20):
    if n % 7 == 0:
        print(n)
else:
    print("Look broken")

for i in range(1, 4):
    print(i)
    break
else:
    print("No Break")

print("=====")

count = 0
while (count < 1):
    count = count+1
    print(count)
    break
else:
    print("No Break")