
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height  # in centimeters
        self.age = age  # in years

    def __str__(self) -> str:
        return f"{self.name}, Height: {self.height} cm, Age: {self.age} years"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def __str__(self) -> str:
        return super().__str__() + f", Color: {self.color}"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int,
                 age: int, color: str, points: int) -> None:
        super().__init__(name, height, age, color)
        self.points = points


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.garden_plants = []

    def add_plant(self, plant: Plant) -> None:
        self.garden_plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")


class GardenManager:
    class GardenStats:
        @staticmethod
        def calculate_total_height(plants: list) -> int:
            total = 0
            for plant in plants:
                total += plant.height
            return total

    def __init__(self) -> None:
        self.gardens = {}

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        print("Booting up the Garden Network...")
        print("Establishing connections...\n")
        new_manager = cls()
        return new_manager

    def add_garden(self, owner: str) -> Garden:
        new_garden_owner = Garden(owner)
        self.gardens[owner] = new_garden_owner
        return new_garden_owner

    def get_garden(self, owner: str) -> Garden:
        return self.gardens.get(owner)

    def generate_report(self, owner: str) -> None:
        garden = self.get_garden(owner)
        if garden is None:
            print("The garden does not exist!")
            return
        print(f"=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in garden.garden_plants:
            print(f"- {plant}")
        total = self.GardenStats.calculate_total_height(garden.garden_plants)
        print(f"Total Plant Height: {total}cm")


def main() -> None:
    manager = GardenManager.create_garden_network()
    owner = str(input("Owner name:")).capitalize()
    garden1 = manager.add_garden(owner)
    rose = FloweringPlant("Rose", 25, 30, "Red")
    prize_flower = PrizeFlower("Super Sunflower", 80, 45, "Yellow", 100)

    garden1.add_plant(rose)
    garden1.add_plant(prize_flower)
    manager.generate_report(owner)


if __name__ == "__main__":
    main()
