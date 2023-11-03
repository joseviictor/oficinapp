from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_serviços = "lista_de_serviços.pk"

def cria_novo_serviço():
    """Pedir os dados de um novo material para a lista de serviços

    :return: dicionario com o novo serviço, {"nome": <<nome>>, "custo": <<nif>>, ...}
    """
    serviço = input("> Serviço: ").capitalize()
    preço = input("> Preço de venda: ")
    observação = input("> Observação: ").capitalize()
        
    serviço = {"serviço": serviço,
                "preço": preço,
                "observação": observação
               }

    return serviço

def atualizar_serviço(lista_de_serviços):
    pass

def remover_serviço(lista_de_serviços):
    id_serviço = pergunta_id(questao="> ID do material: ", lista=lista_de_serviços, mostra_lista=True)
    if id_serviço is not None:
        lista_de_serviços.pop(id_serviço)

    return lista_de_serviços

def imprime_lista_de_serviços(lista_de_serviços):
    """TODO: documentação"""
    
    imprime_lista(cabecalho="Lista de serviços", lista=lista_de_serviços)