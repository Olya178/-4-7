import json
with open ("D:\\лабы питон\\pythonProject\\продукты 2.json", "r", encoding = "utf-8") as file:
    data=json.load(file)
name = input("Введите название продукта: ")
price = int(input("Введите цену продукта: "))
weight = int(input("Введите вес продукта: "))
available_input = input("Есть ли товар в наличии? (да/нет): ")

data["products"].append({
    "name": name,
    "price": price,
    "weight": weight,
    "available":available_input
})
with open("products.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2) #записываем измененные данные в документ в строки

for product in data["products"]:
    print(f"\nНазвание: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")

    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()