from bd import *
# ------------------------------
def db_add_Cliente(v_nome, v_nif, v_cc, v_dob, v_morada, v_telefone, v_email):
    conn, cursor = connector()
    cursor.execute('INSERT INTO CLIENTE (nome, nif, cc, dob, morada, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)', (v_nome, v_nif, v_cc, v_dob, v_morada, v_telefone, v_email))
    conn.commit()
    conn.close()
    
# ------------------------------
def db_delete_Cliente(v_condition_field, v_condition_operator, v_condition_value):
    conn, cursor = connector()
    cursor.execute('DELETE FROM CLIENTE WHERE ' + v_condition_field + ' ' + v_condition_operator + '\'' + v_condition_value + '\'' )
    conn.commit()
    conn.close()
# ------------------------------
# bloco de textes
if __name__ == "__main__":
    #db_show_Cliente()
    #db_add_Cliente('Joãoo', '12345', '12345', '12345', '12345', '123456', '12345')
    #db_delete_Cliente('id_cliente', '=', '3')
    db_show('CLIENTE')
