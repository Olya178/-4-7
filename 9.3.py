from PIL import Image, ImageFilter
import os

orig_dir = "D:\\лабы питон\\pythonProject\\лаба 9"
new_dir = "D:\\лабы питон\\pythonProject\\обработано"
file_names = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

# Создаем папку, если она не существует
os.makedirs(new_dir, exist_ok=True)

# Применение фильтра ко всем изображениям
for name in file_names:
    src_path = os.path.join(orig_dir, name)

    # Открываем изображение
    with Image.open(src_path) as img:
        # Применяем фильтр (например, контур)
        filtered = img.filter(ImageFilter.CONTOUR)

        # Сохраняем с новым именем в новую папку
        new_name = f"filtered_{name}"
        dst_path = os.path.join(new_dir, new_name)
        filtered.save(dst_path)

print("Обработка завершена.")
