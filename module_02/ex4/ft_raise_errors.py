
def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if not isinstance(plant_name, str) or plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if not isinstance(water_level, int) or not (1 <= water_level <= 10):
        raise ValueError(f"Error: Water level {water_level} is invalid")
    if not isinstance(sunlight_hours, int) or not (2 <= sunlight_hours <= 12):
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is invalid")
    print(f"Plant '{plant_name}' is healthy!")


def main() -> None:
    print("Garden Plant Health Checker ===\n")
    plant = {"name": "Rose", "water": 8, "sunlight": 10}
    try:
        check_plant_health(plant["name"], plant["water"], plant["sunlight"])
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
