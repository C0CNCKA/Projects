tasks = []

while True:
    if len(tasks) != 0:
        print(f'\nНевыполненые задачи: ', end="")
        priors = [str(i+1) for i in range(0, len(tasks))]
        for task in tasks:
            i = tasks.index(task)
            if i != len(tasks) - 1:
                print(str(i+1) + ". " + task, end=", ")
            else:
                print(str(i+1) + ". " + task + ".")
        intask = input("Введите название новой задачи или номер одной из задач в списке : ")
    else:
        print("Невыполненых задач нет. Вы молодец!")
        priors = []
        intask = input("Введите название новой задачи: ")
    #print(intask)
    #print(intask.isdigit())
    if str(intask) in (priors) and int(intask) <= len(tasks):
        i = int(intask) - 1
        print(f"Вы выбрали задачу \"{tasks[i]}\". Что вы хотите сделать с задачей?\n(D/del/delete - удалить, E/edit - изменить)")
        op = input()
        if op.lower() == "d" or op.lower() =="del" or op.lower() =="delete":
            tasks.pop(i)
        elif op.lower() == "e" or op.lower() =="edit":
            name = input("Введите новое название для задачи: ")
            tasks[i] = name
        else:
            print("операция введена неправильно")
    elif intask in tasks:
            print("Такая задача уже есть")
    elif intask.isdigit() and int(intask) > len(tasks):
            print("Такой задачи не существует")
    elif priors == []:
        tasks.insert(0, intask)
    else:
        prior = input("Введите приоритет задачи:")
        if prior:
             tasks.insert(int(prior) - 1, intask)
        else:
            tasks.append(intask)

