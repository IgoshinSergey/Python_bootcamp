from voight_kampff_test import Validator

import pytest
import os

JSON_DIR = os.path.join(os.path.dirname(__file__), "resources")


class TestValidator:
    """
    A test class for the Validator class.

    Methods:
    test_is_json_file(filepath, res): Tests the is_json_file method.
    test_is_valid_questions(questions, res): Tests the is_valid_questions method.
    test_is_valid_answer(answer, res): Tests the is_valid_answer method.
    test_is_valid_respiration(respiration, res): Tests the is_valid_respiration method.
    test_is_valid_heart_rate(heart_rate, res): Tests the is_valid_heart_rate method.
    test_is_valid_blushing_level(blushing_level, res): Tests the is_valid_blushing_level method.
    test_is_valid_pupillary_dilation(pupillary_dilation, res): Tests the is_valid_pupillary_dilation method.
    """
    @pytest.mark.parametrize(
        "filepath, res",
        [
            (f"{JSON_DIR}/example_1.json", True),
            (f"{JSON_DIR}/example_2.json", True),
            (f"{JSON_DIR}/example_3", False),
            (f"{JSON_DIR}/example_4.json", False),
            (f"{JSON_DIR}/non_existent_file.json", False),
        ]
    )
    def test_is_json_file(self, filepath: str, res: bool):
        """
        Tests the is_json_file method.

        Parameters:
        filepath (str): The filepath to test.
        res (bool): The expected result.

        Returns:
        None
        """
        assert Validator.is_json_file(filepath) == res

    @pytest.mark.parametrize(
        "questions, res",
        [
            ({
                "questions": [
                    {
                        "question": "How are you doing?",
                        "answers": [
                            "1", "2", "3", "4"
                        ]
                    }
                ]
             }, True),
            ({
                "questions": {
                    "question": "How are you doing?"
                }
             }, False),
            ({
                "question": {
                    "question": "How are you doing?",
                    "answers": [
                        "1", "2", "3", "4"
                    ]
                }
             }, False),
        ]
    )
    def test_is_valid_questions(self, questions: dict, res: bool):
        """
        Tests the is_valid_questions method.

        Parameters:
        questions (dict): The questions to test.
        res (bool): The expected result.

        Returns:
        None
        """
        assert Validator.is_valid_questions(questions) == res

    @pytest.mark.parametrize(
        "answer, res",
        [
            ("1", True),
            ("qwerty", False),
            ("1234abd", False),
            ("3", True),
            ("5", False),
        ]
    )
    def test_is_valid_answer(self, answer: str, res: bool):
        """
        Tests the is_valid_answer method.

        Parameters:
        answer (str): The answer to test.
        res (bool): The expected result.

        Returns:
        None
        """
        assert Validator.is_valid_answer(answer) == res

    @pytest.mark.parametrize(
        "respiration, res",
        [
            ("1", True),
            ("75", True),
            ("150", True),
            ("qwerty", False),
            ("1234abd", False),
            ("-3", False),
            ("5.1234", False),
        ]
    )
    def test_is_valid_respiration(self, respiration: str, res: bool):
        """
        Tests the is_valid_respiration method.

        Parameters:
        respiration (str): The respiration to test.
        res (bool): The expected result.

        Returns:
        None
        """
        assert Validator.is_valid_respiration(respiration) == res

    @pytest.mark.parametrize(
        "heart_rate, res",
        [
            ("1", True),
            ("75", True),
            ("150", True),
            ("300", True),
            ("qwerty", False),
            ("1234abd", False),
            ("0", False),
            ("-3", False),
            ("5.1234", False),
        ]
    )
    def test_is_valid_heart_rate(self, heart_rate: str, res: bool):
        """
        Tests the is_valid_heart_rate method.

        Parameters:
        heart_rate (str): The heart rate to test.
        res (bool): The expected result.

        Returns:
        None
        """
        assert Validator.is_valid_heart_rate(heart_rate) == res

    @pytest.mark.parametrize(
        "blushing_level, res",
        [
            ("1", True),
            ("6", True),
            ("7", False),
            ("qwerty", False),
            ("1234abd", False),
            ("0", False),
            ("-3", False),
            ("5.1234", False),
        ]
    )
    def test_is_valid_blushing_level(self, blushing_level: str, res: bool):
        """
        Tests the is_valid_pupillary_dilation method.

        Parameters:
        pupillary_dilation (str): The pupillary dilation to test.
        res (bool): The expected result.

        Returns:
        None
        """
        assert Validator.is_valid_blushing_level(blushing_level) == res

    @pytest.mark.parametrize(
        "pupillary_dilation, res",
        [
            ("1", True),
            ("6", True),
            ("20", True),
            ("21", False),
            ("1234abd", False),
            ("0", False),
            ("-3", False),
            ("5.1234", False),
        ]
    )
    def test_is_valid_pupillary_dilation(self, pupillary_dilation: str, res: bool):
        """
        Tests the is_valid_pupillary_dilation method.

        Parameters:
        pupillary_dilation (str): The pupillary dilation to test.
        res (bool): The expected result.

        Returns:
        None
        """
        assert Validator.is_valid_pupillary_dilation(pupillary_dilation) == res
