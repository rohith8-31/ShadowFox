class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
    
    def get_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nSuper Power: {self.super_power}\nWeapon: {self.weapon}"
    
    def is_leader(self):
        return self.name == "Captain America"  # Assuming Captain America is the leader

# Creating Avengers
avengers = [
    Avenger("Captain America", 100, "Male", "Super strength", "Shield"),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 42, "Male", "Fighting skills", "Bow and Arrows")
]

# Displaying information
print("Avengers Team Information:")
print("-" * 50)
for avenger in avengers:
    print(avenger.get_info())
    print(f"Leader: {'Yes' if avenger.is_leader() else 'No'}")
    print("-" * 50)