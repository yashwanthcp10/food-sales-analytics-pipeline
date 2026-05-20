from src.utils.retry import retry_on_failure


counter = 0


@retry_on_failure()
def test_function():
    global counter

    counter += 1

    print(f"Attempt: {counter}")

    if counter < 3:
        raise Exception("Temporary failure")

    print("Success")


test_function()