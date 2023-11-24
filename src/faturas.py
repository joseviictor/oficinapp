
from bd import connector
# ------------------------------
def db_add_fatura(v_id_cliente_fatura, v_id_veiculo_fatura, v_dataFatura):
    """
    Função para adicionar faturas na base de dados.
    Args:
        v_id_veiculo_fatura (int) : ID do veículo da fatura.
        v_dataFatura (str) : Data da fatura.
        
    
    """
    
    conn, cursor = connector()
    cursor.execute('INSERT INTO FATURA (id_cliente_fatura, id_veiculo_fatura, dataFatura) VALUES (?, ?, ?)', (v_id_cliente_fatura, v_id_veiculo_fatura, v_dataFatura))
    conn.commit()
    conn.close()
