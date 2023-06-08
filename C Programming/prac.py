# import random
# import string
# print("".join(random.choices(string.ascii_letters+string.digits, k=6)))

# a = 4
# b = 6
# c = 8
# d = 8
# if (a == b ) and (c == d):
#     print("yess")

# else:
#     pass

# def x(n):
#     if n == 0:
#         return 1
#     return n * x(n-1)


# print(x(12))

def sum(a):
    if a == 1:
        return 1
    return 1+ sum(a-1)
print(sum(4))