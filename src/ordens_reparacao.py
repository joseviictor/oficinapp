from datetime import date
from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_or = "lista_de_or.pk"

def cria_nova_or(lista_de_clientes, lista_de_veiculos, lista_de_serviços, lista_de_materiais):
    """Pede ao utilizador para introduzir uma nova ordem de reparação

    :return: dicionario com uma OR
    """
    serviços_da_or = []
    materiais_da_or = []

    id_cliente = pergunta_id(questao="> ID do cliente: ", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="> ID do veiculo: ", lista=lista_de_veiculos, mostra_lista=True)

    produtos_a_faturar(serviços_da_or, lista_de_serviços, "serviço")
    produtos_a_faturar(materiais_da_or, lista_de_materiais, "material")
    
    ordem_reparacao = {
              "cliente": id_cliente,
              "veiculo": id_veiculo,
              "data": date.today(),
              "serviços": serviços_da_or,
              "materiais": materiais_da_or
              }

    return ordem_reparacao

def imprime_lista_de_or(lista_de_or):
    """TODO: documentação"""

    imprime_lista(cabecalho="\nLista de Ordens de Reparação", lista=lista_de_or)

def produtos_a_faturar(produtos_da_or, lista_de_produtos, tipo):
    
    imprime_lista(cabecalho = "\nLista de " + tipo, lista=lista_de_produtos)

    option = "s"

    while option == "s":
        try:
            id = pergunta_id(questao="> ID do "+ tipo + ": ", lista=lista_de_produtos, mostra_lista=False)
            produtos_da_or.append(id)
            option = input("\n> Deseja inserir outro " + tipo + "(s/n)? ")
        except:
            print("> ID inválido.")