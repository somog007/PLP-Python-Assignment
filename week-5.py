# Activity 1
class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_mah):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_mah = battery_mah
        self.is_on = False
        self.remaining_storage = storage_gb
        
    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now powered on! ⚡")
        else:
            print("Phone is already on!")
    
    def power_off(self):
        if self.is_on:
            self.is_on = False
            print("Phone is now powered off.")
        else:
            print("Phone is already off!")
    
    def install_app(self, app_name, size_gb):
        if not self.is_on:
            print("Cannot install app - phone is off!")
            return
            
        if self.remaining_storage >= size_gb:
            self.remaining_storage -= size_gb
            print(f"Installed {app_name}! 📲 Remaining storage: {self.remaining_storage}GB")
        else:
            print(f"Not enough storage for {app_name}! Need {size_gb - self.remaining_storage}GB more.")
    
    def check_battery_life(self, usage_hours):
        if not self.is_on:
            return "Battery life unknown - phone is off"
        
        estimated_life = self.battery_mah / (usage_hours * 100)  # Simplified calculation
        return f"Estimated battery life: {estimated_life:.1f} hours with current usage"
    
    def __str__(self):
        return (f"{self.brand} {self.model} | Storage: {self.storage_gb}GB "
                f"| Battery: {self.battery_mah}mAh | Status: {'On' if self.is_on else 'Off'}")
      
# Inheritance example - GamingPhone extends Smartphone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage_gb, battery_mah, gpu_model, cooling_system):
        super().__init__(brand, model, storage_gb, battery_mah)
        self.gpu_model = gpu_model
        self.cooling_system = cooling_system
        self.game_mode = False
    
    def enable_game_mode(self):
        self.game_mode = True
        print("🔥 Game mode activated! Maximum performance enabled!")
    
    def disable_game_mode(self):
        self.game_mode = False
        print("Game mode deactivated.")
    
    def install_app(self, app_name, size_gb):
        # Overriding parent method to add game-specific behavior
        super().install_app(app_name, size_gb)
        if "game" in app_name.lower():
            print("🎮 Game detected! Consider enabling game mode for better performance!")
    
    def __str__(self):
        return (super().__str__() + 
                f" | GPU: {self.gpu_model} | Cooling: {self.cooling_system}")


# Testing the classes
my_phone = Smartphone("Apple", "iPhone 15", 128, 4000)
print(my_phone)
my_phone.power_on()
my_phone.install_app("Instagram", 0.5)
print(my_phone.check_battery_life(2))

gaming_phone = GamingPhone("ASUS", "ROG Phone 6", 256, 6000, "Adreno 660", "Vapor Chamber")
print(gaming_phone)
gaming_phone.power_on()
gaming_phone.install_app("Genshin Impact", 20)
gaming_phone.enable_game_mode()



# Activity 2
class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")
    
    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")


class Dog(Animal):
    def move(self):
        return f"{self.name} the dog is running happily! 🐕"
    
    def speak(self):
        return "Woof! Woof!"


class Fish(Animal):
    def move(self):
        return f"{self.name} the fish is swimming gracefully! 🐠"
    
    def speak(self):
        return "Blub blub..."


class Bird(Animal):
    def move(self):
        return f"{self.name} the bird is flying high! 🦅"
    
    def speak(self):
        return "Tweet tweet!"


class Snake(Animal):
    def move(self):
        return f"{self.name} the snake is slithering silently! 🐍"
    
    def speak(self):
        return "Hiss..."


# Testing polymorphism
animals = [
    Dog("Buddy"),
    Fish("Nemo"),
    Bird("Sky"),
    Snake("Viper")
]

for animal in animals:
    print(animal.move())
    print(animal.speak())
    print()  # Blank line for separation


# Bonus: Vehicle polymorphism example
print("\n--- Vehicle Example ---")

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")


class Car(Vehicle):
    def move(self):
        return "Driving on the road! 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying through the sky! ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing on the water! ⛵"


vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
