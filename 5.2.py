words = []
while True:
    word = input("Введите слово (или 'stop' для завершения): ")
    if word.lower() == "stop":
        break
    words.append(word)

result = " ".join(words)
print("Результат:", result)
