import constant
import requests
import json


def get(path_params, token, query_params=None):
    if query_params is None:
        query_params = {}
    resp = requests.get(url=_geturl(path_params), params={**_get_token_query(token), **query_params})
    if resp.status_code not in [200, 201]:
        raise Exception('Incorrect response code.', resp.text)
    return json.loads(requests.get(url=_geturl(path_params), params={**_get_token_query(token), **query_params}).text)


def _geturl(path_params):
    constructed_path = ''
    for param in path_params:
        constructed_path += param + '/'
    return constant.GRAPH_ENDPOINT + constructed_path


def _get_token_query(token):
    return {'access_token': token}
