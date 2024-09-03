from sys import stdin


def check_m_pattern(text: list[str]) -> bool:
    result: bool = True
    count_lines: int = 0
    count_symbols: dict = {}
    indexes = [0, 4, 5, 6, 8, 9, 10, 12, 14]
    for i, line in enumerate(text):
        line = line.strip()
        if len(line) == 5 and count_lines < 3:
            count_lines += 1
        else:
            result = False
            break
        for j, symbol in enumerate(line):
            if i * 5 + j in indexes:
                if symbol != '*':
                    result = False
                    break
            else:
                if (symbol == '*') or (count_symbols.get(symbol, 0) > 0):
                    result = False
                    break
                else:
                    count_symbols[symbol] = count_symbols.get(symbol, 0) + 1
    if count_lines != 3:
        result = False
    return result


def main():
    lines: list[str] = stdin.readlines()
    res = check_m_pattern(lines)
    print(res)


if __name__ == '__main__':
    main()
