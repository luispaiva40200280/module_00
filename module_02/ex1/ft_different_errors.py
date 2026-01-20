
def test_error_types() -> None:
    try:
        test_int = int(input("Test if the user input is a valid int: "))
        print(f"{test_int} is a int")
    except ValueError:
        print(f"The input user is not a number: {test_int}")

    try:
        fd = "ola.txt"
        file_test = open(fd)
        print(f"{fd} was open")
        file_test.close()
    except FileNotFoundError:
        print(f"{fd} does not exist!!")

    try:
        nub1 = int(input("number 1: "))
        nub2 = int(input("number 2: "))
        division = nub1 / nub2
        print(f"the {nub1} / {nub2} == {division} ")
    except ZeroDivisionError:
        print(f"Inpossible to divide the numbers {nub1} and {nub2}!!")

    try:
        plants = {
            "rose": "Red Flower",
            "tulip": "Pink Flower",
            "sunflower": "Yellow Flower"
            }
        plant = input("Plant to see: ")
        print(f"Info: {plants[plant]}")
    except KeyError:
        print(f"{plant} does not exist in the list")


if __name__ == "__main__":
    test_error_types("ola.txt")
