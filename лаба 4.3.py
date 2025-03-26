y = int(input("Введите номер года:"))
def year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print("Год", y, " — високосный")
    else:
        print("Это год не високосный")
year(y)