import protobuf.spaceship_pb2 as pb2
import protobuf.spaceship_pb2_grpc as pb2_grpc
import grpc
import random
from concurrent import futures


class Server(pb2_grpc.SpaceshipService):
    def get_spaceships(self, request, context):
        print(f"Coordinates request: {request.coord}")
        for _ in range(10):
            alignment: pb2.Alignment = random.choice([0, 1])
            min_officers = 0 if alignment == 1 else 1
            count_officers = range(random.randint(min_officers, 10))
            spaceship = pb2.Spaceship(**{
                "alignment": alignment,
                "name": random.choice(["Normandy", "Executor", "Mercury", "Apollo"]),
                "length": random.uniform(50, 30000),
                "class_ship": random.randint(0, 5),
                "crew_size": random.randint(1, 500),
                "armed": random.choice([True, False]),
                "officers": [{
                    "first_name": random.choice(["Anna", "Robert", "Denis", "Bob"]),
                    "last_name": random.choice(["Brown", "Smith", "Taylor", "Jones"]),
                    "rank": random.choice(["Captain", "Major", "Lieutenant"])
                    } for _ in count_officers
                ]}
            )
            yield spaceship


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SpaceshipServiceServicer_to_server(Server(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
