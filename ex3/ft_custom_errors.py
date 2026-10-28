class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown watering error") -> None:
        super().__init__(message)


def check_plant(plant_state: str) -> None:
    if plant_state == "wilting":
        raise PlantError("The tomato plant is wilting!")


def check_water_tank(level: int) -> None:
    if level < 10:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        check_plant("wilting")
    except PlantError as err:
        print(f"Caught PlantError: {err}")

    print("Testing WaterError...")
    try:
        check_water_tank(2)
    except WaterError as err:
        print(f"Caught WaterError: {err}")

    print("Testing catching all garden errors...")
    try:
        check_plant("wilting")
    except GardenError as err:
        print(f"Caught GardenError: {err}")

    try:
        check_water_tank(2)
    except GardenError as err:
        print(f"Caught GardenError: {err}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
