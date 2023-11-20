
from clientes import db_add_Cliente
from veiculos import db_add_veiculo
from ordens_reparacao import db_add_ordem_reparacoes
from faturas import db_add_fatura
from materiais import db_add_material
from servicos import db_add_servico
from bd import db_creator, db_getfields, db_show, db_update, db_delete
from io_terminal import imprime_lista
# ------------------------------------------------------------
def menu():
    """Menu principal da aplicação"""
    db_creator()
    opcoes_menu = [menu_cliente, menu_veiculo, menu_or, menu_fatura, menu_produtos]
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
        elif int(op) in range(1, 6):
            opcoes_menu[int(op)-1]()
# ------------------------------------------------------------
def menu_cliente():
    """Menu principal do Cliente"""
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
            """
            Implementar a criação de um Cliente
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_add_Cliente(input('Nome do cliente: '), input('nif: '), input('cc: '), input('dob: '), input('morada: '), input('telefone: '), input('v_email: '))
        elif op == "2":
            """
            Implementar a atualização de um Cliente
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_update('CLIENTE', db_getfields('CLIENTE'), input('INSIRA O VALOR PARA O QUAL DESEJA ALTERAR: '), db_getfields('CLIENTE'), '=', input('INSIRA O VALOR DA CONDIÇÃO: '))
        elif op == "3":
            """
            Implementar a eliminação de um Cliente
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_delete('CLIENTE', db_getfields('CLIENTE'), '=', input('INSIRA O VALOR DA CONDIÇÃO: '))
            
        elif op == "4":
            """
            Implementar a listagem dos Clientes existentes
            TODO: Implementaçao da verificação de dados invalidos
            """
            imprime_lista(db_getfields('CLIENTE', False), db_show('CLIENTE', False))
# ------------------------------------------------------------
def menu_veiculo():
    """Menu principal do Veiculo"""
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
            """
            Implementar a criação de um Veículo
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_add_veiculo(input('marca: '), input('modelo: '), input('matricula: '), input('combustivel: '), input('ano: '), input('kms: '), input('cilindrada: '), input('cor: '), input('observacoes: '))
        elif op == "2":
            """
            Implementar a atualização de um Veiculo
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_update('VEICULO', db_getfields('VEICULO'), input('INSIRA O VALOR PARA O QUAL DESEJA ALTERAR: '), db_getfields('VEICULO'), '=', input('INSIRA O VALOR DA CONDIÇÃO: '))
        elif op == "3":
            """
            Implementar a eliminação de um Veiculo
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_delete('VEICULO', db_getfields('VEICULO'), '=', input('INSIRA O VALOR DA CONDIÇÃO: '))
            
        elif op == "4":
            """
            Implementar a listagem dos Veiculos existentes
            TODO: Implementaçao da verificação de dados invalidos
            """
            imprime_lista(db_getfields('VEICULO', False), db_show('VEICULO', False))
# ------------------------------------------------------------
def menu_or():
    """Menu principal das Ordens de Reparação"""
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
            """
            Implementar a criação de uma Ordem de Reparação
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_add_ordem_reparacoes(input('id_cliente_or: '), input('id_veiculo_or: '), input('data_or: '), input('serviços: '))
        elif op == "2":
            """
            Implementar a atualização de uma Ordem de Reparação
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_update('ORDEM_REPARACOES', db_getfields('ORDEM_REPARACOES'), input('INSIRA O VALOR PARA O QUAL DESEJA ALTERAR: '), db_getfields('ORDEM_REPARACOES'), '=', input('INSIRA O VALOR DA CONDIÇÃO: '))
        elif op == "3":
            """
            Implementar a eliminação uma Ordem de Reparação
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_delete('ORDEM_REPARACOES', db_getfields('ORDEM_REPARACOES'), '=', input('INSIRA O VALOR DA CONDIÇÃO: '))
            
        elif op == "4":
            """
            Implementar a listagem das Ordens de Reparação existentes
            TODO: Implementaçao da verificação de dados invalidos
            """
            imprime_lista(db_getfields('ORDEM_REPARACOES', False), db_show('ORDEM_REPARACOES', False))
# ------------------------------------------------------------
def menu_fatura():
    """Menu principal da Fatura"""
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
            """
            Implementar a criação de uma Fatura
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_add_fatura(input('id_cliente_or: '), input('id_veiculo_or: '), input('data_or: '), input('serviços: '))
        elif op == "2":
            """
            Implementar a atualização de uma Fatura
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_update('FATURA', db_getfields('FATURA'), input('INSIRA O VALOR PARA O QUAL DESEJA ALTERAR: '), db_getfields('FATURA'), '=', input('INSIRA O VALOR DA CONDIÇÃO: '))
        elif op == "3":
            """
            Implementar a eliminação de uma Fatura
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_delete('FATURA', db_getfields('FATURA'), '=', input('INSIRA O VALOR DA CONDIÇÃO: '))
            
        elif op == "4":
            """
            Implementar a listagem das Faturas existentes
            TODO: Implementaçao da verificação de dados invalidos
            """
            imprime_lista(db_getfields('FATURA', False), db_show('FATURA', False))
# ------------------------------------------------------------
def menu_produtos():
    """Menu principal dos Produtos (Materiais e Serviços)"""
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
            """
            Implementar a criação de um Material
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_add_material(input('material: '), input('custo: '), input('preço: '), input('fornecedor: '), input('telefone: '), input('email: '), input('part_number: '))
        elif op == "2":
            """
            Implementar a atualização de um Material
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_update('MATRIAL', db_getfields('MATRIAL'), input('INSIRA O VALOR PARA O QUAL DESEJA ALTERAR: '), db_getfields('MATRIAL'), '=', input('INSIRA O VALOR DA CONDIÇÃO: '))
        elif op == "3":
            """
            Implementar a eliminação de um Material
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_delete('MATRIAL', db_getfields('MATRIAL'), '=', input('INSIRA O VALOR DA CONDIÇÃO: '))
            
        elif op == "4":
            """
            Implementar a listagem dos Materiais existentes
            TODO: Implementaçao da verificação de dados invalidos
            """
            imprime_lista(db_getfields('MATRIAL', False), db_show('MATRIAL', False))
        
        elif op == "5":
            """
            Implementar a criação de um serviço
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_add_servico(input('servico: '), input('preco: '), input('observacao: '))
        elif op == "6":
            """
            Implementar a atualização de um serviço
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_update('SERVICO', db_getfields('SERVICO'), input('INSIRA O VALOR PARA O QUAL DESEJA ALTERAR: '), db_getfields('SERVICO'), '=', input('INSIRA O VALOR DA CONDIÇÃO: '))
        elif op == "7":
            """
            Implementar a eliminação de um serviço
            TODO: Implementaçao da verificação de dados invalidos
            """
            db_delete('SERVICO', db_getfields('SERVICO'), '=', input('INSIRA O VALOR DA CONDIÇÃO: '))
            
        elif op == "8":
            """
            Implementar a listagem dos serviços existentes
            TODO: Implementaçao da verificação de dados invalidos
            """
            imprime_lista(db_getfields('SERVICO', False), db_show('SERVICO', False))
if __name__ == "__main__":
    menu()
