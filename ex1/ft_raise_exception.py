def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)

    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    test_input = ["25", "abc", "100", "-50"]

    for temp_input in test_input:
        print(f"Input data is '{temp_input}'")
        try:
            temp_val = input_temperature(temp_input)
        except ValueError as err:
            print(f"Caught input_temperature error: {err}")
        else:
            print(f"Temperature is now {temp_val}°C")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
