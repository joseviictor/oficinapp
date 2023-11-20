
from io_terminal import imprime_lista, pergunta_id
from bd import *
# ------------------------------
def db_add_Cliente(v_nome, v_nif, v_cc, v_dob, v_morada, v_telefone, v_email):
    conn, cursor = connector()
    cursor.execute('INSERT INTO CLIENTE (nome, nif, cc, dob, morada, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)', (v_nome, v_nif, v_cc, v_dob, v_morada, v_telefone, v_email))
    conn.commit()
    conn.close()
# ------------------------------
# bloco de textes
if __name__ == "__main__":
    #db_show_Cliente()
    #db_add_Cliente('Joãoo', '12345', '12345', '12345', '12345', '123456', '12345')
    db_show('CLIENTE')
