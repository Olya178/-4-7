def user(number):
    try:
        result = 100 / number
        return f"Результат: {result}"
    except ValueError:
        return "Ошибка: Введите корректное число!"  # ошибка ввод строки вместо числа
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль невозможно!" # деление на 0
    except Exception as e:
        return f"Ошибка: {e}"  #  другие исключения
print (user(int(input("Введите число для деления 100: "))))
