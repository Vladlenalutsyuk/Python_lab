def main():
    my_list = []
    while True:
        print("\nМеню:")
        print("1. Добавить элемент в конец списка")
        print("2. Добавить элемент на определённую позицию")
        print("3. Удалить элемент по индексу")
        print("4. Удалить элемент по значению")
        print("5. Показать размер списка")
        print("6. Сортировать список по возрастанию")
        print("7. Сортировать список по убыванию")
        print("8. Вывести список на экран")
        print("9. Выйти")
        
        choice = input("Выберите операцию: ")
        
        if choice == "1":
            element = input("Введите элемент: ")
            my_list.append(element)
            print("Элемент добавлен.")

        elif choice == "2":
            index = int(input("Введите позицию: "))
            element = input("Введите элемент: ")
            my_list.insert(index, element)
            print("Элемент добавлен.")

        elif choice == "3":
            index = int(input("Введите индекс для удаления: "))
            if 0 <= index < len(my_list):
                my_list.pop(index)
                print("Элемент удалён.")
            else:
                print("Ошибка: индекс вне диапазона.")

        elif choice == "4":
            element = input("Введите значение для удаления: ")
            if element in my_list:
                my_list.remove(element)
                print("Элемент удалён.")
            else:
                print("Ошибка: элемент не найден.")

        elif choice == "5":
            print("Размер списка:", len(my_list))

        elif choice == "6":
            my_list.sort()
            print("Список отсортирован по возрастанию.")

        elif choice == "7":
            my_list.sort(reverse=True)
            print("Список отсортирован по убыванию.")

        elif choice == "8":
            print("Текущий список:", my_list)

        elif choice == "9":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: некорректный выбор.")

