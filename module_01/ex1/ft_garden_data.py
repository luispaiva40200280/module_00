
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data() -> None:
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    nunber_of_plants = int(input("HOW MANY PLANTS DO YOU WANT TO ADD:: "))
    for plant in range(nunber_of_plants):
        name = input("Enter plant name: ")
        try:
            height = int(input("Enter plant height (in cm): "))
            age = int(input("Enter plant age (in days): "))
        except ValueError:
            print("ERROR: Height and age must be non-negative integers.")
            return
        print(f"\n--- Plant {name} Data Recorded ---\n")
        plant = Plant(name, height, age)
        plants.append(plant)

    print("\n=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height} cm, {plant.age} days")


if __name__ == "__main__":
    ft_garden_data()
