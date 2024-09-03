from typing import Dict
from functools import wraps


def print_squeak(func):
    @wraps(func)
    def squeak_wrapper(*args, **kwargs):
        print("SQUEAK")
        return func(*args, **kwargs)
    return squeak_wrapper


@print_squeak
def add_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    new_purse: type(purse) = purse.copy()
    new_purse["gold_ingots"] = new_purse.get("gold_ingots", 0) + 1
    return new_purse


@print_squeak
def get_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    new_purse: type(purse) = purse.copy()
    if purse.get("gold_ingots", 0) != 0:
        new_purse["gold_ingots"] -= 1
    return new_purse


@print_squeak
def empty(purse: Dict[str, int]) -> Dict[str, int]:
    new_purse: type(purse) = {}
    return new_purse


def main() -> None:
    purse: Dict[str, int] = {}
    print(add_ingot(get_ingot(add_ingot(empty(purse)))))


if __name__ == "__main__":
    main()
