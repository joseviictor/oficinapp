from clientes import cria_novo_cliente, imprime_lista_de_clientes
from faturas import cria_nova_fatura, imprime_lista_de_faturas
from io_ficheiros import (carrega_as_listas_dos_ficheiros, guarda_as_listas_em_ficheiros)
from io_terminal import pause, pergunta_id
from veiculos import cria_novo_veiculo, imprime_lista_de_veiculos
from ordens_reparacao import cria_nova_or, imprime_lista_de_or

lista_de_veiculos = []
lista_de_clientes = []
lista_de_faturas = []
lista_de_or = []

def menu():
    """Menu principal da aplicação"""

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

def menu_cliente():
    while True:
        print("""
        ---------------------------------------------------------------------
        |                            OFICINAPP                              |
        ---------------------------------------------------------------------
        | Home > Cliente                                                    |
        |                                                                   |
        | [1] - Novo cliente                                                |
        | [2] - Atualizar cliente                                           |
        | [3] - Remover cliente                                             |
        | [4] - Listagem de clientes                                        |
        |                                                                   |
        | [x] - Voltar                                                      |
        ---------------------------------------------------------------------
        """)

        op = input("[OPÇÃO] ").lower()

        if op == "x":
            break

        elif op == "1":
            novo_cliente = cria_novo_cliente()
            if novo_cliente is not None:
                lista_de_clientes.append(novo_cliente)

        elif op == "2":
            """TODO Implementar atualização de cliente"""
            pass

        elif op == "3":
            id_cliente = pergunta_id(questao="> ID do cliente: ", lista=lista_de_clientes, mostra_lista=True)
            if id_cliente is not None:
                lista_de_clientes.pop(id_cliente)
            
        elif op == "4":
            imprime_lista_de_clientes(lista_de_clientes)
            pause()

def menu_veiculo():
    while True:
        print("""
        ---------------------------------------------------------------------
        |                            OFICINAPP                              |
        ---------------------------------------------------------------------
        | Home > Veículos                                                   |
        |                                                                   |
        | [1] - Novo veículo                                                |
        | [2] - Atualizar veículo                                           |
        | [3] - Remover veículo                                             |
        | [4] - Listagem de veículos                                        |
        |                                                                   |
        | [x] - Voltar                                                      |
        ---------------------------------------------------------------------
        """)

        op = input("[OPÇÃO] ").lower()

        if op == "x":
            break

        elif op == "1":
            novo_veiculo = cria_novo_veiculo()
            if novo_veiculo is not None:
                lista_de_veiculos.append(novo_veiculo)

        elif op == "2":
            """TODO Implementar atualização de veículo"""
            pass

        elif op == "3":
            id_veículo = pergunta_id(questao="> ID do veículo: ", lista=lista_de_veiculos, mostra_lista=True)
            if id_veículo is not None:
                lista_de_veiculos.pop(id_veículo)
            
        elif op == "4":
            imprime_lista_de_veiculos(lista_de_veiculos)
            pause()

def menu_or():
    while True:
        print("""
        ---------------------------------------------------------------------
        |                            OFICINAPP                              |
        ---------------------------------------------------------------------
        | Home > Ordens de Reparação                                        |
        |                                                                   |
        | [1] - Nova ordem de reparação                                     |
        | [2] - Atualizar ordem de reparação                                |
        | [3] - Remover ordem de reparação                                  |
        | [4] - Listagem de ordens de reparação                             |
        |                                                                   |
        | [x] - Voltar                                                      |
        ---------------------------------------------------------------------
        """)

        op = input("[OPÇÃO] ").lower()

        if op == "x":
            break

        elif op == "1":
            if len(lista_de_clientes) == 0 or len(lista_de_veiculos) == 0:
                print("Não há clientes ou veiculos registados...")
                continue
            nova_or = cria_nova_or(lista_de_clientes, lista_de_veiculos)
            lista_de_or.append(nova_or)

        elif op == "2":
            """TODO Implementar atualização de or"""
            pass

        elif op == "3":
            id_or = pergunta_id(questao="> ID da ordem de reparação: ", lista=lista_de_or, mostra_lista=True)
            if id_or is not None:
                lista_de_or.pop(id_or)
            
        elif op == "4":
            imprime_lista_de_or(lista_de_or)
            pause()

def menu_fatura():
    while True:
        print("""
        ---------------------------------------------------------------------
        |                            OFICINAPP                              |
        ---------------------------------------------------------------------
        | Home > Faturas                                                    |
        |                                                                   |
        | [1] - Nova fatura                                                 |
        | [2] - Atualizar fatura                                            |
        | [3] - Remover fatura                                              |
        | [4] - Listagem de faturas                                         |
        |                                                                   |
        | [x] - Voltar                                                      |
        ---------------------------------------------------------------------
        """)

        op = input("[OPÇÃO] ").lower()

        if op == "x":
            break

        elif op == "1":
            if len(lista_de_clientes) == 0 or len(lista_de_veiculos) == 0:
                print("Não há clientes ou veiculos registados...")
                continue

            nova_fatura = cria_nova_fatura(lista_de_clientes, lista_de_veiculos)
            lista_de_faturas.append(nova_fatura)

        elif op == "2":
            """TODO Implementar atualização de or"""
            pass

        elif op == "3":
            id_fatura = pergunta_id(questao="> ID da fatura: ", lista=lista_de_faturas, mostra_lista=True)
            if id_fatura is not None:
                lista_de_faturas.pop(id_fatura)
            
        elif op == "4":
            imprime_lista_de_faturas(lista_de_faturas)
            pause()

if __name__ == "__main__":
    menu()
