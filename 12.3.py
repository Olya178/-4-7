with open("D:\\лабы питон\\pythonProject\\en-ru.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

ru_en = {}

for line in lines:
    if '-' not in line:
        continue
    en, ru = line.strip().split('-', 1)
    en = en.strip() #убираем пробелы переводы строк с начала и конца строки
    rus_words = [w.strip() for w in ru.split(',')]

    for rw in rus_words:
        if rw not in ru_en:
            ru_en[rw] = []
        ru_en[rw].append(en)

with open("ru-en.txt", "w", encoding="utf-8") as f:
    for ru_word in sorted(ru_en):
        translations = sorted(set(ru_en[ru_word]))  # убираем повторы и сортируем
        f.write(f"{ru_word} – {', '.join(translations)}\n")
print("Файл сохранен")