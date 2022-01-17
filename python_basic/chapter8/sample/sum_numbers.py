

def sum_all(n):

    result = 0
    for i in range(1, n + 1):
        result += i

    return result

def sum_all2(n):

    result = int((n * (n+1))/2)

    return result 

n = 10
result = sum_all2(n)
print(result)