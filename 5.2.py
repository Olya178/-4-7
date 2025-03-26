words = []
while True:
    word = input("Введите слово (или 'stop' для завершения): ")
    if word.lower() == "stop":  # проверка, ввел ли слово стоп или нет
        break
    words.append(word)

result = " ".join(words)
print("Результат:", result)
