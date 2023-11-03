from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"

def cria_novo_cliente():
    """Pedir os dados de um novo cliente

    :return: dicionario com o novo cliente, {"nome": <<nome>>, "nif": <<nif>>, ...}
    """
    nome = input("> Nome: ").capitalize()
    nif = input("> NIF: ").upper()
    cc = input("> CC: ").upper()
    dob = input("> Data de Nascimento: ")
    morada = input("> Morada: ")
    telefone = input("> Telefone: ")
    email = input("> Email: ").lower()
        
    cliente = {"nome": nome,
               "nif": nif,
                "cc": cc,
                "dob": dob,
                "morada": morada,
                "telefone": telefone,
                "email": email
               }

    return cliente

def remover_cliente(lista_de_clientes):
    id_cliente = pergunta_id(questao="> ID do cliente: ", lista=lista_de_clientes, mostra_lista=True)
    if id_cliente is not None:
        lista_de_clientes.pop(id_cliente)

    return lista_de_clientes

def imprime_lista_de_clientes(lista_de_clientes):
    """TODO: documentação"""
    
    imprime_lista(cabecalho="Lista de clientes", lista=lista_de_clientes)