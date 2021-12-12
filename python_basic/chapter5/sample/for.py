for i in range(0, 10):
    print(i)


a = 0
result = []
for i in range(10):
    for j in range(10):
        a += 1
        result.append(a)

print(result)


a = 0
result = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            a += 1
            result.append(a)

print(result)
