
from PIL import Image
import os

filepath = 'D:\\лабы питон\\pythonProject\\лаба 9'

def image_file(filename):
    return filename.lower().endswith(('.png', '.jpg'))

for file in os.listdir(filepath):
    if image_file(file):
        fil = os.path.join(filepath, file)
        try:
            img = Image.open(fil)

            print(f'Файл: {file}')
            print(f'Размер изображения: {img.size}')
            print(f'Формат: {img.format}')
            print(f'Цветовая модель: {img.mode}')
            print('---')

        except Exception as e:
            print(f'Не удалось открыть {file}: {e}')
