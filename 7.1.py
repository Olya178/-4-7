import random
def check_number():

    numbers_list = [random.randint(1, 100) for _ in range(5)]

    user_number = int(input("Введите число: "))

    if user_number in numbers_list:
        message = "Поздравляю, Вы угадали число!"
    else:
        message = "Нет такого числа!"

    print(f"Исходный список: {numbers_list}")
    print(f"Ваше число: {user_number}")
    print(message)


check_number()