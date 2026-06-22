#!/usr/bin/env python3

import math


def to_float(input_str: str) -> float:
    try:
        return float(input_str)
    except ValueError as e:
        print(f"Error on parameter '{input_str}': {e}")
        raise


def get_player_pos() -> tuple[float, float, float]:
    while True:
        input_str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parts = input_str.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x = to_float(parts[0])
            y = to_float(parts[1])
            z = to_float(parts[2])
            return (x, y, z)
        except ValueError:
            pass


def distance(
        p1: tuple[float, float, float],
        p2: tuple[float, float, float],
        ) -> float:
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2
    )


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first_tuple = get_player_pos()
    print(f"Got a first tuple: ({first_tuple})")
    print(
        "It includes: "
        f"X={first_tuple[0]}, Y={first_tuple[1]}, Z={first_tuple[2]}"
        )
    print(f"Distance to center: {distance(first_tuple, (0.0, 0.0, 0.0))}")
    print("Get a second set of coordinates")
    second_tuple = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates: "
        f"{distance(first_tuple, second_tuple)}"
        )
