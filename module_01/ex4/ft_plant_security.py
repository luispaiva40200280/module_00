
class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: int) -> str:
        if height < 0:
            return (
                f"Invalid operation attempted: height {height}cm [REJECTED]\n"
                + "Security: Negative height rejected!"
                )
        else:
            self._height = height
            return f"Height updated: {height}cm [OK].\n"

    def set_age(self, age: int) -> None:
        if age < 0:
            return (
                f"Invalid operation attempted: age {age} days [REJECTED]\n"
                + "Security: Negative height rejected!"
                )
        else:
            self._age = age
            return f"Age updated: {age} days [OK].\n"


def get_plant_info() -> None:
    name = input("Enter plant name: ")
    try:
        height = int(input("Enter plant height in cm: "))
        age = int(input("Enter plant age in days: "))
    except ValueError:
        print("ERROR: Height and age needs to be integres.")
        return
    plant = SecurePlant(name, height, age)
    print("== Garden Security System ==")
    print("\n" + plant.set_height(height))
    print(plant.set_age(age))
    if (height >= 0 and age >= 0):
        print(f"Current plant: {plant._name} ({plant.get_height()}cm,"
              + f"{plant.get_age()} days")


if __name__ == "__main__":
    get_plant_info()
