"""
*
**
***

*
**
***
****
"""

# n = 4
# for i in range(0, n):
#     if i > 0:
#         a = "*"
#         print(a*i)


n = 4
for i in range(0, n):
    a = ""
    for j in range(0, i+1):
        a += "*"

    print(a)
