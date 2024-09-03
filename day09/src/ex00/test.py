import calculator


def main():
    print(f"{calculator.add(3.2, 2)=:.2f}")
    print(f"{calculator.sub(3.2, 2)=:.2f}")
    print(f"{calculator.mul(3.2, 2)=:.2f}")
    print(f"{calculator.div(3.2, 2)=:.2f}")
    print(f"{calculator.div(3.2, 0)=}")


if __name__ == "__main__":
    main()
