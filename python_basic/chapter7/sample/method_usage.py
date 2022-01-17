import math

def add_num(a,b):
    result = a + b
    return result

def minus_num(a,b):
    result = a - b
    return result

def mult_num(a,b):
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

def add_sec(target_time, sec):

    if abs(sec) >= 60:
        print("sec 값 초과")
        return False

    hh = int(target_time[0:2])
    mm = int(target_time[3:5])
    ss = int(target_time[6:8])

    ss += sec
    if sec > 0:
        
        if ss >= 60:
            ss = ss - 60
            mm += 1
        
        if mm >= 60:
            mm = mm - 60
            hh += 1
        
        if hh >= 24:
            hh = hh - 24
    
    else:

        if ss < 0:
            ss = abs(ss + 60)
            mm += -1
            
        if mm < 0:
            mm = abs(mm + 60)
            hh += -1
        
        if hh < 0:
            hh = abs(hh + 24)
    
    hh = str(hh).zfill(2)
    mm = str(mm).zfill(2)
    ss = str(ss).zfill(2)
    result_time = f"{hh}:{mm}:{ss}"
    return result_time

# 
target_time = "23:59:01"
sec = 59

result_time = add_sec(target_time, sec)
print(result_time)