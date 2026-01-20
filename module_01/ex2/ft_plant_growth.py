
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_plant_growth() -> None:
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    growth_rate = 6  # cm per day
    days = 7  # number of days to simulate
    print("\n=== Plant Growth Simulation ===")
    i = 1
    while i <= days:
        print(f"\n--- Day {i} ---")
        for plant in plants:
            plant.height += growth_rate
            plant.age += 1
            print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
        i += 1


if __name__ == "__main__":
    ft_plant_growth()
