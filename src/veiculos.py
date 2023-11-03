from io_terminal import imprime_lista

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"

def cria_novo_veiculo():
    """Pede ao utilizador para introduzir um novo veiculo

    :return: dicionario com um veiculo na forma
        {"marca": <<marca>>, "matricula": <<matricula>>, ...}
    """
    
    matricula = input("> Matricula: ").upper()
    marca = input("> Marca: ").capitalize()
    modelo = input("> Modelo: ").capitalize()
    ano = input("> Ano: ")
    combustivel = input("> Combustivel: ").lower()
    kms = input("> Kms: ")
    cilindrada = input("> Cilindrada: ")
    cor = input("> Cor: ").lower()
    observacoes = input("> Observações: ")

    veiculo = {
               "marca": marca,
               "modelo": modelo,
               "matricula": matricula,
               "ano": ano,
               "combustivel": combustivel,
               "kms": kms,
               "cilindrada": cilindrada,
               "cor": cor,
               "observacoes": observacoes
              }

    return veiculo

def imprime_lista_de_veiculos(lista_de_veiculos):
    """TODO: documentação"""

    imprime_lista(cabecalho="Lista de Veiculos", lista=lista_de_veiculos)