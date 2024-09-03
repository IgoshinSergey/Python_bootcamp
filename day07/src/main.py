from voight_kampff_test import VoightKampff


def main() -> None:
    """
    Main function.

    Returns:
        None
    """
    VoightKampff("resources/questions.json").run()


if __name__ == "__main__":
    main()
