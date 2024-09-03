from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from json import dumps


def application(environ, start_response):
    all_species = {
        "Cyberman": "John Lumic",
        "Dalek": "Davros",
        "Judoon": "Shadow Proclamation Convention 15 Enforcer",
        "Human": "Leonardo da Vinci",
        "Ood": "Klineman Halpen",
        "Silence": "Tasha Lem",
        "Slitheen": "Coca-Cola salesman",
        "Sontaran": "General Staal",
        "Time Lord": "Rassilon",
        "Weeping Angel": "The Division Representative",
        "Zygon": "Broton"
    }
    data = dict()
    status_code = "200 OK"
    query_string = environ['QUERY_STRING']
    if query_string:
        params = parse_qs(query_string)
        species = params.get('species', None)
        if species and species[0] in all_species.keys():
            data = {"credentials": all_species[species[0]]}
        else:
            data = {"credentials": "Unknown"}
            status_code = "404 Not Found"

    json_data = dumps(data, ensure_ascii=False)
    start_response(status_code, [('Content-Type', 'application/json')])

    return [json_data.encode('UTF-8')]


host = 'localhost'
port = 8888

httpd = make_server(host, port, application)
httpd.handle_request()


# curl http://localhost:8888/?species=Cyberman
# curl http://localhost:8888/?species=Time%20Lord
