# 배열의 선언
a = [1, 2, 3, 4, 5]
b = ["안", "녕", "하", "세", "요"]
print(a)
print(b)

# 배열 인덱싱
a = [1, 2, 3, 4, 5]
print(a[4])

# 배열 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[2:])
print(a[:3])
print(a[1:3])


# 배열의 연산
a = [1, 2, 3]
b = [4, 5, 6]

# 더하기
print(a + b)

# 곱하기
print(a * 3)

# 길이
print(len(a))


# 배열의 수정

# 추가
a = [1, 2, 3]
a.append(4)
print(a)

a = [1, 2, 3]
a.insert(0, 10)
print(a)

# 삭제
a = [1, 2, 3]
del(a[1])
print(a)

a = [1, 2, 3]
a.remove(3)
print(a)

a = [1, 2, 3]
a.pop(1)
print(a)

# 갱신
a = [1, 2, 3]
a[1] = 5
print(a)


# 배열의 순서

a = [1, 4, 3, 2]
a.sort()
print(a)

a = [1, 4, 3, 2]
a.sort(reverse=True)
print(a)

a = [1, 4, 3, 2]
a.reverse()
print(a)
