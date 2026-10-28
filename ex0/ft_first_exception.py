def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    test_input = ["25", "abc"]

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
