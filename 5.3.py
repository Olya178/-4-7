words = []
while True:
    word = input("Введите слово (или 'stop' для завершения): ")
    if word.lower() == "stop":
        break

    if "ф" in word.lower():
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")
    words.append(word)

result = " ".join(words)
print("Результат:", result)
