h = int(input("Введите высоту: "))
s = 'I'

for m in range(0,h):
    for n in range(m,h):
        print(" ",end="")
    for i in range(h-(2*m+1),h):
        print(s, end="")
    print("")
