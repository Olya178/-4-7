def mix_colors(color1, color2):
    all_colors = ("красный", "синий", "желтый")

    secondary_colors = {
        ("красный", "синий"): "фиолетовый",
        ("синий","красный"): "фиолетовый",
        ("красный", "желтый"): "оранжевый",
        ("желтый", "красный"): "оранжевый",
        ("синий", "желтый"): "зеленый",
        ("желтый", "синий"): "зеленый"
    }

    if color1 not in all_colors or color2 not in all_colors:
        return "Ошибка: введены некорректные цвета"
    elif color1 == color2:
        return f"Получился {color1} цвет."
    else:
        return f"При смешивании получается {secondary_colors[(color1, color2)]}"


color1 = input("Введите первый цвет: ").lower()
color2 = input("Введите второй цвет: ").lower()

print(mix_colors(color1, color2))
