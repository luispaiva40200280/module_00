
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def str(self) -> str:
        return f"{self.name}: {self.height}cm tall, {self.age} days old"
# start the child classes to add plant types


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return f"{self.name} is blooming with {self.color} flowers!"


class Tree(Plant):
    def __init__(self, name: str,
                 height: int, age: int, diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = diameter

    def produce_shade(self) -> str:
        shade_area = int(self.trunk_diameter * 0.14)
        return f"{self.name} is providing {shade_area} square meters"


class Vegetable(Plant):
    def __init__(self, name: str,
                 height: int, age: int,
                 nutricinal_value: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.nutricinal_value = nutricinal_value
        self.harvest_season = harvest_season

    def get_atributes(self) -> str:
        return (f"{self.nutricinal_value} calories, harvested in "
                + f"{self.harvest_season}")


def main() -> None:
    roses = [Flower("Rose", 50, 30, "red"),
             Flower("Tulip", 40, 20, "yellow")]
    oaks = [Tree("Oak", 500, 100, 120),
            Tree("Pine", 600, 80, 100)]
    Vegetables = [Vegetable("Carrot", 30, 60, 41, "Summer"),
                  Vegetable("Lettuce", 25, 45, 15, "Spring")]

    for flower in roses:
        print(flower.str())
        print(flower.bloom() + "\n")
    for tree in oaks:
        print(tree.str())
        print(tree.produce_shade() + "\n")
    for veg in Vegetables:
        print(veg.str())
        print(veg.get_atributes() + "\n")


if __name__ == "__main__":
    main()
