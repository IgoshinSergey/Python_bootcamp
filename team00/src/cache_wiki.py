import wikipedia
import warnings
import argparse
import json
import logging

parser = argparse.ArgumentParser()

parser.add_argument("-p", dest="current_page", default="Giraffe")
parser.add_argument("-d", dest="max_depth", default=3, type=int)


def find_pages(
    all_pages: dict, current_page: str, links: set, curr_depth: int, max_depth: int
) -> None:
    logging.basicConfig(level=logging.INFO)
    logging.info(all_pages)
    all_pages[current_page] = set()
    for link in links:
        if len(all_pages) >= 1000:
            return
        if curr_depth >= max_depth:
            break
        try:
            page = wikipedia.page(link, auto_suggest=False)
        except (Exception, Warning) as error:
            continue
        if link not in all_pages:
            find_pages(all_pages, link, page.links, curr_depth + 1, max_depth)
        all_pages[current_page].add(link)


def get_page(page_name):
    try:
        page = wikipedia.page(page_name, auto_suggest=False)
    except wikipedia.PageError as error:
        logging.error("No such page")
        exit()

    return page


def create_result_file(all_pages: dict):
    if len(all_pages) >= 20:
        all_pages = {key: list(val) for key, val in all_pages.items()}
        with open("result.json", "w") as file:
            json.dump(all_pages, file)
    else:
        print(
            "Count of links is less than 20. Please choose another default start page"
        )


def main():
    logging.basicConfig(level=logging.INFO)
    args = parser.parse_args()

    page = get_page(args.current_page)
    links: set = page.links
    all_pages = {}

    find_pages(all_pages, args.current_page, links, 0, args.max_depth)

    create_result_file(all_pages)


if __name__ == "__main__":
    main()

# python3 cache_wiki.py -p 'Erdős number'
