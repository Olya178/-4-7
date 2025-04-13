from PIL import Image
filepath = '"D:\\лабы питон\\pythonProject\\лаба 9\\капибар.jpg"'
img = Image.open(filepath)
img.show()

print(f'Размер изображения: {img.size}')
print(f'Формат: {img.format}')
print(f'Цветовая модель: {img.mode}')