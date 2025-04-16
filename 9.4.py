from PIL import Image, ImageDraw, ImageFont
import os

folder = "D:\\лабы питон\\pythonProject\\лаба 9"
watermark_text = "АИП"

font = ImageFont.load_default()

for file in os.listdir(folder):
    if file.endswith(".jpg"):
        path = os.path.join(folder, file)

        image = Image.open(path).convert("RGBA")

        txt_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)

        text_w, text_h = draw.textsize(watermark_text, font)
        x = (image.width - text_w) // 2
        y = (image.height - text_h) // 2

        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 255))


        watermarked = Image.alpha_composite(image, txt_layer)        # объединяем изображение и текстовый слой

        # Сохраняем как PNG
        new_file = os.path.join(folder, "wm_" + os.path.splitext(file)[0] + ".png")
        watermarked.save(new_file)

print("Готово! Водяные знаки добавлены в центр (без прозрачности).")
