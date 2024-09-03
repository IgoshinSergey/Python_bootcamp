from typing import List


def fix_wiring(cables: List, sockets: List, plugs: List):
    return map(
        lambda elements:
        f"plug {elements[1][1]} into {elements[1][0]} using "
        f"{list(filter(lambda x: isinstance(x, str), plugs))[elements[0]]}"
        if elements[0] < len(list(filter(lambda x: isinstance(x, str), plugs))) else
        f"weld {elements[1][1]} to {elements[1][0]} without plug",
        list(
            enumerate(
                zip(
                    filter(lambda x: isinstance(x, str), cables),
                    filter(lambda x: isinstance(x, str), sockets)
                )
            )
        )
    )


def main():
    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]

    # sockets = ["socket1", "socket2", "socket3", "socket4"]
    # cables = ["cable1", "cable2", "cable3", "cable4"]
    # plugs = ["plug1", "plug2", "plug3"]

    for i in fix_wiring(sockets, cables, plugs):
        print(i)


if __name__ == "__main__":
    main()
