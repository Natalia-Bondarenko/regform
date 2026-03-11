HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
"""

# Список задач
tasks = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":     # Задача Справка
        print(HELP)
    elif command == "show":   # Задача Вывод
        print(tasks)
    elif command == "add":    # Задача Добавить
        task = input("Введите название задачи ")
        tasks.append(task)
        print("Задача добавлена")
    else:
        print("Неизвестная команда")
        break

print("Завершение программы.")
