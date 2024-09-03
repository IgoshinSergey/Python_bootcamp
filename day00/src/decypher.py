import argparse


def parsing_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("cypher", type=str, help="The cypher")
    return parser.parse_args()


def main():
    args = parsing_arguments()
    line: list[str] = args.cypher.split()
    result: str = ""
    for word in line:
        result += word[0]
    print(result)


if __name__ == "__main__":
    main()
