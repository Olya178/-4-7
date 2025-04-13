from PIL import Image
file = 'D:\\лабы питон\\pythonProject\\лаба 9\\капибар.jpg'
img = Image.open(file)
img.show()

width, height = img.size
reducedimage = img.resize((int(width / 3), int(height / 3)))
reducedimage.save("D:\\лабы питон\\pythonProject\\лаба 9\\reducedimage.jpg")

horizontalflip = img.transpose(Image.FLIP_LEFT_RIGHT)
horizontalflip.save("D:\\лабы питон\\pythonProject\\лаба 9\\horizontalflip.jpg")

verticalflip = img.transpose(Image.FLIP_TOP_BOTTOM)
verticalflip.save("D:\\лабы питон\\pythonProject\\лаба 9\\verticalflip.jpg")