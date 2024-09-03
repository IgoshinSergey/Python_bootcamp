from voight_kampff_test import VoightKampff
from typing import List
import pytest
import os


JSON_DIR = os.path.join(os.path.dirname(__file__), "resources")


class TestVoightKampff:
    """
    A test class for the VoightKampff class.

    Methods:
    test_load_json_data(filepath, res): Tests the load_json_data method.
    test_update_user_data_1(input_data): Tests the update_user_data method with example 1.
    test_update_user_data_2(input_data): Tests the update_user_data method with example 2.
    test_calculate_result(input_data, res): Tests the calculate_result method.
    """

    @pytest.mark.parametrize(
        "filepath, res",
        [
            (f"{JSON_DIR}/example_1.json", True),
            (f"{JSON_DIR}/example_2.json", False),
            (f"{JSON_DIR}/example_3", False),
            (f"{JSON_DIR}/example_4.json", False),
        ]
    )
    def test_load_json_data(self, filepath: str, res: bool):
        """
        Tests the load_json_data method.

        Parameters:
        filepath (str): The filepath to test.
        res (bool): The expected result.

        Returns:
        None
        """
        voight_kampff = VoightKampff(filepath)
        assert voight_kampff.load_json_data() == res

    @pytest.mark.parametrize(
        "input_data",
        [
            (["1", "13", "75", "2", "2"]),
            (["q", "1", "1234", "13", "75", "qwr12", "2", "2"])
        ]
    )
    def test_update_user_data_1(self, monkeypatch: pytest.MonkeyPatch, input_data: List[str]):
        """
        Tests the update_user_data method with example 1.

        Parameters:
        monkeypatch (pytest.MonkeyPatch): A pytest monkeypatch object.
        input_data (List[str]): The input data to test.

        Returns:
        None
        """
        voight_kampff = VoightKampff(f"{JSON_DIR}/example_1.json")

        def mock_input(prompt):
            return input_data.pop(0)
        monkeypatch.setattr("builtins.input", mock_input)
        voight_kampff.load_json_data()
        voight_kampff.ask_questions()
        assert voight_kampff.get_user_data() == {
            "respiration": 13,
            "heart_rate": 75,
            "blushing_level": 2,
            "pupillary_dilation": 2
        }

    @pytest.mark.parametrize(
        "input_data",
        [
            (
                [
                    "1", "13", "75", "2", "2",
                    "4", "10", "100", "1", "3",
                    "2", "12", "120", "2", "2"
                ]
            ),
        ]
    )
    def test_update_user_data_2(self, monkeypatch: pytest.MonkeyPatch, input_data: List[str]):
        """
        Tests the update_user_data method with example 2.

        Parameters:
        monkeypatch (pytest.MonkeyPatch): A pytest monkeypatch object.
        input_data (List[str]): The input data to test.

        Returns:
        None
        """
        voight_kampff = VoightKampff(f"{JSON_DIR}/example_5.json")

        def mock_input(prompt):
            return input_data.pop(0)
        monkeypatch.setattr("builtins.input", mock_input)
        voight_kampff.load_json_data()
        voight_kampff.ask_questions()
        assert voight_kampff.get_user_data() == {
            "respiration": 35,
            "heart_rate": 295,
            "blushing_level": 5,
            "pupillary_dilation": 7
        }

    @pytest.mark.parametrize(
        "input_data, res",
        [
            (
                [
                    "1", "13", "75", "2", "2",
                    "4", "10", "100", "1", "3",
                    "2", "12", "120", "2", "2"
                ],
                False
            ),
            (
                [
                    "1", "13", "75", "2", "2",
                    "2", "14", "80", "1", "3",
                    "2", "12", "85", "2", "2"
                ],
                True
            ),
            (
                [
                    "1", "13", "75", "4", "2",
                    "2", "14", "80", "4", "3",
                    "2", "12", "85", "2", "2"
                ],
                False
            ),
            (
                [
                    "1", "13", "75", "2", "1",
                    "2", "14", "80", "1", "1",
                    "2", "12", "85", "2", "2"
                ],
                False
            ),
        ]
    )
    def test_calculate_result(self, monkeypatch: pytest.MonkeyPatch, input_data: List[str], res: bool):
        """
        Tests the calculate_result method.

        Parameters:
        monkeypatch (pytest.MonkeyPatch): A pytest monkeypatch object.
        input_data (List[str]): The input data to test.
        res (bool): The expected result.

        Returns:
        None
        """
        voight_kampff = VoightKampff(f"{JSON_DIR}/example_5.json")

        def mock_input(prompt):
            return input_data.pop(0)

        monkeypatch.setattr("builtins.input", mock_input)
        voight_kampff.load_json_data()
        voight_kampff.ask_questions()
        assert voight_kampff.calculate_result() == res
