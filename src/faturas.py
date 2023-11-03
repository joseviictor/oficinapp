from datetime import date

from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"

def cria_nova_fatura(lista_de_clientes, lista_de_veiculos):
    """Pede ao utilizador para introduzir os dados de uma nova fatura

    :return: dicionario com uma fatura, na forma
        {"cliente": <<id_cliente>>, "veiculo": <<id_veiculo>>, "data": <<data>>, ...}
    """

    id_cliente = pergunta_id(questao="Qual o id do cliente?", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="Qual o id do veiculo?", lista=lista_de_veiculos, mostra_lista=True)

    # TODO: Pedir o resto dos dados da fatura, e não esquecer de os guardar no dicionario
    # ...

    fatura = {"cliente": id_cliente,
              "veiculo": id_veiculo,
              "data": date.today()}

    return fatura

def remover_fatura(lista_de_faturas):
    id_fatura = pergunta_id(questao="> ID da fatura: ", lista=lista_de_faturas, mostra_lista=True)
    if id_fatura is not None:
        lista_de_faturas.pop(id_fatura)

    return lista_de_faturas

def imprime_lista_de_faturas(lista_de_faturas):
    """TODO: documentação"""

    imprime_lista(cabecalho="Lista de faturas", lista=lista_de_faturas)