def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        _ = 21 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        _ = "TypeError" + 21


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for op in range(5):
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError
                ) as err:
            print(f"Caught {err.__class__.__name__}: {err}")
        else:
            print("Operation completed successfully")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
