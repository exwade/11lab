class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")
        print()

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.restaurant_name} обновлен: {self.rating}")

# Создаем экземпляр класса Restaurant
restaurant = Restaurant("Итальянский уголок", "Итальянская кухня", 4.5)

# Выводим информацию о ресторане
restaurant.describe_restaurant()

# Обновляем рейтинг ресторана
restaurant.update_rating(4.8)

# Выводим обновленную информацию о ресторане
restaurant.describe_restaurant()
