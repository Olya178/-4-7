def de(number):
    if number % 3 == 0:
        return "Делится"
    else:
        return "Не делится"
print(de(int(input("Введите число:"))))