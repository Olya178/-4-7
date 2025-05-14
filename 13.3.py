class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' предлагает кухню типа: {self.cuisine_type} (Рейтинг: {self.rating}/5)")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' сейчас открыт!")

    def update_rating(self, new_rating):
        if 0 <= new_rating <= 5:
            self.rating = new_rating
            print(f"Рейтинг ресторана '{self.restaurant_name}' обновлён до {self.rating}")
        else:
            print("Ошибка: рейтинг должен быть от 0 до 5.")

restaurant = Restaurant("Круассан", "французская", 4)
restaurant.describe_restaurant()

user_input = float(input("Введите новый рейтинг для ресторана (от 0 до 5): "))
restaurant.update_rating(user_input)
restaurant.describe_restaurant()