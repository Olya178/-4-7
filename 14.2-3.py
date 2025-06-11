import tkinter as tk
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return f"Ресторан '{self.restaurant_name}' предлагает кухню типа: {self.cuisine_type}"

    def open_restaurant(self):
        return f"Ресторан '{self.restaurant_name}' сейчас открыт!"

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, location, opening_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []  # сюда будем складывать все вкусы
        self.location = location
        self.opening_hours = opening_hours
        self.ice_cream_types = {
            "На палочке": [],
            "Станканчик": []
        }

    def add_flavor(self, new_flavor):
        if new_flavor and new_flavor not in self.flavors:
            self.flavors.append(new_flavor)
            return True
        return False

    def remove_flavor(self, flavor_to_remove):
        if flavor_to_remove in self.flavors:
            self.flavors.remove(flavor_to_remove)
            return True
        return False

    def get_all_flavors(self):
        # Возвращает список всех вкусов из общего меню
        return list(self.flavors)

    def add_ice_cream_type(self, ice_cream_type, flavors):
        if ice_cream_type in self.ice_cream_types:
            self.ice_cream_types[ice_cream_type].extend(flavors)
        else:
            print(f"Мороженного типа '{ice_cream_type}' нет в меню.")

    def display_ice_cream_types(self):
        for ice_cream_type, flavors in self.ice_cream_types.items():
            if flavors:
                print(f"\n{ice_cream_type}:")
                for flavor in flavors:
                    print(f"- {flavor}")

    def describe(self):
        print(self.describe_restaurant())
        print(f"Адрес: {self.location}")
        print(f"Время работы: {self.opening_hours}")
        print()



if __name__ == "__main__":
    rest = IceCreamStand(
        "Шоколадница",
        "Десертная",
        "Вознесенский, 44",
        "9:00 - 21:00"
    )

    rest.add_flavor("Шоколадный")
    rest.add_flavor("Ванильный")
    rest.add_flavor("Бабл гам")
    rest.add_ice_cream_type("На палочке", ["Шоколадный", "Бабл гам"])
    rest.add_ice_cream_type("Станканчик", ["Ванильный", "Черничный"])

    rest.describe()
    rest.display_ice_cream_types()


    root = tk.Tk()
    root.title(rest.restaurant_name)

    # Заголовок
    tk.Label(
        root,
        text=f"Приветствуем в кафе «{rest.restaurant_name}»!",
        font=("Arial", 16)
    ).pack(pady=10)

    # Listbox для вкусов
    flavor_listbox = tk.Listbox(root, width=30, height=6)
    flavor_listbox.pack(padx=20)

    def display_ice_cream():
        """Обновляет содержимое listbox """
        flavor_listbox.delete(0, tk.END)
        all_flavors = rest.get_all_flavors()
        if not all_flavors:
            flavor_listbox.insert(tk.END, "(нет вкусов)")
        else:
            for flavor in all_flavors:
                flavor_listbox.insert(tk.END, flavor)

    tk.Button(
        root,
        text="Показать сорта",
        command=display_ice_cream
    ).pack(pady=10)
    root.mainloop()
