import pytest
from elasticsearch import Elasticsearch
from data_storage.input_values import URL_ELASTIC
from logic.base_logic import now_date, now_date_file_name
from schemas.query import query
from data_storage.input_values import KOMS, MINE, PATH_TO_FILE


def pytest_addoption(parser):
    parser.addoption(
        "--server", default="koms", help="Get logs from server komsomol"
    )
    parser.addoption(
        "--write", default=False, help="Write to file"
    )


@pytest.fixture
def server_name(request):
    return request.config.getoption("--server")


@pytest.fixture
def select_server(request):
    es = Elasticsearch(URL_ELASTIC)
    server_name = request.config.getoption("--server")
    write_file = request.config.getoption("--write")

    if server_name == "koms":
        resp = es.search(index=f"{KOMS}{now_date}", query=query)
        for r in resp['hits']['hits']:
            output_data = r['_source']['log']
            print(output_data)
        if write_file:
            for r in resp['hits']['hits']:
                output_data = r['_source']['log']
                print(output_data)
                with open(f"{PATH_TO_FILE}_{server_name}_{now_date_file_name}.txt", 'w+') as file:
                    file.write(output_data)

    elif server_name == "mine":
        resp = es.search(index=f"{MINE}{now_date}", query=query)
        for r in resp['hits']['hits']:
            output_data = r['_source']['log']
            print(output_data)
        if write_file:
            for r in resp['hits']['hits']:
                output_data = r['_source']['log']
                print(output_data)
                with open(f"{PATH_TO_FILE}{server_name}_{now_date_file_name}.txt", 'w+') as file:
                    file.write(output_data)
                    file.close()

    else:
        raise ValueError("Введите наименование сервера koms или mine")
