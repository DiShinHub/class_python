# 문자열 선언
a = "안녕 나는 코린이야. 아무것도 모르니까 살살 알려줘. 나는 겁쟁이거든."
print(a)

# 카운트
print(a.count("나"))

# 찾기
print(a.find("코"))
print(a.rfind("코"))

print(a.find("ㅋㅋ"))
print(a.rfind("ㅋㅋㅋ"))

# 대소문자
a = "hello world"
print(a.upper())

a = "HELLO world"
print(a.lower())

a = "HELLO world"
print(a.swapcase())

# trip
a = "  hello world "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

# 변환
a = "안녕 나는 코린이야. 아무것도 모르니까 살살 알려줘. 나는 겁쟁이거든."
print(a.replace("겁쟁이", "멋쟁이"))
