import requests


def get_cep_infos(baseurl, endpoint, midpoint):
    r = requests.get(baseurl + f'{midpoint}' + endpoint)
    return r.json()

