print (str("Задание 1"))
def de(number):
    if number % 3 == 0:
        return "Делится"
    else:
        return "Не делится"
print(de(int(input("Введите число:"))))


print (str("Задание 2"))
def user(num):
    try:
        result = 100 / float(num)
        return f"Результат: {result}"
    except ValueError:
        return "Ошибка: Введите корректное число!"  # ошибка ввод строки вместо числа
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль невозможно!" # деление на 0
print (user(int(input("Введите число для деления на 100: "))))


print (str("Задание 3"))
def mag(dat):
    dat=dat.split(".")
    return int(dat[0]) * int(dat[1]) == int(dat[2][-2:])
print(mag(input("Введите дату :")))


print (str("Задание 4"))
def num(d):
    d = [int(i) for i in d]
    print(d[:len(d)//2])
    print(d[len(d) // 2:])
    return sum(d[:len(d)//2]) == sum(d[len(d)//2:])
print(num(input("Введите число, с четным количеством цифр :")))
