import random
correct = 0
mistakes = 0
while mistakes < 3:
    a, b = random.randint(1, 10), random.randint(1, 10)
    answer = int(input(f"{a} + {b} = "))

    if answer == a + b:
        print("Правильно!")
        correct += 1
    else:
        print("Ответ неверный.")
        mistakes += 1

print(f"Игра окончена. Правильных ответов: {correct}")
