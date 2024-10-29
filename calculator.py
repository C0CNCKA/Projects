a = int(input("Первое число: "))
op = input("Действие: ")
b = int(input("Второе число: "))

print("Результат: ", end = '')
if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif (op == "/" op == or "%") and b != 0:
    print(a/b)
elif op == "**" or op == "^":
    print(a**b)
else:
    print("Что-то пошло не так.")
