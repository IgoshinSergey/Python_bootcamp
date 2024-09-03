from collections import deque
import argparse
import json
import os
import logging

parser = argparse.ArgumentParser()
parser.add_argument("--from", help="source of walking", default="Abdus Salam")
parser.add_argument("--to", help="destination of walking", default="Franklin Matthias")
parser.add_argument(
    "--non-directed", action="store_true", help="destination of walking"
)
parser.add_argument("-v", action="store_true", help="logging")


def print_path(found_path: list) -> None:
    logging.basicConfig(level=logging.INFO)
    found = ""
    for vertex in found_path:
        found += vertex
        if vertex != found_path[-1]:
            found += " -> "
    logging.info(found)


def find_shortest_path(graph: dict, start: str, end: str, args) -> list | None:
    if start == end:
        return [start]

    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_vertex, path = queue.popleft()

        if current_vertex == end:
            return path

        if current_vertex in graph:
            for neighbor in graph[current_vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

                if args.non_directed:
                    keys_of_val = [key for key, val in graph.items() if neighbor in val]
                    for key in keys_of_val:
                        if key not in visited:
                            queue.append((key, path + [key]))
                            visited.add(key)

            visited.add(current_vertex)

    return None


def process_file(file_path: str, args) -> list | None:
    try:
        graph = {}
        with open(file_path) as file:
            graph = json.load(file)
        path = find_shortest_path(
            graph, getattr(args, "from"), getattr(args, "to"), args
        )
    except FileNotFoundError:
        print("Data not found")
        return None
    return path


def main():
    args = parser.parse_args()

    file_path = os.getenv("WIKI_FILE")

    path = process_file(file_path, args)

    if path is None:
        print("Path not found")
    else:
        print(f"length: {len(path)}")
        if args.v:
            print_path(path)


if __name__ == "__main__":
    main()

# WIKI_FILE='result.json' python3 shortest_path.py -v
# WIKI_FILE='result.json' python3 shortest_path.py -v --from 'Erdős number'
# WIKI_FILE='result.json' python3 shortest_path.py --from 'Abdus Salam' --to 'Franklin Matthias'
# WIKI_FILE='result.json' python3 shortest_path.py -v --from 'Erdős number' --to 'Hans Georg Dehmelt' --non-directed
