class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def catch_plant_error() -> str:
    try:
        raise PlantError("The plant is wilting!!")
    except PlantError as e:
        return f"cought Plant Error: {e}\n"


def catch_water_error() -> str:
    try:
        raise WaterError("Not enough Water!!")
    except WaterError as e:
        return f"Cought Water Error: {e}\n"


def catch_garden_error():
    try:
        raise WaterError("Not enough Water!!")
    except GardenError as e:
        print(f"cought a Garden Error: {e}")
    try:
        raise PlantError("The plant is wilting!!")
    except GardenError as e:
        print(f"cought a Garden Error: {e}")


def ft_custom_error() -> None:
    print("Custom Garden Errors Demo")

    print("\n Testing Plant Error...")
    print("Testing PlantError...")
    print(catch_plant_error())
    print("Testing WaterError...")
    print(catch_water_error())
    print("Testing catching all garden errors...")
    catch_garden_error()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_error()
