#!/usr/bin/env python3

import random

ACHIEVEMENTS = [
    "Crafting Genius"
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Unstoppable",
    "Treasure Hunter",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    count = random.randint(6, 11)
    player_achievements = random.sample(ACHIEVEMENTS, count)
    return set(player_achievements)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    Alice_list = gen_player_achievements()
    Bob_list = gen_player_achievements()
    Charlie_list = gen_player_achievements()
    Dylan_list = gen_player_achievements()
    achievements = set(ACHIEVEMENTS)
    all_list = set.union(Alice_list, Bob_list, Charlie_list, Dylan_list)

    print(f"Player Alice: {Alice_list}")
    print(f"Player Bob: {Bob_list}")
    print(f"Player Charlie: {Charlie_list}")
    print(f"Player Dylan: {Dylan_list}")
    print("")
    print(f"All distinct achievements: {all_list}")
    print("")
    print(
        "Common achievements: "
        f"{set.intersection(Alice_list, Bob_list, Charlie_list, Dylan_list)}"
    )
    print("")
    print(
        "Only Alice has: "
        f"{Alice_list.difference(Bob_list, Charlie_list, Dylan_list)}"
    )
    print(
        "Only Bob has: "
        f"{Bob_list.difference(Alice_list, Charlie_list, Dylan_list)}"
    )
    print(
        "Only Charlie has: "
        f"{Charlie_list.difference(Alice_list, Bob_list, Dylan_list)}"
    )
    print(
        "Only Dylan has: "
        f"{Dylan_list.difference(Alice_list, Bob_list, Charlie_list)}"
    )
    print("")
    print(f"Alice is missing: {achievements.difference(Alice_list)}")
    print(f"Bob is missing: {achievements.difference(Bob_list)}")
    print(f"Charlie is missing: {achievements.difference(Charlie_list)}")
    print(f"Dylan is missing: {achievements.difference(Dylan_list)}")
