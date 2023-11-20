
from bd import connector
# ------------------------------
def db_add_ordem_reparacoes(v_id_cliente_or, v_id_veiculo_or, v_data_or, v_serviços):
    conn, cursor = connector()
    cursor.execute('INSERT INTO ORDEM_REPARACOES (id_cliente_or, id_veiculo_or, data_or, serviços) VALUES (?, ?, ?, ?)', (v_id_cliente_or, v_id_veiculo_or, v_data_or, v_serviços))
    conn.commit()
    conn.close()
