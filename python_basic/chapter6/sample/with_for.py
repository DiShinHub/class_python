
# 튜플 선언
a = (1,2,3)

# 튜플 with for 
for data in a:
    print(data)

# set 선언
b = set(['a','b','b'])

# set with for
for data in b:
    print(data)

# dict 선언
c = {
    "a" : 1,
    "b" : 2,
}

# for data in c:
#     print(data)

for idx, key in enumerate(c):
    print(f"key :{key}, data :{c[key]}")

"""
2. enumerate 함수
리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가집니다.
enumerate는 “열거하다”라는 뜻입니다.
이 함수는 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴합니다.
보통 enumerate 함수는 for문과 함께 자주 사용됩니다.
"""
