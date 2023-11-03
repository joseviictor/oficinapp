from datetime import date
from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_or = "lista_de_or.pk"

def cria_nova_or(lista_de_clientes, lista_de_veiculos):
    """Pede ao utilizador para introduzir uma nova ordem de reparação

    :return: dicionario com uma OR
    """
    lista_serviços = []
    id_cliente = pergunta_id(questao="> ID do cliente: ", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="> ID do veiculo: ", lista=lista_de_veiculos, mostra_lista=True)

    while True:
        id_serviço = input("> ID do serviço a realizar: ")
        if len(id_serviço) > 0:
            lista_serviços.append(id_serviço)
        else:
            break
    
    ordem_reparacao = {
              "cliente": id_cliente,
              "veiculo": id_veiculo,
              "data": date.today(),
              "serviços": lista_serviços
              }

    return ordem_reparacao

def imprime_lista_de_or(lista_de_or):
    """TODO: documentação"""

    imprime_lista(cabecalho="Lista de Ordens de Reparação", lista=lista_de_or)