import math

a = float(input("Первое число: "))
op = input("Действие: ")
b = float(input("Второе число: "))

print("Результат: ", end = '')
if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif (op == "/" or op == "%") and b != 0:
    print(a/b)
elif op == "**" or op == "^":
    print(a**b)
elif op == "root":
    print(a**(1/b))
else:
    print("Что-то пошло не так.")
