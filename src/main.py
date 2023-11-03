from clientes import cria_novo_cliente, imprime_lista_de_clientes
from faturas import cria_nova_fatura, imprime_lista_de_faturas
from io_ficheiros import (carrega_as_listas_dos_ficheiros, guarda_as_listas_em_ficheiros)
from io_terminal import pause
from veiculos import cria_novo_veiculo, imprime_lista_de_veiculos
from ordens_reparacao import cria_nova_or, imprime_lista_de_or

def menu():
    """Menu principal da aplicação"""

    lista_de_veiculos = []
    lista_de_clientes = []
    lista_de_faturas = []
    lista_de_or = []

    while True:
        print("""
        ---------------------------------------------------------------------
        |                            OFICINAPP                              |
        ---------------------------------------------------------------------
        |                                                                   |
        | [1] - Novo cliente         [5] - Listagem de clientes             |
        | [2] - Novo veiculo         [6] - Listagem de veiculos             |
        | [3] - Nova OR              [7] - Listagem de ordens de reparação  |      
        | [4] - Nova fatura          [8] - Listagem das faturas             |
        |                                                                   |
        | [g] - Guarda tudo          [c] - Carrega tudo                     |
        | [x] - Sair                                                        |
        |                                                                   |
        ---------------------------------------------------------------------
        """)

        op = input("[OPÇÃO] ").lower()

        if op == "x":
            exit()

        elif op == "g":
            guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_or, lista_de_faturas)

        elif op == "c":
            lista_de_veiculos, lista_de_clientes, lista_de_faturas = carrega_as_listas_dos_ficheiros()

        elif op == "1":
            novo_cliente = cria_novo_cliente()
            if novo_cliente is not None:
                lista_de_clientes.append(novo_cliente)

        elif op == "2":
            novo_veiculo = cria_novo_veiculo()
            if novo_veiculo is not None:
                lista_de_veiculos.append(novo_veiculo)

        elif op == "3":
            if len(lista_de_clientes) == 0 or len(lista_de_veiculos) == 0:
                print("Não há clientes ou veiculos registados...")
                continue
            nova_or = cria_nova_or(lista_de_clientes, lista_de_veiculos)
            lista_de_or.append(nova_or)

        elif op == "4":
            if len(lista_de_clientes) == 0 or len(lista_de_veiculos) == 0:
                print("Não há clientes ou veiculos registados...")
                continue

            nova_fatura = cria_nova_fatura(lista_de_clientes, lista_de_veiculos)
            lista_de_faturas.append(nova_fatura)

        elif op == "5":
            imprime_lista_de_clientes(lista_de_clientes)
            pause()

        elif op == "6":
            imprime_lista_de_veiculos(lista_de_veiculos)
            pause()

        elif op == "7":
            imprime_lista_de_or(lista_de_or)
            pause()

        elif op == "8":
            imprime_lista_de_faturas(lista_de_faturas)
            pause()

if __name__ == "__main__":
    menu()
