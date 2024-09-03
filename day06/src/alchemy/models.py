from .database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class TableSpaceship(Base):
    __tablename__ = 'spaceships'
    id: Mapped[int] = mapped_column(primary_key=True)
    alignment: Mapped[str]
    name: Mapped[str]
    ship_class: Mapped[str]
    length: Mapped[float]
    crew_size: Mapped[int]
    armed: Mapped[bool]


class TableOfficers(Base):
    __tablename__ = 'officers'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    rank: Mapped[str]
    ship_id: Mapped[int] = mapped_column(ForeignKey('spaceships.id'))
