class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' предлагает кухню типа: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' сейчас открыт!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,  flavors=None):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Доступные сорта мороженого:")
        for flavor in self.flavors:
            print(f"– {flavor}")

if __name__ == "__main__":
    ice_cream_cafe = IceCreamStand(
        restaurant_name="Шоколадница",
        cuisine_type="Десертная",
        flavors=["ваниль", "шоколад", "клубника", "мята"]
    )
    ice_cream_cafe.describe_restaurant()
    ice_cream_cafe.open_restaurant()
    ice_cream_cafe.display_flavors()