import requests


class ListsApiHelper:

    base_url = 'https://api.clickup.com/api/v2'
    headers_variable = {
        'Authorization': 'pk_302428217_Q0SH3L1KRFHUY6Z5W0FON35SHCRQ3TOH',
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    def get_list(self, list_id):
        response = requests.get(self.base_url + '/list/' + list_id, headers = self.headers_variable)
        return response