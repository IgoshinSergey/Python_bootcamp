from sys import stdin
import argparse


def check_zero_in_line(string: str) -> bool:
    return string.startswith("00000") and string[5] != "0"


def parsing_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("number_of_lines", type=int, help="Number of lines")
    return parser.parse_args()


def main():
    args = parsing_arguments()
    for i in range(args.number_of_lines):
        line = stdin.readline().strip()
        if len(line) == 32 and check_zero_in_line(line):
            print(line)


if __name__ == "__main__":
    main()
