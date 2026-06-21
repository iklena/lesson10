import json

import pytest
import requests
# from urllib3.contrib.emscripten import response

from lists.lists_api_helper import ListsApiHelper

headers_variable = {
    'Authorization': 'pk_302428217_Q0SH3L1KRFHUY6Z5W0FON35SHCRQ3TOH',
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# fixture - выполняются до наших тестов
#

# @pytest.fixture
# # создаём метод для считывания id листа из файла
# def get_list_id():
#     with open('./test_lists.json', 'r') as json_file:
#         json_data = json.load(json_file)
#         list_id = json_data['id']
#         return list_id
#
# def test_get_list_request(get_list_id):
#     # # считываем данные из файла без fixture
#     # with open('./test_lists.json', 'r') as json_file:
#     #     json_data = json.load(json_file)
#     #     list_id = json_data['id']
#     print(get_list_id)
#
#     # response_for_get_list = requests.get('https://api.clickup.com/api/v2/list/' + list_id, headers = headers_variable)
#     # print('Check a Status Code response_for_get_list: ', response_for_get_list.status_code)
#     # assert response_for_get_list.status_code == 200
#     # assert response_for_get_list.json()['id'] == '901417264550'


@pytest.fixture(scope='module')
def client():
    session = requests.Session()
    session.headers.update(headers_variable)
    return session

def test_get_list_request1(client):
# def test_get_list_request1():
    list_helpers = ListsApiHelper()
    response_get = list_helpers.get_list('901417264711')

    print('Check a Status Code response_for_get_list: ', response_get.status_code)
    assert response_get.status_code == 200, 'Expected status code 200. Actual status code ' + str(response_get.status_code) + ' and body ' + response_get.text
