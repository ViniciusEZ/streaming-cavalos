# id ,usuário ,Nome, sobrenome, idade, cpf, cep, logradouro, bairro, localidade ,Número da casa, senha
import re
from app.entrypoints.api_requests import get_cep_infos

def iscpfvalid(cpf):
    recpf = re.match(r'[0-9]{11}', cpf)
    if recpf is None:
        return True


def collect_info(baseurl, endpoint, midpoint):
    response = get_cep_infos(baseurl, endpoint, midpoint)
    infos = {
        'logradouro': response['logradouro'],
        'bairro': response['bairro'],
        'localidade': response['localidade']
    }
    return infos




