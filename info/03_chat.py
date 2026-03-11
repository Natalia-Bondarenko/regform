HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
"""

# Ключ - значение (список)
tasks = {


}

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":     # Задача Справка
        print(HELP)
    elif command == "show":   # Задача Вывод
        date = input("Введите дату для отображения списка задач")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print("Такой даты нет.")
    elif command == "add":    # Задача Добавить
        date = input("Введите дату для добавления задачи:  ")
        task = input("Введите название задачи: ")
        if date in tasks:
            # Дата есть в словаре
            # Добавляем в список задачу
            tasks[date].append(task)
        else:
            # Даты в словаре нет
            # Создаём запись с ключом date
            tasks[date] = []
            tasks[date].append(task)
        print("Задача ", task, " добавлена на дату ", date)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        run = False
    else:
        print("Неизвестная команда")
        break

print("Завершение программы.")
