 def task11():
     class Restaurant:
         def __init__(self, restaurant_name, cuisine_type):
             self.restaurant_name = restaurant_name
             self.cuisine_type = cuisine_type
             self.rating = 0

         def describe_restaurant(self):
             print(f"В ресторане {self.restaurant_name} {self.cuisine_type} кухня.")

         def open_restaurant(self):
             print(f"Ресторан {self.restaurant_name} открыт!")

         def update_rating(self, new_rating):
             self.rating = new_rating
             print(f"Рейтинг ресторана {self.restaurant_name} обновлен: {self.rating}.")


     newRestaurant = Restaurant("Italy", "Итальянская")

     print(f"Название ресторана: {newRestaurant.restaurant_name}")
     print(f"Тип кухни: {newRestaurant.cuisine_type}")
     newRestaurant.describe_restaurant()
     newRestaurant.open_restaurant()

     restaurant1 = Restaurant("Claude Monet", "Французская")
     restaurant2 = Restaurant("Ёбидоёби", "Японская")
     restaurant3 = Restaurant("Mapuche", "Испанская")

     restaurant1.describe_restaurant()
     restaurant2.describe_restaurant()
     restaurant3.describe_restaurant()

     restaurant1.update_rating(4.8)

 task11()
