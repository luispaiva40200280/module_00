from sys import argv


def main(argv: list[tuple]) -> None:
    print("=== Command Quest ===")

    list_args = argv
    if len(list_args) == 1:
        print("No args recived!!")
    else:
        print(f"Arguments recive : {len(list_args)}")
    i = 0
    for arg in list_args:
        if i == 0:
            print(f"Progam name: {arg}")
        else:
            print(f"Argumen {i}: {arg}")
        i += 1
    print(f"Total arguments: {len(list_args)}")


if __name__ == "__main__":
    main(argv)
