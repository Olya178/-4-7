def de(number):
    if number % 3 == 0:
        return "Делится"
    else:
        return "Не делится"
print(de(int(input("Введите число:"))))


def user(num):
    try:
        result = 100 / num
        return f"Результат: {result}"
    except ValueError:
        return "Ошибка: Введите корректное число!"  # ошибка ввод строки вместо числа
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль невозможно!" # деление на 0
    except Exception as e:
        return f"Ошибка: {e}"  #  другие исключения
print (user(int(input("Введите число для деления 100: "))))


def mag(dat):
    dat=dat.split(".")
    return int(dat[0]) * int(dat[1]) == int(dat[2][-2:])
print(mag(input("Введите дату :")))


def num(d):
    d = [int(i) for i in d]
    print(d[:len(d)//2])
    print(d[len(d) // 2:])
    return sum(d[:len(d)//2]) == sum(d[len(d)//2:])
print(num(input("Введите дату :")))
