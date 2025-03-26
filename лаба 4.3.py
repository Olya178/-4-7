def year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return "Год", y, " — високосный"
    else:
        return "Это год не високосный"
print(year(int(input("Введите номер года:"))))