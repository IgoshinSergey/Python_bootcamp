from typing import Dict, List
from json import loads
import argparse
import redis
import logging


def list_of_ints(arg: str) -> List[int]:
    return list(map(int, arg.split(',')))


def parse_args() -> List[int]:
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', type=list_of_ints, required=True, help='Usage: consumer.py -e 1,2,3,4')
    args = parser.parse_args()
    return args.e


def check_message(log: logging.Logger,
                  message: Dict,
                  numbers: List[int]) -> None:
    metadata = message["metadata"]
    if metadata["to"] in numbers and message["amount"] >= 0:
        log.info("Swap \"to\" and \"from\" in message")
        metadata["to"], metadata["from"] = metadata["from"], metadata["to"]


def main():
    account_numbers = parse_args()

    redis_client = redis.Redis(host='localhost', port=6379)
    pubsub = redis_client.pubsub()
    pubsub.subscribe('transactions')

    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.INFO)

    for transaction in pubsub.listen():
        if transaction['type'] == 'message':
            data = loads(transaction['data'])
            check_message(logger, data, account_numbers)
            print(data)


if __name__ == '__main__':
    main()
