import protobuf.spaceship_pb2_grpc as pb2_grpc
import protobuf.spaceship_pb2 as pb2

import argparse
import grpc
import json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("coordinates", type=float, nargs='+')
    return parser.parse_args().coordinates


def get_ships(channel, coords):
    stub = pb2_grpc.SpaceshipServiceStub(channel)
    for ship in stub.get_spaceships(pb2.Coordinates(coord=coords)):
        yield (
            json.dumps({
                'alignment': pb2.Alignment.Name(ship.alignment),
                'name': ship.name,
                'class': pb2.ClassShip.Name(ship.class_ship),
                'length': round(ship.length, 1),
                'crew_size': ship.crew_size,
                'armed': ship.armed,
                'officers': [{
                    'first_name': officer.first_name,
                    'last_name': officer.last_name,
                    'rank': officer.rank,
                } for officer in ship.officers]
            }, indent=4)
        )


def print_spaceships(coords: list[float]):
    with grpc.insecure_channel('localhost:50051') as channel:
        for ship in get_ships(channel, coords):
            print(ship)


if __name__ == "__main__":
    coordinates: list[float] = parse_args()
    print_spaceships(coordinates)
