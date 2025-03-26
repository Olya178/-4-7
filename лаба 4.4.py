def mix_colors(color1, color2):
    all_colors = ("красный", "синий", "желтый")

    # Определяем словарь, где ключ - это множество двух цветов, а значение - полученный цвет
    secondary_colors = {
        frozenset(["красный", "синий"]): "фиолетовый",
        frozenset(["красный", "желтый"]): "оранжевый",
        frozenset(["синий", "желтый"]): "зеленый"
    }

    if color1 not in all_colors or color2 not in all_colors:
        print("Ошибка: введены некорректные цвета")
    elif color1 == color2:
        print(f"Получился {color1} цвет.")
    else:
        print(f"При смешивании получается {secondary_colors[frozenset([color1, color2])]}.")


# Запрашиваем ввод первого цвета у пользователя
color1 = input("Введите первый цвет: ").lower()
# Запрашиваем ввод второго цвета у пользователя
color2 = input("Введите второй цвет: ").lower()

mix_colors(color1, color2)
