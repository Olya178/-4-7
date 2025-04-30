from PIL import Image, ImageDraw, ImageFont

# Словарь с путями к изображениям
cards = {
    "Новый год": "D:\\лабы питон\\pythonProject\\лаба 9\\new_year.jpg",
    "День рождения": "D:\\лабы питон\\pythonProject\\лаба 9\\открытка.jpg",
    "8 марта": "D:\\лабы питон\\pythonProject\\лаба 9\\march_8.jpg",
    "23 февраля": "D:\\лабы питон\\pythonProject\\лаба 9\\feb_23.jpg"
}

# Ввод данных
holiday = input("К какому празднику Вам нужна открытка? ")
name = input("Кого вы хотите поздравить? ")
# Если праздник найден в словаре
if holiday in cards:
    filename = cards[holiday]

    # Открываем изображение
    image = Image.open(filename).convert("RGB")
    draw = ImageDraw.Draw(image)

    # Подключаем шрифт
    font = ImageFont.truetype("arialbd.ttf", 10)

    # Подготавливаем текст
    text = f"{name}, поздравляю!"

    # Получаем размер текста
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]#координаты правой границы вычитают координаты левой границы
    text_h = bbox[3] - bbox[1]#координаты нижней границы вычитают координаты верхней границы

    # Вычисляем координаты для центрирования текста по горизонтали и размещения внизу
    x = (image.width - text_w) / 2
    y = image.height - text_h - 20

    # Рисуем текст (белый цвет)
    draw.text((x, y), text, font=font, fill=(255, 0, 0))

    # Сохраняем как PNG
    new_name = f"{holiday}_{name}.png"
    image.save(new_name)
    print(f"Открытка сохранена как {new_name}")

else:
    print("Нет открытки для такого праздника.")
