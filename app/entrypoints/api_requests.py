import requests
import re


def get_cep_infos(baseurl, endpoint, midpoint):
    while iscepvalid(midpoint):
        print('CEP inválido (apenas números).')
        user = input('Digite novamente: ')
        if not iscepvalid(user):
            midpoint = user
            break
        else:
            continue

    while cepnotfound(baseurl, endpoint, midpoint):
        print('CEP não encontrado.')
        user = input('Digite novamente: ')
        midpoint = user
        if not cepnotfound(baseurl, endpoint, midpoint):
            break
        else:
            continue

    r = requests.get(baseurl + f'{midpoint}' + endpoint)
    return r.json()


def iscepvalid(cep):
    regex = re.compile(r'[0-9]{8}')
    if re.match(regex, cep) is None:
        return True


def cepnotfound(baseurl, endpoint, midpoint):
    r = requests.get(baseurl + f'{midpoint}' + endpoint).json()
    if r.get('erro'):
        return True
