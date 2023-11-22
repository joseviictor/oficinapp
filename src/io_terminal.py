
from tabulate import tabulate
def imprime_lista(cabecalho, linhas):
    """
    Imprime a lista na forma de uma tabela com um cabeçalho.

    Recebe uma lista na forma [{"atrib1": valor1, "atrib2": valor2, ...},
    {"atrib1": valor1, "atrib2": valor2, ...}, ...] e imprime no terminal uma tabela.

    Exemplo:
    ==  ======  ======
    id  atrib1  atrib2
    ==  ======  ======
    0   valor1  valor2
    1   ...      ...
    ==  ======  ======

    :param cabecalho: Lista contendo o cabeçalho para a listagem.
    :type cabecalho: list
    :param lista: Lista a ser impressa.
    :type lista: list
    
    """
    #print(cabecalho)
    lista = [dict(zip(cabecalho, linha)) for linha in linhas]
    if (len(lista) == 0):
        print("Lista vazia")
    else:
        # cabecalho da tabela
        lista_a_imprimir = [["id"] + list(lista[0].keys())]
        # dados
        lista_a_imprimir.extend([[id] + list(d.values()) for id, d in enumerate(lista)])
        print(tabulate(lista_a_imprimir, headers="firstrow", tablefmt='psql'))
    pause()
def pause():
    """Faz uma pausa no programa e espera que o utilizador pressione ENTER"""
    input("Pressione ENTER para continuar...")
def pergunta_id(questao, lista, mostra_lista=False):
    """     
    Realiza uma pergunta ao utilizador para selecionar um ID da lista.

    Se `mostra_lista` for True, imprime a lista na forma de uma tabela antes de fazer a pergunta.

    :param questao: A pergunta a ser exibida ao utilizador.
    :param lista: Lista de itens a partir da qual o utilizador escolherá um ID.
    :param mostra_lista: Sinaliza se a lista deve ser impressa antes da pergunta.
    :type mostra_lista: bool
    :return: O ID selecionado pelo utilizador.
    :rtype: int
    
    """
    if mostra_lista:
        imprime_lista(cabecalho="", lista=lista)
    while True:
        id = int(input(questao))
        if 0 <= id < len(lista):
            return id
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")
