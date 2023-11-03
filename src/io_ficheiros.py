import os
import pickle

from clientes import nome_ficheiro_lista_de_clientes
from faturas import nome_ficheiro_lista_de_faturas
from ordens_reparacao import nome_ficheiro_lista_de_or
from veiculos import nome_ficheiro_lista_de_veiculos
from materiais import nome_ficheiro_lista_de_materiais
from servicos import nome_ficheiro_lista_de_serviços


def carrega_as_listas_dos_ficheiros():
    """TODO: documentação"""

    lista_de_veiculos = le_de_ficheiro(nome_ficheiro_lista_de_veiculos)
    lista_de_clientes = le_de_ficheiro(nome_ficheiro_lista_de_clientes)
    lista_de_or = le_de_ficheiro(nome_ficheiro_lista_de_or)
    lista_de_faturas = le_de_ficheiro(nome_ficheiro_lista_de_faturas)
    lista_de_materiais = le_de_ficheiro(nome_ficheiro_lista_de_materiais)
    lista_de_serviços = le_de_ficheiro(nome_ficheiro_lista_de_serviços)

    return  lista_de_veiculos, lista_de_clientes, lista_de_or, lista_de_faturas, lista_de_materiais, lista_de_serviços

def guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_or, lista_de_faturas, lista_de_materiais, lista_de_serviços):
    """TODO: documentação

    :param lista_de_clientes:
    :param lista_de_veiculos:
    :param lista_de_or:
    :param lista_de_faturas:
    :param lista_de_materiais:
    :param lista_de_serviços:
    """
    guarda_em_ficheiro(nome_ficheiro_lista_de_veiculos, lista_de_veiculos)
    guarda_em_ficheiro(nome_ficheiro_lista_de_clientes, lista_de_clientes)
    guarda_em_ficheiro(nome_ficheiro_lista_de_or, lista_de_or)
    guarda_em_ficheiro(nome_ficheiro_lista_de_faturas, lista_de_faturas)
    guarda_em_ficheiro(nome_ficheiro_lista_de_materiais, lista_de_materiais)
    guarda_em_ficheiro(nome_ficheiro_lista_de_serviços, lista_de_serviços)

def guarda_em_ficheiro(nome_do_ficheiro, dados):
    """Guarda os dados recebidos num ficheiro

    :param nome_do_ficheiro: nome do ficheiro onde vai guardar os dados
    :param dados: dados a serem guardados
    """

    with open(nome_do_ficheiro, "wb") as f:
        pickle.dump(dados, f)
        
def le_de_ficheiro(nome_ficheiro):
    """Lê os dados de um ficheiro

    :param nome_ficheiro: nome do ficheiro onde estao os dados
    :return: o que leu do ficheiro (depende dos dados guardados)
    """
    if os.path.isfile(nome_ficheiro):
        with open(nome_ficheiro, "rb") as f:
            return pickle.load(f)
