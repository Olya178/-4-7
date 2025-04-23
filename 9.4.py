from PIL import Image, ImageDraw, ImageFont
import os

orig_dir = "D:\\лабы питон\\pythonProject\\лаба 9"
watermark_text = "water"

font_path = "C:\\Windows\\Fonts\\arial.ttf"
font = ImageFont.truetype(font_path, size=50)

for file in os.listdir(orig_dir):
    if file.endswith(".jpg"): #проверяет на что оканчивается документ
        path = os.path.join(orig_dir, file)

        image = Image.open(path).convert("RGBA")

        txt_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)

        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_w = bbox[2] - bbox[0] #координаты правой границы вычитают координаты левой границы
        text_h = bbox[3] - bbox[1] #координаты нижней границы вычитают координаты верхней границы

        x = (image.width - text_w)//2
        y = (image.height - text_h)//2

        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 255))

        watermarked = Image.alpha_composite(image, txt_layer)#объединение текста и знака

        new_file = os.path.join(orig_dir, "wm_" + os.path.splitext(file)[0] + ".png")
        watermarked.save(new_file)

print("Водяные знаки добавлены")

