def user():
    try:
        number = int(input("Введите число для деления 100: "))
        result = 100 / number
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: Введите корректное число!")  # ошибка ввод строки вместо числа
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль невозможно!")  # деление на 0
    except Exception as e:
        print(f"Ошибка: {e}")  #  другие исключения
    return None
user()
