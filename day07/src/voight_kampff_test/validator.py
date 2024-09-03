from typing import List, Dict, Literal
from pydantic import BaseModel, ValidationError, model_validator
import os


class Question(BaseModel):
    """
    A question with a list of possible answers.

    Attributes:
    question (str): The question text.
    answers (List[str]): The list of possible answers.
    """
    question: str
    answers: List[str]


class Questions(BaseModel):
    """
    A collection of questions.

    Attributes:
    questions (List[Question]): The list of questions.
    """
    questions: List[Question]


class UserInputAnswer(BaseModel):
    """
    A user's answer to a question.

    Attributes:
    answer (Literal["1", "2", "3", "4"]): The user's answer.
    """
    answer: Literal["1", "2", "3", "4"]


class UserInputRespiration(BaseModel):
    """
    A user's respiration rate.

    Attributes:
    respiration (str): The user's respiration rate.

    Validators:
    respiration_validator: Checks that the respiration rate is a valid integer between 1 and 150.
    """
    respiration: str

    @model_validator(mode="before")
    def respiration_validator(cls, values):
        if not values.get("respiration").isdigit():
            raise TypeError("Respiration must be an integer")
        resp = int(values.get("respiration"))
        if resp < 1 or resp > 150:
            raise ValidationError()
        return values


class UserInputHeartRate(BaseModel):
    """
    A user's heart rate.

    Attributes:
    heart_rate (str): The user's heart rate.

    Validators:
    heart_rate_validation: Checks that the heart rate is a valid integer between 1 and 300.
    """
    heart_rate: str

    @model_validator(mode="before")
    def heart_rate_validation(cls, values):
        if not values.get("heart_rate").isdigit():
            raise TypeError()
        hr = int(values.get("heart_rate"))
        if hr < 1 or hr > 300:
            raise ValidationError()
        return values


class UserInputBlushingLevel(BaseModel):
    """
    A user's blushing level.

    Attributes:
    blushing_level (str): The user's blushing level.

    Validators:
    heart_rate_validation: Checks that the blushing level is a valid integer between 1 and 6.
    """
    blushing_level: str

    @model_validator(mode="before")
    def heart_rate_validation(cls, values):
        if not values.get("blushing_level").isdigit():
            raise TypeError()
        bl = int(values.get("blushing_level"))
        if bl < 1 or bl > 6:
            raise ValidationError()
        return values


class UserInputPupillaryDilation(BaseModel):
    """
    A user's pupillary dilation.

    Attributes:
    pupillary_dilation (str): The user's pupillary dilation.

    Validators:
    heart_rate_validation: Checks that the pupillary dilation is a valid integer between 1 and 20.
    """
    pupillary_dilation: str

    @model_validator(mode="before")
    def heart_rate_validation(cls, values):
        if not values.get("pupillary_dilation").isdigit():
            raise TypeError()
        pd = int(values.get("pupillary_dilation"))
        if pd < 1 or pd > 20:
            raise ValidationError()
        return values


class Validator:
    """
    A validator class for checking the validity of user input.

    Methods:
    is_valid_questions(questions): Checks if the questions are valid.
    is_valid_answer(answer): Checks if the answer is valid.
    is_json_file(filepath): Checks if the filepath is a valid JSON file.
    is_valid_respiration(respiration): Checks if the respiration is valid.
    is_valid_heart_rate(heart_rate): Checks if the heart rate is valid.
    is_valid_blushing_level(blushing_level): Checks if the blushing level is valid.
    is_valid_pupillary_dilation(pupillary_dilation): Checks if the pupillary dilation is valid.
    """
    @staticmethod
    def is_valid_questions(questions: Dict) -> bool:
        try:
            Questions(**questions)
            return True
        except ValidationError:
            return False

    @staticmethod
    def is_valid_answer(answer: str) -> bool:
        try:
            UserInputAnswer(answer=answer)
            return True
        except ValidationError:
            return False

    @staticmethod
    def is_json_file(filepath: str) -> bool:
        return os.path.isfile(filepath) and os.stat(filepath).st_size and filepath.endswith(".json")

    @staticmethod
    def is_valid_respiration(respiration: str) -> bool:
        try:
            UserInputRespiration(respiration=respiration)
            return True
        except (ValidationError, TypeError):
            return False

    @staticmethod
    def is_valid_heart_rate(heart_rate: str) -> bool:
        try:
            UserInputHeartRate(heart_rate=heart_rate)
            return True
        except (ValidationError, TypeError):
            return False

    @staticmethod
    def is_valid_blushing_level(blushing_level: str) -> bool:
        try:
            UserInputBlushingLevel(blushing_level=blushing_level)
            return True
        except (ValidationError, TypeError):
            return False

    @staticmethod
    def is_valid_pupillary_dilation(pupillary_dilation: str) -> bool:
        try:
            UserInputPupillaryDilation(pupillary_dilation=pupillary_dilation)
            return True
        except (ValidationError, TypeError):
            return False
