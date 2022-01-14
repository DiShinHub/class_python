
# set 선언
a = set(['a','b','b'])
print(a)
print(type(a))


a = set([1,2,3,4,5,6,7])
b = set([4,5,6,7,8,9])

# 교집합 
print(a&b)

# 합집합
print(a|b)
print(a.union(b))

# 차집합
print(a-b)

# 값 추가
a = set([1,2,3,4,5,6,7])
print(a)
a.add(8)
print(a)

a = set([1,2,3,4,5,6,7])
print(a)
a.update([8,9,10])
print(a)

# 값 제거
a = set([1,2,3,4,5,6,7])
print(a)
a.remove(7)
print(a)

