from io_terminal import imprime_lista, pergunta_id
from bd import *

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"

def remover_cliente(lista_de_clientes):
    id_cliente = pergunta_id(questao="> ID do cliente: ", lista=lista_de_clientes, mostra_lista=True)
    if id_cliente is not None:
        lista_de_clientes.pop(id_cliente)

    return lista_de_clientes

def imprime_lista_de_clientes(lista_de_clientes):
    """TODO: documentação"""
    
    imprime_lista(cabecalho="Lista de clientes", lista=lista_de_clientes)

# ------------------------------

def db_show_Cliente():
    conn, cursor = connector()

    cursor.execute('SELECT * FROM CLIENTE')

    dados = cursor.fetchall()

    for linha in dados:
        print(linha)

    conn.close()

# ------------------------------

def db_add_Cliente(v_nome, v_nif, v_cc, v_dob, v_morada, v_telefone, v_email):
    conn, cursor = connector()

    cursor.execute('INSERT INTO CLIENTE (nome, nif, cc, dob, morada, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)', (v_nome, v_nif, v_cc, v_dob, v_morada, v_telefone, v_email))

    conn.commit()
    conn.close()
    
# ------------------------------

def db_update_Cliente(v_define_field, v_define_value, v_condition_field, v_condition_operator, v_condition_value):
    conn, cursor = connector()

    cursor.execute('UPDATE CLIENTE SET ' + v_define_field + ' = ? WHERE ' + v_condition_field + v_condition_operator + ' ?', (v_define_value, v_condition_value))

    conn.commit()
    conn.close()

# ------------------------------

def db_delete_Cliente(v_condition_field, v_condition_operator, v_condition_value):
    conn, cursor = connector()

    cursor.execute('DELETE FROM CLIENTE WHERE ' + v_condition_field + v_condition_operator + ' ?', (v_condition_value))

    conn.commit()
    conn.close()

# ------------------------------

if __name__ == "__main__":
    #db_show_Cliente()

    #db_add_Cliente('Joãoo', '12345', '12345', '12345', '12345', '123456', '12345')

    #db_update_Cliente('nome', 'Maria', 'id_cliente', '=', '10')

    #db_delete_Cliente('id_cliente', '=', '3')

    db_show_Cliente()