from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_materiais = "lista_de_materiais.pk"

def cria_novo_material():
    """Pedir os dados de um novo material para a lista de materiais

    :return: dicionario com o novo material, {"nome": <<nome>>, "custo": <<nif>>, ...}
    """
    material = input("> Material: ").capitalize()
    custo = input("> Custo: ")
    preço = input("> Preço de venda: ")
    stock = input("> Stock: ")
    fornecedor = input("> Fornecedor: ").capitalize()
    telefone = input("> Telefone fornecedor: ")
    email = input("> Email fornecedor: ").lower()
        
    material = {"material": material,
                "custo": custo,
                 "preço": preço,
                 "stock": stock,
                 "fornecedor": fornecedor,
                 "telefone": telefone,
                 "email": email
               }

    return material

def atualizar_material(lista_de_materiais):
    pass

def remover_material(lista_de_materiais):
    id_material = pergunta_id(questao="> ID do material: ", lista=lista_de_materiais, mostra_lista=True)
    if id_material is not None:
        lista_de_materiais.pop(id_material)

    return lista_de_materiais

def imprime_lista_de_materiais(lista_de_materiais):
    """TODO: documentação"""
    
    imprime_lista(cabecalho="Lista de materiais", lista=lista_de_materiais)