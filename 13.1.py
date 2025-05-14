class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' предлагает кухню типа: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' сейчас открыт!")

newRestaurant = Restaurant("Итальянский уголок", "итальянская") # Создание объекта
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

newRestaurant.describe_restaurant()# Вызов методов
newRestaurant.open_restaurant()