N = int(input("Введите количество слов: "))
words = []

for i in range(N):
    word = input(f"Введите слово {i + 1}: ")
    words.append(word) #добавления новых элементов в конец списка

result = " ".join(words) # объединяет слова в одну строку через пробел
print("Результат:", result)