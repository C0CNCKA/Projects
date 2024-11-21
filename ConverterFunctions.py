import math
# основание системы не больше 16!!!
def fromdec(num, base):
    num_ = []
    while num >= base:
        num, r = divmod(num, base)
        if r == 10: r = 'A'
        elif r == 11: r = 'B'
        elif r == 12: r = 'C'
        elif r == 13: r = 'D'
        elif r == 14: r = 'E'
        elif r == 15: r = 'F'
        num_.insert(0, str(r))
    num_.insert(0, str(num))
    return ''.join(num_)

def todec(num, base):
    res = 0
    num = list(str(num))
    num.reverse()
    for i in range(0, len(num)):
        if num[i] == 'A': num[i] = 10
        elif num[i] == 'B': num[i] = 11
        elif num[i] == 'C': num[i] = 12
        elif num[i] == 'D': num[i] = 13
        elif num[i] == 'E': num[i] = 14
        elif num[i] == 'F': num[i] = 15
        else: num[i] = int(num[i])
        res += num[i] * (base**i)
    return res

print(todec(1111011, 2))