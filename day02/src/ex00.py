class Key:
    def __init__(self, passphrase: str = "zax2rulez"):
        self.passphrase: str = passphrase

    def __len__(self) -> int:
        return 1337

    def __getitem__(self, item) -> int:
        return 3

    def __str__(self) -> str:
        return "GeneralTsoKeycard"

    def __gt__(self, other) -> bool:
        return True


def test():
    key = Key()
    assert len(key) == 1337
    assert key[404] == 3
    assert key > 9000
    assert key.passphrase == "zax2rulez"
    assert str(key) == "GeneralTsoKeycard"
    print("The test is passed")


def main():
    test()


if __name__ == '__main__':
    main()
