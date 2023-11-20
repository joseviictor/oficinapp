
from clientes import *
from faturas import *
from io_terminal import pause, pergunta_id
from materiais import *
from servicos import *
from veiculos import *
from ordens_reparacao import *
from bd import *

def menu():
    """Menu principal da aplicação"""
    db_creator()
    while True:
        print("""
        ---------------------------------------------------------------------
        |                            OFICINAPP                              |
        ---------------------------------------------------------------------
        | Home                                                              |
        |                                                                   |
        | [1] - Clientes                                                    |
        | [2] - Veículos                                                    |
        | [3] - Ordens de reparação                                         |      
        | [4] - Faturas                                                     |
        | [5] - Produtos                                                    |      
        |                                                                   |
        | [x] - Sair                                                        |
        ---------------------------------------------------------------------
        """)
        op = input("[OPÇÃO] ").lower()
        if op == "x":
            exit()
        elif op == "1":
            menu_cliente()
        elif op == "2":
            menu_veiculo()
        elif op == "3":
            menu_or()
        elif op == "4":
            menu_fatura()
        elif op == "5":
            menu_produtos()
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
            db_add_Cliente(input('Nome do cliente: '), input('nif: '), input('cc: '), input('dob: '), input('morada: '), input('telefone: '), input('v_email: '))
        elif op == "2":
            """TODO Implementar atualização de cliente"""
            db_update('CLIENTE', db_getfields('CLIENTE'), input('INSIRA O VALOR: '), db_getfields('CLIENTE'), '=', input('INSIRA O VALOR: '))
        elif op == "3":
            db_delete('CLIENTE', db_getfields('CLIENTE'), '=', input('INSIRA O VALOR: '))
            
        elif op == "4":
            db_show('CLIENTE')
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
            db_add_veiculo(input('marca: '), input('modelo: '), input('matricula: '), input('combustivel: '), input('ano: '), input('kms: '), input('cilindrada: '), input('cor: '), input('observacoes: '))
        elif op == "2":
            """TODO Implementar atualização de VEICULO"""
            db_update('VEICULO', db_getfields('VEICULO'), input('INSIRA O VALOR: '), db_getfields('VEICULO'), '=', input('INSIRA O VALOR: '))
        elif op == "3":
            db_delete('VEICULO', db_getfields('VEICULO'), '=', input('INSIRA O VALOR: '))
            
        elif op == "4":
            db_show('VEICULO')
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
            db_add_ordem_reparacoes(input('id_cliente_or: '), input('id_veiculo_or: '), input('data_or: '), input('serviços: '))
        elif op == "2":
            """TODO Implementar atualização de ORDEM_REPARACOES"""
            db_update('ORDEM_REPARACOES', db_getfields('ORDEM_REPARACOES'), input('INSIRA O VALOR: '), db_getfields('ORDEM_REPARACOES'), '=', input('INSIRA O VALOR: '))
        elif op == "3":
            db_delete('ORDEM_REPARACOES', db_getfields('ORDEM_REPARACOES'), '=', input('INSIRA O VALOR: '))
            
        elif op == "4":
            db_show('ORDEM_REPARACOES')
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
            db_add_fatura(input('id_cliente_or: '), input('id_veiculo_or: '), input('data_or: '), input('serviços: '))
        elif op == "2":
            """TODO Implementar atualização de fatura"""
            db_update('FATURA', db_getfields('FATURA'), input('INSIRA O VALOR: '), db_getfields('FATURA'), '=', input('INSIRA O VALOR: '))
        elif op == "3":
            db_delete('FATURA', db_getfields('FATURA'), '=', input('INSIRA O VALOR: '))
            
        elif op == "4":
            db_show('FATURA')
            pause()
def menu_produtos():
    while True:
        print("""
        ---------------------------------------------------------------------
        |                            OFICINAPP                              |
        ---------------------------------------------------------------------
        | Home > Produtos                                                   |
        |                                                                   |
        | [1] - Novo material                  [5] - Novo serviço           |
        | [2] - Atualizar material             [6] - Atualizar serviço      |
        | [3] - Remover material               [7] - Remover serviço        |
        | [4] - Listagem de material           [8] - Listagem de serviços   |
        |                                                                   |
        | [x] - Voltar                                                      |
        ---------------------------------------------------------------------
        """)
        op = input("[OPÇÃO] ").lower()
        if op == "x":
            break
        elif op == "1":
            db_add_material(input('material: '), input('custo: '), input('preço: '), input('fornecedor: '), input('telefone: '), input('email: '), input('part_number: '))
        elif op == "2":
            """TODO Implementar atualização de material"""
            db_update('MATRIAL', db_getfields('MATRIAL'), input('INSIRA O VALOR: '), db_getfields('MATRIAL'), '=', input('INSIRA O VALOR: '))
        elif op == "3":
            db_delete('MATRIAL', db_getfields('MATRIAL'), '=', input('INSIRA O VALOR: '))
            
        elif op == "4":
            db_show('MATRIAL')
            pause()
        
        elif op == "5":
            """TODO Implementar criação de serviço"""
            db_add_servico(input('servico: '), input('preco: '), input('observacao: '))
        elif op == "6":
            """TODO Implementar atualização de serviço"""
            db_update('SERVICO', db_getfields('SERVICO'), input('INSIRA O VALOR: '), db_getfields('SERVICO'), '=', input('INSIRA O VALOR: '))
        elif op == "7":
            db_delete('SERVICO', db_getfields('SERVICO'), '=', input('INSIRA O VALOR: '))
            
        elif op == "8":
            """TODO Implementar listagem de serviço"""
            db_show('SERVICO')
            pause()
if __name__ == "__main__":
    menu()
