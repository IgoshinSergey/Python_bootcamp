from .database import session_factory, engine, Base
from .models import TableSpaceship, TableOfficers


def is_duplicate(spaceship) -> bool:
    with session_factory() as session:
        db_spaceships = session.query(TableSpaceship).filter(TableSpaceship.name == spaceship['name']).all()
        if len(db_spaceships) == 0:
            return False
        for db_spaceship in db_spaceships:
            db_officers = session.query(TableOfficers).filter(TableOfficers.ship_id == db_spaceship.id).all()
            if len(db_officers) != len(spaceship['officers']):
                return False
            for db_officer in db_officers:
                db_officer = {
                    'first_name': db_officer.first_name,
                    'last_name': db_officer.last_name,
                    'rank': db_officer.rank
                }
                if db_officer not in spaceship['officers']:
                    return False
    return True


def insert_spaceships(spaceship: dict):
    with session_factory() as session:
        if is_duplicate(spaceship):
            print("is_duplicate")
            return
        print("is_not_duplicate")
        db_spaceship = TableSpaceship(
            alignment=spaceship['alignment'],
            name=spaceship['name'],
            ship_class=spaceship['class'],
            length=spaceship['length'],
            crew_size=spaceship['crew_size'],
            armed=spaceship['armed']
        )
        session.add(db_spaceship)
        session.commit()

        for officer in spaceship['officers']:
            db_officer = TableOfficers(
                first_name=officer['first_name'],
                last_name=officer['last_name'],
                rank=officer['rank'],
                ship_id=db_spaceship.id,
            )
            session.add(db_officer)
        session.commit()


def get_officers(alignment: str):
    with session_factory() as session:
        result_query = session.query(TableOfficers).join(TableSpaceship).filter(TableSpaceship.alignment == alignment).all()
        result_officers = [
            {
                "first_name": officer.first_name,
                "last_name": officer.last_name,
                "rank": officer.rank,
            } for officer in result_query
        ]
        return result_officers


def get_traitors():
    traitors: list = []
    ally_officers = get_officers('Ally')
    enemy_officers = get_officers("Enemy")
    for ally_officer in ally_officers:
        if ally_officer in enemy_officers and ally_officer not in traitors:
            traitors.append(ally_officer)
    return traitors


def create_table():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
