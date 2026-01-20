
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory() -> None:
    plants = []
    nunber_of_plants = int(input("HOW MANY PLANTS DO YOU WANT TO CREATE:: "))
    for plant in range(nunber_of_plants):
        name = input("Enter plant name: ")
        try:
            height = int(input("Enter plant height (in cm): "))
            age = int(input("Enter plant age (in days): "))
        except ValueError:
            print("ERROR: Height and age must be non-negative integers.")
            return
        print(f"\n--- Plant {name} Created ---\n")
        plant = Plant(name, height, age)
        plants.append(plant)

    print("\n=== Plant Factory Output  ===")
    for plant in plants:
        print(f"Created: ({plant.name.capitalize()}: {plant.height}"
              + f"cm, {plant.age} days")
    print(f"Total Plants Created: {nunber_of_plants}")


if __name__ == "__main__":
    ft_plant_factory()
