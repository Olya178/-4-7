import csv
file_path="покупки.csv"
sum = 0
staf=[]

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[0]
        quantity = int(row[1])
        price = int(row[2])
        sum += quantity * price
        staf.append(f"{product} - {quantity} шт. за {price} руб.")

print("Нужно купить:")
for item in staf:
    print(item)

print(f"Итоговая сумма: {sum} руб.")
