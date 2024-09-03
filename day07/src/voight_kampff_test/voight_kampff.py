from .validator import Validator
from .constants import *
import json


class VoightKampff:
    """
    Voight-Kampff test for detecting replicants.

    Attributes:
    filepath (str): The path to the JSON file.
    validator (Validator): The validator object.
    respiration (float): The amount respiration rate of the user.
    heart_rate (float): The amount heart rate of the user.
    blushing_level (float): The amount blushing level of the user.
    pupillary_dilation (float): The amount pupillary dilation of the user.
    json_data (dict): The JSON data loaded from the file.
    user_answers (list[int]): The list of user answers.

    Methods:
    load_json_data(): Loads the JSON data from the file.
    get_user_data(): Returns the user's physiological data.
    print_question(question): Prints a question to the user.
    user_input_answer(): Gets the user's answer to a question.
    user_data(text, validator): Gets user input for a specific physiological parameter.
    update_person_data(): Updates the user's physiological data.
    ask_questions(): Asks the user a series of questions.
    calculate_result(): Calculates the result of the Voight-Kampff test.
    print_result(is_human): Prints the result of the test.
    run(): Runs the Voight-Kampff test.
    """
    def __init__(self, filepath: str):
        """
        Initializes the Voight-Kampff machine.

        Parameters:
        filepath (str): The path to the JSON file.
        """
        self.__validator: Validator = Validator()
        self.__filepath: str = filepath
        self.__respiration: float = 0
        self.__heart_rate: float = 0
        self.__blushing_level: float = 0
        self.__pupillary_dilation: float = 0
        self.__json_data: dict = dict()
        self.__user_answers: list[int] = list()

    def load_json_data(self) -> bool:
        """
        Loads the JSON data from the file.

        Returns:
        bool: True if the data was loaded successfully, False otherwise.
        """
        if not self.__validator.is_json_file(self.__filepath):
            return False
        with open(self.__filepath, "r") as file:
            self.__json_data: dict = json.load(file)
            if not self.__validator.is_valid_questions(self.__json_data):
                return False
        return True

    def get_user_data(self):
        """
        Returns the user's physiological data.

        Returns:
        dict: A dictionary containing the user's physiological data.
        """
        return {
            "respiration": self.__respiration,
            "heart_rate": self.__heart_rate,
            "blushing_level": self.__blushing_level,
            "pupillary_dilation": self.__pupillary_dilation
        }

    @staticmethod
    def print_question(question: dict) -> None:
        """
        Prints a question to the user.

        Parameters:
        question (dict): The question to be printed.
        """
        print(f"{question["question"]}")
        for answer in question["answers"]:
            print(f"{answer}")

    def user_input_answer(self) -> int:
        """
        Gets the user's answer to a question.

        Returns:
        int: The user's answer.
        """
        answer = input(YOUR_ANSWER)
        while not self.__validator.is_valid_answer(answer):
            answer = input(YOUR_ANSWER)
        return int(answer)

    @staticmethod
    def user_data(text: str, validator) -> int:
        """
        Gets user input for a specific physiological parameter.

        Parameters:
        text (str): The prompt to display to the user.
        validator: The validator function to use.

        Returns:
        int: The user's input.
        """
        data = input(text)
        while not validator(data):
            data = input(text)
        return int(data)

    def update_person_data(self):
        """
        Updates the user's physiological data.

        Returns:
        None
        """
        print()
        print(INPUT_HUMAN_DATA)
        self.__respiration += self.user_data(RESPIRATION, self.__validator.is_valid_respiration)
        self.__heart_rate += self.user_data(HEART_RATE, self.__validator.is_valid_heart_rate)
        self.__blushing_level += self.user_data(BLUSHING_LEVEL, self.__validator.is_valid_blushing_level)
        self.__pupillary_dilation += self.user_data(PUPILLARY_DILATION, self.__validator.is_valid_pupillary_dilation)
        print()

    def ask_questions(self) -> None:
        """
        Asks the user a series of questions.

        Returns:
        None
        """
        for data in self.__json_data["questions"]:
            self.print_question(data)
            self.__user_answers.append(self.user_input_answer())
            self.update_person_data()

    def calculate_result(self) -> bool:
        """
        Calculates the result of the Voight-Kampff test.

        Returns:
        bool: True if the user is a human, False otherwise.
        """
        avg_respiration: float = self.__respiration / len(self.__user_answers)
        avg_heart_rate: float = self.__heart_rate / len(self.__user_answers)
        avg_blushing_level: float = self.__blushing_level / len(self.__user_answers)
        avg_pupillary_dilation: float = self.__pupillary_dilation / len(self.__user_answers)
        if (12 < avg_respiration < 16 and 60 < avg_heart_rate < 100
                and 1 < avg_blushing_level < 3 and 2 < avg_pupillary_dilation < 8
                and self.__user_answers.count(4) < 3):
            return True
        else:
            return False

    @staticmethod
    def print_result(is_human: bool) -> None:
        """
        Prints the result of the test.

        Parameters:
        is_human (bool): True if the user is a human, False otherwise.
        """
        print(YOU_HUMAN) if is_human else print(YOU_REPLICANT)

    def run(self) -> None:
        """
        Runs the Voight-Kampff test.

        Returns:
        None
        """
        if not self.load_json_data():
            print(INCORRECT_FILE)
            return
        self.ask_questions()
        self.print_result(self.calculate_result())
