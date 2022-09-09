import requests
import re


def get_cep_infos(baseurl, endpoint, midpoint):
    while iscepvalid(midpoint):
        print('Invalid cep (Only numbers and no punctuation)')
        user = input('Type again: ')
        if not iscepvalid(user):
            midpoint = user
            break
        else:
            continue

    while cepnotfound(baseurl, endpoint, midpoint):
        print('Cep not found')
        user = input('Type again: ')
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
