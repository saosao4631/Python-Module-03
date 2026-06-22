#!/usr/bin/env python3

import random

PLAYERS = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]


def capitalize_names(names: list[str]) -> list[str]:
    for name in names:
        name = name.capitalize()
    return names


def capitalized_only(names: list[str]) -> list[str]:
    for name in names:
        if name.istitle():
            return [name]
    return []


def enchant_score(players: list[str]) -> dict[str, int]:
    return {name: random.randint(0, 999) for name in players}


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {PLAYERS}")

    capitalized_players = capitalize_names(PLAYERS)
    print(f"New list with all names capitalized: {capitalized_players}")

    capitalized_name_only = capitalized_only(PLAYERS)
    print(f"New list of capitalized names only: {capitalized_name_only}")

    score = enchant_score(capitalized_players)
    print(f"Score dict: {score}")

    average = sum(score.values()) / len(score)
    print(f"Score average is {round(average, 2)}")

    high_scores = {
        name: score[name]
        for name in score
        if average < score[name]
    }
    print(f"High scores: {high_scores}")
