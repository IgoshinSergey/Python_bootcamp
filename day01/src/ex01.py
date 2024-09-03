from typing import Dict


def split_booty(*args) -> tuple[Dict[str, int], Dict[str, int], Dict[str, int]]:
    counter: int = 0
    for purse in args:
        counter += purse.get("gold_ingots", 0)
    new_purse_1: Dict[str, int] = {"gold_ingots": (counter // 3)}
    counter -= (counter // 3)
    new_purse_2: Dict[str, int] = {"gold_ingots": (counter // 2)}
    counter -= (counter // 2)
    new_purse_3: Dict[str, int] = {"gold_ingots": counter}
    return new_purse_3, new_purse_2, new_purse_1


def main() -> None:
    res = split_booty({"gold_ingots": 3}, {"gold_ingots": 2}, {"apples": 10})
    print(res)


if __name__ == "__main__":
    main()
