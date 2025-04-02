mylist = [1, 2, 3, 4, 4,  5, 6]
uniq = set()
dupl = set()

for element in mylist:
    if element in uniq:
        dupl.add(element)
    else:
        uniq.add(element)

if dupl:
    print("Повторяющиеся элементы:", *dupl)
else:
    print("Дубликатов нет")