
days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

num = int(input("Сколько выходных в неделю вы хотите? "))

work = days[:-num]
weekends = days[-num:]

print("Ваши выходные дни:", ", ".join(weekends))
print("Ваши рабочие дни:", ", ".join(work))