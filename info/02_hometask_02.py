HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выход из программы.
"""

# Список задач
tasks = []

today = []
tomorrow = []
other = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":     # Задача Справка
        print(HELP)
    elif command == "show":   # Задача Вывод
        print("Сегодня")
        print(today)
        print("Завтра")
        print(tomorrow)
        print("Другое")
        print(other)
    elif command == "add":    # Задача Добавить
        date = input("Введите дату (Сегодня, Завтра, Другое): ")
        task = input("Введите название задачи: ")
        if date == "Сегодня":
            today.append(task)
        elif date == "Завтра":
            tomorrow.append(task)
        elif date == "Другое":
            other.append(task)
        else:
            print("Неизвестная дата. Попробуйте снова.")
            continue
        #tasks.append(task)
        print("Задача добавлена")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        run = False
    else:
        print("Неизвестная команда")
        break

print("Завершение программы.")
