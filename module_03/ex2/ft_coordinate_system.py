
from sys import argv as argv
from math import sqrt as sqrt


def ft_unpack_coor(coord_str: list[str]) -> list[int] | None:
    coords = []
    try:
        for c in coord_str:
            c = int(c)
            coords.append(c)
        return coords
    except (IndexError, ValueError) as e:
        c = ",".join(coord_str)
        print(
            f"\nParsing invalid coordinates: {c}\n"
            f"Error parsing coordinates: {e}\n"
            f"Error details - Type: {e.__class__.__name__}, Args: {e.args}"
        )
        return None


def ft_coordinate_system(argv: list[tuple]) -> None:
    leng = len(argv)
    coords = []

    if leng == 1:
        print("No coordenates imputed")
        return
    elif leng == 2:
        coord_str = argv[1].replace(',', ' ').split()
        coords = ft_unpack_coor(coord_str)
    elif leng == 4:
        argv.pop(0)
        coords = ft_unpack_coor(argv)
    else:
        print("There is not enought/to many valid aguments")
        return

    if coords is None:
        return

    cx, cy, cz = coords
    x1, y1, z1 = 0, 0, 0
    orig = (x1, y1, z1)
    pos = (cx, cy, cz)
    distance = sqrt((cx-x1)**2 + (cy-y1)**2 + (cz-z1)**2)

    print("=== Game Coordinate System ===\n")
    print(
        f"Parsing coordinates: {pos}\n"
        f"Position created: {pos}\n"
        f"Distance between {orig} and {pos}: {distance:.2f}\n"
    )

    print(
        f"Unpacking demonstration: \n"
        f"Player at x={cx}, y={cy}, z={cz} \n"
        f"Coordinates: x={cx}, y={cy}, z={cz} "
    )


if __name__ == "__main__":
    ft_coordinate_system(argv)
