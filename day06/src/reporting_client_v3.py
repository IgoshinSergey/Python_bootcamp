import argparse

from reporting_client_v2 import validate_spaceships
from alchemy.orm import insert_spaceships, get_traitors

from json import loads, dumps


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    scan_parser = subparsers.add_parser('scan')
    scan_parser.add_argument("coordinates", type=float, nargs='+')
    list_parser = subparsers.add_parser('list')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.command == 'scan':
        for validate_ship in validate_spaceships(args.coordinates):
            sh: dict = loads(validate_ship)
            print(sh)
            insert_spaceships(sh)
    elif args.command == 'list':
        print("traitors")
        for officer in get_traitors():
            print(dumps(officer))


