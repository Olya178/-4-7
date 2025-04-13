from PIL import Image, ImageDraw, ImageFont
import os

# Папка с изображениями
folder = "images"  # замени на нужную папку

# Текст водяного знака
watermark = "© MyWatermark"

# Проходим по всем JPG-файлам в папке
for filename in os.listdir(folder):
    if filename.endswith(".jpg"):
        path = os.path.join(folder, filename)
        image = Image.open(path)
        draw = ImageDraw.Draw(image)

        # Используем встроенный шрифт
        font = ImageFont.load_default()

        # Позиция водяного знака (правый нижний угол)
        text_width, text_height = draw.textsize(watermark, font)
        x = image.width - text_width - 10
        y = image.height - text_height - 10

        # Добавляем текст
        draw.text((x, y), watermark, font=font, fill=(255, 255, 255))

        # Сохраняем в той же папке с новым именем
        new_name = "wm_" + filename
        new_path = os.path.join(folder, new_name)
        image.save(new_path)

print("Водяные знаки добавлены.")