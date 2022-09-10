# usuário ,Nome, sobrenome, idade, cpf, cep, logradouro, bairro, localidade ,Número da casa, senha
import re
from app.entrypoints.api_requests import get_cep_infos
import sqlite3


def collect_info(baseurl, endpoint, midpoint):
    response = get_cep_infos(baseurl, endpoint, midpoint)
    infos = {
        'logradouro': response['logradouro'],
        'bairro': response['bairro'],
        'localidade': response['localidade']
    }
    return infos


def iscpfvalid(cpf):
    recpf = re.match(r'[0-9]{11}', cpf)
    if recpf is None:
        return True


def ispasswordvalid(password):
    regex = re.match(r'(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[0-9]+)(?=.*[ -\/:-@[-`{-~]+).{6,}', password)
    if regex is None:
        return True


def isuserexistent(vcon, username):
    connection = vcon.cursor()
    connection.execute('SELECT usuario FROM UserData WHERE usuario=?', (username,))
    res = connection.fetchone()
    return res


def isthesamecpf(vcon, cpf):
    connection = vcon.cursor()
    connection.execute('SELECT cpf FROM UserData WHERE cpf=?', (cpf,))
    res = connection.fetchone()
    return res
