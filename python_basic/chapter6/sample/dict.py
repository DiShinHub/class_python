
# dict 선언
data_dict = {
    "a" : 1,
    "b" : 2,
}
print(data_dict)
print(type(data_dict))

# dict 요소 사용
print(data_dict["a"])

# dict 추가
data_dict["c"] = 3
print(data_dict)

# dict 변경
data_dict["b"] = 15
print(data_dict)

# dict 삭제
del(data_dict["a"])
print(data_dict)