from reporting_client import parse_args, get_ships
import grpc

from pydantic import BaseModel, ValidationError, model_validator, Field
from typing import List


class OfficerModel(BaseModel):
    first_name: str
    last_name: str
    rank: str


class ShipModel(BaseModel):
    alignment: str
    name: str
    length: float
    class_ship: str = Field(alias="class")
    crew_size: int
    armed: bool
    officers: List[OfficerModel]

    @model_validator(mode="after")
    def validate_officers(self):
        if not ((
            self.class_ship == "Corvette" and 80 <= self.length <= 250 and
            4 <= self.crew_size <= 10 and self.armed
        ) or (
            self.class_ship == "Frigate" and 300 <= self.length <= 600 and
            10 <= self.crew_size <= 15 and self.armed and self.alignment == 'Ally'
        ) or (
            self.class_ship == "Cruiser" and 500 <= self.length <= 1000 and
            15 <= self.crew_size <= 30 and self.armed
        ) or (
            self.class_ship == "Destroyer" and 800 <= self.length <= 2000 and
            50 <= self.crew_size <= 80 and self.armed and self.alignment == 'Ally'
        ) or (
            self.class_ship == "Carrier" and 1000 <= self.length <= 4000 and
            120 <= self.crew_size <= 250 and not self.armed
        ) or (
            self.class_ship == "Dreadnought" and 5000 <= self.length <= 20000 and
            300 <= self.crew_size <= 500 and self.armed
        ) or (
            self.name == 'Unknown' and self.alignment == 'Ally'
        )):
            raise ValueError()
        return self


def is_valid_spaceship(ship: str) -> bool:
    try:
        ShipModel.model_validate_json(ship)
        return True
    except ValidationError as e:
        return False


def validate_spaceships(coords: List[float]):
    with grpc.insecure_channel('localhost:50051') as channel:
        for ship in get_ships(channel, coords):
            if is_valid_spaceship(ship):
                yield ship


if __name__ == "__main__":
    coordinates: List[float] = parse_args()
    for validate_ship in validate_spaceships(coordinates):
        print(validate_ship)
