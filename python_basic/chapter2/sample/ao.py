# 정수형 변수 선언
x = 1
print(x)
print(type(x))

#
x = 1
y = 2


# 더하기
sum_xy = x + y
print(sum_xy)

# 빼기
minus_xy = x - y
print(minus_xy)

# 곱하기
mul_xy = x * y
print(mul_xy)

# 나누기
div_xy = x/y
print(div_xy)

# 실수형 변수 선언
x = 1.1
print(x)
print(type(x))

#
x = 1.5
y = 1.2

# 더하기
sum_xy = x + y
print(sum_xy)

# 빼기
minus_xy = x - y
print(minus_xy)

# 곱하기
mul_xy = x * y
print(mul_xy)

# 나누기
div_xy = x/y
print(div_xy)


# 나누기 (시스템 애러 유발)
x = 1.2
y = 0

div_xy = x/y
print(div_xy)

if y != 0:
    div_xy = x/y
    print(div_xy)

else:
    print("0으로 나눌 수 없습니다.")
