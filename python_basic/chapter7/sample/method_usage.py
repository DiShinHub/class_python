import math

def add_num(a,b):
    result = a + b
    return result

def minus_num(a,b):
    result = a - b
    return result

def multi_num(a,b):
    result = a * b
    return result

def div_num(a,b):

    if b == 0:
        print("0으로 나눌 수 없습니다")
        return False

    else:
        result = a / b
        return result

def remove_extension(file_name):

    cut_point = file_name.rfind('.')
    if cut_point > 0 :
        file_name = file_name[:cut_point]

    return file_name


file_name = "test.png"
new_file_name = remove_extension(file_name)
print(new_file_name)