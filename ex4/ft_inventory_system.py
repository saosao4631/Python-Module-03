import sys


def create_inventory(args: list[str]) -> dict[str, int]:
    invent: dict[str, int] = {}
    for arg in args:
        item_parts = arg.split(":")
        if len(item_parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item_name = item_parts[0]
        if item_name in invent.keys():
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(item_parts[1])
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
            continue

        invent.update({item_name: quantity})
    return invent


def print_percentages(invent: dict[str, int], total: int) -> None:
    for key in invent.keys():
        if total == 0:
            percentage = 0.0
        else:
            percentage = round(invent[key] / total * 100, 1)
        print(
            f"Item {key} represents "
            f"{percentage}%"
        )


def find_most_item(invent: dict[str, int]) -> str:
    keys = list(invent.keys())
    item_name = keys[0]
    quantity = invent[keys[0]]

    for key in keys[1:]:
        if quantity < invent[key]:
            item_name = key
            quantity = invent[key]
    return item_name


def find_least_item(invent: dict[str, int]) -> str:
    keys = list(invent.keys())
    item_name = keys[0]
    quantity = invent[keys[0]]

    for key in keys[1:]:
        if invent[key] < quantity:
            item_name = key
            quantity = invent[key]
    return item_name


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    if len(sys.argv) < 2:
        print(
            "No items provided. Usage: "
            "python3 ft_inventory_system.py <item_name>:<quantity> ..."
        )

    invent = create_inventory(sys.argv[1:])

    if len(invent) == 0:
        print("Got inventory: {}")

    total = sum(list(invent.values()))
    print(f"Got inventory: {invent}")
    print(f"Item list: {list(invent.keys())}")
    print(f"Total quantity of the {len(invent)} items: {total}")
    print_percentages(invent, total)

    most = find_most_item(invent)
    print(
        f"Item most abundant: {most} "
        f"with quantity {invent[most]}"
    )
    least = find_least_item(invent)
    print(
        f"Item least abundant: {least} "
        f"with quantity {invent[least]}"
    )

    invent.update(magic_item=1)
    print(f"Updated inventory: {invent}")
