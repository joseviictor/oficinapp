
from bd import connector
# ------------------------------
def db_add_Cliente(v_nome, v_nif, v_cc, v_dob, v_morada, v_telefone, v_email):
    conn, cursor = connector()
    cursor.execute('INSERT INTO CLIENTE (nome, nif, cc, dob, morada, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)', (v_nome, v_nif, v_cc, v_dob, v_morada, v_telefone, v_email))
    conn.commit()
    conn.close()

