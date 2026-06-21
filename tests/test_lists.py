# import os

import requests
# from dotenv import load_dotenv
#
# load_dotenv()  # reads variables from a .env file and sets them in os.environ
#
# token = os.getenv("TOKEN")
# base_url = os.getenv("BASE_URL")
#
# url = base_url + "/folder/90149614048/list"

headers_variable = {
    'Authorization': 'pk_302428217_Q0SH3L1KRFHUY6Z5W0FON35SHCRQ3TOH',
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# def test_get_lists_request():
#     response = requests.get('https://api.clickup.com/api/v2/folder/90149614048/list', headers = headers_variable)
#
#     print('Check a Status Code: ', response.status_code)
#     assert response.status_code == 200
#     print('Check list ID:', response.json()['lists'][0]['id'])
#     assert response.json()['lists'][0]['id'] == '901417264711'
#     # print(response.json())


# def test_post_list_request():
#     response = requests.post('https://api.clickup.com/api/v2/folder/90149614048/list', headers = headers_variable, json = {"name": "test24425"})
#     print('Check a Status Code: ', response.status_code)
#     assert response.status_code == 200, 'Expected status code 200. Actual status code ' + str(response.status_code) + ' and body ' + response.text

def test_put_list_request():
    # Create a list
    # Update the list

    # Delete the list

    name = "tst_upd_new"
    response = requests.put('https://api.clickup.com/api/v2/list/901417264550', headers = headers_variable, json = {"name": name})
    print('Check a Status Code: ', response.status_code)
    assert response.status_code == 200, 'Expected status code 200. Actual status code ' + str(response.status_code) + ' and body ' + response.text
    print('Check list name:', response.json()['name'])
    assert response.json()['name'] == name
    print(response.json())

    response_for_get_list = requests.get('https://api.clickup.com/api/v2/list/901417264550', headers = headers_variable)
    print('Check a Status Code response_for_get_list: ', response_for_get_list.status_code)
    assert response_for_get_list.status_code == 200
    assert response_for_get_list.json()['name'] == name

