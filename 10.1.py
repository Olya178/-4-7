from PIL import Image
import os

image='D:\\лабы питон\\pythonProject\\лаба 9\\открытка.jpg'
path=os.path.dirname(image)
image = Image.open(image)

crop = (150,200,400,500)
crop_image= image.crop(crop)
crop_image.save (os.path.join(path,'crop_image.jpg'))

print("Изображение обработано")