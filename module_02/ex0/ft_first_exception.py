
def check_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
        if temp > 40:
            print(f"{temp}C is to higth for the plants")
        elif temp < 0:
            print(f"{temp}C is to low for the plants")
        else:
            print(f"Temperature {temp}C is perfect for plants!")
        return temp
    except ValueError:
        print(f"Error {temp_str} is not valid number")


if __name__ == "__main__":
    check_temperature("ola")
    check_temperature("-152")
    check_temperature("52")
    check_temperature("2")
    check_temperature("25")
