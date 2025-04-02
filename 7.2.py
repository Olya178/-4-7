mylist = [1, 2, 3, 4, 5, 6]
uniq = set()
dupl = set()

for element in mylist:
    if element in uniq:
        dupl.add(element)
    else:
        uniq.add(element)

if dupl:
    print("Повторяющиеся элементы:", ', '.join(map(str, dupl)))
else:
    print("Дубликатов нет")