
from bd import connector
# ------------------------------
def db_add_fatura(v_id_veiculo_fatura, v_dataFatura):
    conn, cursor = connector()
    cursor.execute('INSERT INTO FATURA (id_veiculo_fatura, dataFatura) VALUES (?, ?)', (v_id_veiculo_fatura, v_dataFatura))
    conn.commit()
    conn.close()
