from random import randrange
from typing import Dict
from json import dumps
import logging
import redis


def generate_message() -> str:
    from_message: int = randrange(1000000000, 9999999999, 1000000000)
    to_message: int = randrange(1000000000, 9999999999, 1000000000)
    amount: int = randrange(-10000, 10000, 1000)

    message: Dict = {
        "metadata": {
            "from": from_message,
            "to": to_message
        },
        "amount": amount
    }
    return dumps(message)


def main():

    redis_client = redis.Redis(host="localhost", port=6379)

    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.INFO)

    for i in range(10):
        message: str = generate_message()
        logger.info(f"Message generated: {message}")
        redis_client.publish("transactions", message)
        logger.info("The message has been sent")


if __name__ == '__main__':
    main()
