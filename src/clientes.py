
from bd import connector
# ------------------------------
def db_add_Cliente(v_nome, v_nif, v_cc, v_dob, v_morada, v_telefone, v_email):
    """
    Funcionalidade para adicionar um Cliente na base de dados.
    
    Args:
        v_nome (str): Nome do cliente a ser inserido.
        v_nif (int): NIF do cliente a ser inserido.
        v_cc (int): Cartão de cidadão do cliente a ser inserido.
        v_dob (date): Data de nascimento do cliente a ser inserido.
        v_morada (str): Morada do cliente a ser inserido.
        v_telefone (str): Telefone do cliente a ser inserido.
        v_email (str): Email do cliente a ser inserido.
    """
    conn, cursor = connector()
    cursor.execute('INSERT INTO CLIENTE (nome, nif, cc, dob, morada, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)', (v_nome, v_nif, v_cc, v_dob, v_morada, v_telefone, v_email))
    conn.commit()
    conn.close()
