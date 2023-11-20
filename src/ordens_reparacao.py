
from bd import connector
# ------------------------------
def db_add_ordem_reparacoes(v_id_cliente_or, v_id_veiculo_or, v_data_or, v_serviços):
    """
    Funcionalidade para adicionar uma ordem de reparações na base de dados.
    Args:
    v_id_cliente_or (str): ID do cliente que realizou a ordem de reparações.
    v_id_veiculo_or (str): ID do veículo da ordem de reparações.
    v_data_or (str): Data em que foi realizada a ordem de reparações.
    v_serviços (str): descreve o serviço.
    """
    conn, cursor = connector()
    cursor.execute('INSERT INTO ORDEM_REPARACOES (id_cliente_or, id_veiculo_or, data_or, serviços) VALUES (?, ?, ?, ?)', (v_id_cliente_or, v_id_veiculo_or, v_data_or, v_serviços))
    conn.commit()
    conn.close()
