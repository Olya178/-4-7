from PIL import Image, ImageFilter
import os

orig_dir = "D:\\лабы питон\\pythonProject\\лаба 9"
new_dir = "D:\\лабы питон\\pythonProject\\обработано"
file_names = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

for name in file_names:
    orig_path = os.path.join(orig_dir, name)
    img = Image.open(orig_path)
    filtered = img.filter(ImageFilter.CONTOUR)
    new_name = f"filtered_{name}"
    new_path = os.path.join(new_dir, new_name)
    filtered.save(new_path)
    img.close()

print("Обработка завершена.")
