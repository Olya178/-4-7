from PIL import Image
import os

cards = {
    "Новый год": "D:\\лабы питон\\pythonProject\\лаба 9\\new_year.jpg",
    "День рождения": "D:\\лабы питон\\pythonProject\\лаба 9\\открытка.jpg",
    "8 марта": "D:\\лабы питон\\pythonProject\\лаба 9\\march_8.jpg",
    "23 февраля": "D:\\лабы питон\\pythonProject\\лаба 9\\feb_23.jpg"
}

holiday = input("К какому празднику Bам нужна открытка? ")

if holiday in cards:
    filename = cards[holiday]
    if os.path.exists(filename):  # проверяем существует ли файл
        print(f"Открытка для праздника '{holiday}': {filename}")
        image = Image.open(filename)
        image.show()
    else:
        print("Файл с открыткой не найден.")
else:
    print("Открытка для этого праздника не найдена.")